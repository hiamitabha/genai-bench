# Benchmarking Together APIs
Together is a service that enables developers to build applications with access to APIs for open source machine learning models.
This code attempts to benchmark Together APIs and demostrates how they work.
Reports the end to end time for API access and the token generation time reported by together.

# Usage:
python3 benchmark.py togethercomputer/RedPajama-INCITE-7B-Instruct <API_key>

# How to Use:
1. Sign up for Together API access at https://api.together.xyz
2. Start your favorite Large Language Model (LLM). Right now the benchmark expects the model to be up and running
3. Retrieve your API key from the settings portion of your profile.
4. Supply the model and the API key in the example above.

# Example results
Here are a few example results:

$ python3 benchmark.py togethercomputer/RedPajama-INCITE-7B-Instruct <api key>
Performance results for model togethercomputer/RedPajama-INCITE-7B-Instruct
API end to end time in seconds 0.3629
Together reported compute time in seconds 0.0400

$ python3 benchmark.py togethercomputer/RedPajama-INCITE-Instruct-3B-v1 <api key>
Performance results for model togethercomputer/RedPajama-INCITE-Instruct-3B-v1
API end to end time in seconds 0.3474
Together reported compute time in seconds 0.0372

python3 benchmark.py togethercomputer/falcon-40b <api key> 
Performance results for model togethercomputer/falcon-40b
API end to end time in seconds 0.7129
Together reported compute time in seconds 0.1936
