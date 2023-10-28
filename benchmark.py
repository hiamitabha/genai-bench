import requests
import time
import sys
from datetime import datetime

_TOGETHER_ENDPOINT = 'https://api.together.xyz/inference'

def time_request(model, api_key):
    """Issue a sample payload to the Together AI server for the specified
       model and time the API response. Optionally returns the compute time reported by Together
       if it was reported by the service
       :param model Model name
       :param api_key Together API Key
    """
    payload = { 
        "model": model,
        "prompt": """\
              The capital of France is   """,
        "top_p": 1,
        "top_k": 40,
        "temperature": 0.1,
        "max_tokens": 1,
        "repetition_penalty": 1
    }
    headers = {
        "Authorization": "Bearer %s" % api_key,
        "User-Agent": "Learn With A Robot"
    }
    try:
        start = time.perf_counter()
        res = requests.post(_TOGETHER_ENDPOINT, json=payload, headers = headers)
        end = time.perf_counter()
        result = res.json()
        if result.get('status') == 'finished':
            compute_time = result['output'].get('raw_compute_time')
            api_time = (end - start)
            return (api_time, compute_time)
        else:
            print (result)
            return (None, None)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)  

def test_api(model, api_key, iterations=100, sleep_in_seconds=300):
    """Test a model for a specified number of iterations
    :param model Model that needs to be tested
    :param api_key Together API Key
    :param iterations Total number of iterations for monitoring
    :param sleep_in_seconds Seconds to sleep before next iteration of test
    """
    print (f"Performance results for model {model}")
    print (f"Iteration #, Date/Time, API response time(s)")

    for i in range(iterations):
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        (api_time, compute_time) = time_request(model,
                                                api_key)
        print (f"{i},{dt_string},{api_time}")
        time.sleep(sleep_in_seconds)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Usage: python3 benchmark.py <model> <api key> e.g.")
        print ("python3 benchmark.py togethercomputer/RedPajama-INCITE-7B-Instruct <api key from Together>")
        exit()
    test_api(sys.argv[1], sys.argv[2])
