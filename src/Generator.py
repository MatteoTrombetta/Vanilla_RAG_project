import requests

class Generator:
    """Class that generate an answer according to the provided context through HTTP requests to the LLM model 'llama3'"""
    def __init__(self, model: str = 'llama3', base_url: str= 'http://localhost:11434'):
        self.model = model
        self.base_url = base_url

    def generate_answer(self, query: str, db_chunks: list[str]) -> str:
        chunks_str = "\n".join(db_chunks)

        prompt = f"""You are an assistant. Answer the question bu ONLY using the following context.
        If the answer is not in the context say that you can't answer.
        
        CONTEXT:
        {chunks_str}

        QUESTION: {query}"""
        
        json_message = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        res = requests.post(url=self.base_url+'/api/generate', json=json_message)
        res.raise_for_status()

        answer = res.json()["response"]

        return answer