_TOGETHER_ENDPOINT = "https://api.together.xyz/inference"

class Together:
    def __init__(self, model, api_key, prompt, top_p=1, top_k=40, temperature=0.1,
                 max_tokens=1, repetition_penalty=1):
        self.model = model
        self.api_key = api_key
        self.prompt = prompt
        self.top_p = top_p
        self.top_k = top_k
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.repetition_penalty = repetition_penalty

    def get_payload(self):
        payload = { 
            "model": self.model,
            "prompt": self.prompt,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "repetition_penalty": self.repetition_penalty 
        }
        return payload

    def get_header(self):
        header = {
            "Authorization": "Bearer %s" % self.api_key,
            "User-Agent": "Learn With A Robot"
        }
        return header

    @staticmethod
    def get_endpoint():
        return _TOGETHER_ENDPOINT

    @staticmethod
    def process_result(result): 
        if result.get('status') == 'finished':
            compute_time = result['output'].get('raw_compute_time')
            return (True, compute_time)
        else:
            print (result)
            return (False, None)
