import ollama

class OllamaEmbedder:
    """Class that handles the HTTP requests 
and APIs logic to perform the embedding 
of the given chunk. We will be using ollama
for simiplicity (it's required to run the server
using the command 'ollama serve' in cmd)"""
    def __init__(self, model_name: str = 'nomic-embed-text'):
        self.model_name = model_name

    def get_embed(self, in_string: str) -> list[float] :
        response = ollama.embed(
            model=self.model_name,
            input=in_string
        )
        #print(response["embeddings"][0])        
        return response["embeddings"][0]