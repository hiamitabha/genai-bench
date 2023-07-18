import requests
import time
import sys

_TOGETHER_ENDPOINT = 'https://api.together.xyz/inference'

def time_request(model, api_key):
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

def main(model, api_key):
    (api_time, compute_time) = time_request(model,
                                            api_key)
    if api_time: 
        print (f"Performance results for model {model}")
        print (f"API end to end time in seconds {api_time:0.4f}")
        print (f"Together reported compute time in seconds {compute_time:0.4f}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print ("Usage: python3 benchmark.py <model> <api key> e.g.")
        print ("python3 benchmark.py togethercomputer/RedPajama-INCITE-7B-Instruct <api key from Together>")
        exit()
    main(sys.argv[1], sys.argv[2])
