from providers.provider import Provider

_ANYSCALE_ENDPOINT = "https://api.endpoints.anyscale.com/v1/chat/completions"
class Anyscale(Provider):

    def __init__(self, model, api_key, prompt, top_p=1, top_k=40, temperature=0.1,
                 max_tokens=2, repetition_penalty=1):
        Provider.__init__(self, model, api_key, prompt,
                           top_p, top_k, temperature,
                           max_tokens, repetition_penalty)

    def get_payload(self):
        payload = {
            "model": self.model,
            "messages": [{"role": "system", "content": "You need to answer questions in a single word."}, 
               {"role": "user", "content": self.prompt}],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens 
        }
        return payload

    def get_header(self):
        header = headers={"Authorization": f"Bearer {self.api_key}"}
        return header

    @staticmethod
    def get_endpoint():
        return _ANYSCALE_ENDPOINT

    def process_result(self, result): 
        usage = result.get("usage")
        if usage:
            completion_tokens = usage.get("completion_tokens")
            if completion_tokens and completion_tokens <= self.max_tokens:
                return (True, None)
            else:
                print (result)
                return (False, None)
        else:
            print (result)
            return (False, None)

