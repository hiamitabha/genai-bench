# Benchmarking LLM Inference APIs provide by Cloud Services
Cloud Providers such as Together AI, Anyscale enables developer to build applications with access to APIs for open source machine learning models.
This code attempts to benchmark LLM Inference APIs, demostrates how they work and compares models provided
Reports the end to end time for API response time for one token, which becomes the equivalent of Time To First Token (TTFT).

The distinguishing part about this benchark is that it issues requests to all providers/models in parallel, so you get
a fair apples-to-apples analysis of all the endpoints.

# Usage:
First add all the required vendors, models, and API Keys in the configuration file. The configuration file should look like:
[
    {
        "vendor": "togetherai",
        "model": "togethercomputer/llama-2-7b-chat",
        "api_key": "<Insert API Key here>"
    },
    {
        "vendor": "anyscale",
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "api_key": "<Insert API Ley here>"
    }
]
You can replace the model with your favorite one. You can also compare multiple models from the same provider.

Then Run:
python3 benchmark.py

# How to get the API Key for a large language model provider:

Here we take the example of Together AI. Other vendors have siilar steps
1. Sign up for Together API access at https://api.together.xyz
2. Start your favorite Large Language Model (LLM). Right now the benchmark expects the model to be up and running
3. Retrieve your API key from the settings portion of your profile.
4. Supply the model and the API key in the example above.

# Example results
Here are a few example results. At the end of all the iterations, the benchark plots a comparison in the provided results file.


# Repository of results
A detailed spreadsheet of results is available here: http://llms.learnwitharobot.com

