import requests

class VanillaEmbedder:
    """Class that handles the HTTP requests 
and APIs logic to perform the embedding 
of the given chunk."""
    def __init__(self, base_url: str = 'http://localhost:11434', model_name: str = 'nomic-embed-text'):
        self.base_url = base_url
        self.model_name = model_name
    
    def get_embed(self, in_string: str) -> list[float]:
        embed_api_url = self.base_url + '/api/embed'
        payload = {
            "model": self.model_name,
            "input": in_string
        }
        response = requests.post(embed_api_url, json=payload)
        response.raise_for_status()
        result = response.json()['embeddings'][0]
        #print(result)
        return result