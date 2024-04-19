# GenAI-Bench: Benchmarking Large Language Models (LLMs) Inference APIs provide by Cloud Providers
Cloud Providers such as Together AI, Anyscale, etc, enable developers to build applications with access to APIs for open source Large Language Models (LLMs).
GenAI-Bench attempts to benchmark LLM Inference APIs, demostrate how they work, and compare models provided.
The benchmark reports the end to end time for API response time for one token, which becomes the equivalent of Time To First Token (TTFT).

The distinguishing feature about this benchmark is that it issues requests to all providers/models concurrently, so you get
a fair apples-to-apples analysis of all the endpoints. The TTFT reported can be easiily compared bewteen the different providers/models.

# Usage:
First add all the required vendors, models, and API Keys in the configuration file (config.json). The configuration file should look like:
<code>
[
    {
        "vendor": "togetherai",
        "model": "togethercomputer/llama-2-7b-chat",
        "api_key": "Insert API Key here"
    },
    {
        "vendor": "anyscale",
        "model": "meta-llama/Llama-2-7b-chat-hf",
        "api_key": "Insert API Key here"
    }
]

</code>

You can replace the model with your favorite one. You can also compare multiple models from the same provider.
As an example, the following config file compares Llama2-7B vs Llama2-70B from Together AI

<code>
[
    {
        "vendor": "togetherai",
        "model": "togethercomputer/llama-2-7b-chat",
        "api_key": "Insert API Key here"
    },
    {
        "vendor": "togetherai",
        "model": "togethercomputer/llama-2-70b-chat",
        "api_key": "Insert API Key here"
    }
]

</code>
Then Run:

<code>python3 benchmark.py</code>


Optional arguments allow you to change the number of iterations, time between iterations, and input file used to load tokens.

# How to get the API Key for a large language model provider:

Here we take the example of Together AI. Other vendors have similar steps
1. Sign up for Together API access at https://api.together.xyz
2. Retrieve your API key from the settings portion of your profile.
3. Supply the model and the API key in the example above.

# Example results
The benchmark reports the results per iteration in CSV format. At the end of all the iterations, the benchmark plots a comparison in the provided results file.

Here are is an example result:

<code>
python3 benchmark.py 
Iteration #, Date/Time, Model Name, Vendor, API response time(s)
0,togethercomputer/llama-2-7b-chat,togetherai,02/05/2024 00:01:42,0.6702483710005254
0,meta-llama/Llama-2-7b-chat-hf,anyscale,02/05/2024 00:01:42,0.7416756729999179
  </code>
  
The above is the result of one iteration.

The following plot compares the Llama2-7B-chat model provided by Together AI and Anyscale. Data was collected on 2/5/2024 between 10AM PST and 12PM PST.

![Comparison between Together AI and Anyscale](https://github.com/hiamitabha/genai-bench/blob/main/results/result-together_vs_anyscale_llama27b.png?raw=true)

The following plot compares the Llama2-7B-chat model and Llama2-70B-chat model provided by Together AI. Data was collected on 2/5/2024 between 6PM PST and 8PM PST.

![Comparison between Llama2-7B-chat vs Llama2-70B-chat at Together AI](https://raw.githubusercontent.com/hiamitabha/genai-bench/main/results/result-together_llama2_7b_vs_70b.png)

The following plot compares the Llama2-7B-chat model and the Llama3-8B-chat models provided by Together AI. The comparison was generated on the day Llama3 was made available by Together AI.

![Comparison between Llama2 and Llama3](https://raw.githubusercontent.com/hiamitabha/genai-bench/main/results/result-together_llama2_7b_vs_llama3_8b.png)

# Repository of results
A detailed spreadsheet of results is available here: http://llms.learnwitharobot.com

