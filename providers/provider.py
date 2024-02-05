from abc import abstractmethod
class Provider:
    """
        Provider is an abstract class which encapsulates the routines
        that all large language model provders should implement. 
    """

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
        #results maintains a tuple of timestamp and value
        self.results = []
 
    @abstractmethod 
    def get_payload(self):
        pass

    @abstractmethod
    def get_header(self):
        pass

    def append_result(self, timestamp, value):
        self.results.append((timestamp, value))

    def get_result(self):
        return self.results

    @abstractmethod
    def get_endpoint():
        pass
    
    @abstractmethod
    def process_result(self, result):
        pass
