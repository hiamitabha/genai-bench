from providers.provider import Provider
import json

_SAMBANOVA_ENDPOINT = "https://api.sambanova.ai/v1/chat/completions"

class Sambanova(Provider):
    def __init__(self, model, api_key, prompt, top_p=1, top_k=40, temperature=0.1,
                 max_tokens=1, repetition_penalty=1):
        Provider.__init__(self, model, api_key, prompt,
                           top_p, top_k, temperature,
                           max_tokens, repetition_penalty)

    def get_payload(self):
        payload = { 
            "model": self.model,
            "messages": [
                {
                   "role": "system",
                   "content": "You are a helpful assistant"
                },
                {
                   "role": "user",
                   "content": self.prompt
                }
            ],
            "top_p": self.top_p,
            "top_k": self.top_k,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stream": True 
        }
        return payload

    def get_header(self):
        header = {
            "Authorization": "Bearer %s" % self.api_key,
            "Content-Type": "application/json"
        }
        return header

    @staticmethod
    def get_endpoint():
        return _SAMBANOVA_ENDPOINT

    def process_result(self, result):
        if result.status_code == 200:
            lines = result.text.split('\n')
            for line in lines:
                if line and len(line)>6:
                    data = json.loads(line[6:])
                    choices = data.get('choices')
                    for choice in choices:
                        delta = choice.get('delta')
                        if delta.get('content') and len(delta.get('content')) > 0:
                            return (True, None)
        return (False, None) 
