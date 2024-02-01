import requests
import time
import sys
import threading
import argparse
import json
from datetime import datetime

from providers.together_ai import Together
from providers.anyscale import Anyscale

def time_request(llm_instance):
    """Issue a sample inference query using the provided llm_instance
       Optionally returns the compute time reported by the llm_instance
       if it was reported by the service. (e.g. Togetehr AI reported the compute time
       at one point although they do not report any more)
       :param llm_instance An instance of a llm model serviced by an API
    """
    try:
        start = time.perf_counter()
        res = requests.post(llm_instance.get_endpoint(), json=llm_instance.get_payload(), headers=llm_instance.get_header())
        end = time.perf_counter()
        result = res.json()
        api_time = end - start
        is_result_valid, details = llm_instance.process_result(result)
        if (is_result_valid):
            return (api_time, details)
        else:
            return (None, None)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)  

def test_api(llm_instance, model_name, vendor, iterations=10, sleep_in_seconds=30):
    """Test a model for a specified number of iterations
    :param llm_instance An instance of a llm model serviced by an API
    :param model Model name. Only used for the purposes of reporting.
    :param vendor Vendor whose API is tested. Only used for the purposes of reporting.
    :param iterations Total number of iterations for monitoring
    :param sleep_in_seconds Seconds to sleep before next iteration of test
    """
    for i in range(iterations):
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        (api_time, compute_time) = time_request(llm_instance)
        print (f"{i},{model_name},{vendor},{dt_string},{api_time}")
        time.sleep(sleep_in_seconds)

def run_threads(config_file, iterations, sleep):
    """
        Open the config file and run requested APIs in parallel
    """
    num_models = 0
    thread_pool = []
    with open(config_file) as json_file:
        model_list = json.load(json_file)
        for model_det in model_list:
           vendor = model_det.get("vendor")
           model = model_det.get("model")
           api_key = model_det.get("api_key")
           num_models += 1
           if vendor == "togetherai":
               model_instance = Together(model, api_key, "What is the capital of France?")
               thread = threading.Thread(target=test_api, args=(model_instance, model, vendor, iterations, sleep))
               thread_pool.append(thread)
           elif vendor == "anyscale":
               model_instance = Anyscale(model, api_key, "What is the capital of France?")
               thread = threading.Thread(target=test_api, args=(model_instance, model, vendor, iterations, sleep))
               thread_pool.append(thread)

    print (f"Iteration #, Date/Time, Model Name, Vendor, API response time(s)")

    for thread in thread_pool:
        thread.start()

    for thread in thread_pool:
        thread.join()

def parse_args():
   parser = argparse.ArgumentParser("Benchmark multiple LLMs simultaneously")
   parser.add_argument("-i", "--iterations", type=int, default=10,
                       help="Number of iterations to run for each LLM model")
   parser.add_argument("-s", "--sleep", type=int, default=30,
                       help="Time to sleep between iteratione")
   parser.add_argument("-c", "--config", default="config.json",
                       help="Configuration file which lists LLM API Keys")
   args = parser.parse_args()
   return args

if __name__ == "__main__":
    args = parse_args()
    run_threads(args.config, args.iterations, args.sleep)
