import numpy as np
from numpy import linalg
import operator

class Retriever:
    """Class that performs the retrieval in the RAG system,
    given a query and the database where to look into retrieves
    the most similar chunks of documents to those of the input query"""
    def __init__(self, database: list[dict]):
        self.database = database

    @staticmethod
    def cosine_similarity(a: list[float], b: list[float]) -> float:
        distance = 0.0
        np_a = np.array(a)
        np_b = np.array(b)
        distance = (np.dot(np_a, np_b)) / (linalg.norm(np_a) * linalg.norm(np_b))
        return distance

    def search(self, query: list[float], k: int=3) -> list[str]:
        """Function that given the database it works on and the embedded
        input query returns the list of the top-k chunks matching in the database"""
        scores = {}
        for item in self.database:
            temp_dis = self.cosine_similarity(item["embedding"], query)
            scores[item["text"]] = temp_dis
        # sorts the dict according to the values (distances)    
        res = dict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))
        return list(res.keys())[:k]