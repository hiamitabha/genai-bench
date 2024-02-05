from providers.provider import Provider

_TOGETHER_ENDPOINT = "https://api.together.xyz/inference"

class Together(Provider):
    def __init__(self, model, api_key, prompt, top_p=1, top_k=40, temperature=0.1,
                 max_tokens=1, repetition_penalty=1):
        Provider.__init__(self, model, api_key, prompt,
                           top_p, top_k, temperature,
                           max_tokens, repetition_penalty)

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

    def process_result(self, result):
        if result.get('status') == 'finished':
            compute_time = result['output'].get('raw_compute_time')
            return (True, compute_time)
        else:
            print (result)
            return (False, None)
