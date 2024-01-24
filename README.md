# Benchmarking LLM Inference APIs provide by Cloud Services
Cloud services such as Togethe, Anyscale, and others enable developers to build applications with access to APIs for open source machine learning models.
This code attempts to benchmark LLM Inference APIs and demostrates how they work.
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

<code>
python3 benchmark.py togethercomputer/llama-2-7b-chat e870071a84b339d1bf3e1d6f5e5338601afb9db0633c38eda1244df9aba560b5
Performance results for model togethercomputer/llama-2-7b-chat
Iteration #, Date/Time, API response time(s)
0,10/28/2023 23:11:08,0.44153342099980364
1,10/28/2023 23:16:08,0.4318333090000124
2,10/28/2023 23:21:09,0.4267277169992667
3,10/28/2023 23:26:09,0.40943820099982986
4,10/28/2023 23:31:10,1.295396979000543
5,10/28/2023 23:36:11,0.42362863200014544
6,10/28/2023 23:41:12,0.37723448099950474
7,10/28/2023 23:46:12,0.4338321889999861
<code>

# Repository of results
A detailed spreadsheet of results is available here: http://llms.learnwitharobot.com

