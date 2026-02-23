import faiss
import numpy as np

class VectorStore:
    def __init__(self, embeddings):
        dim = embeddings.shape[1] #how long each list  is
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query_embedding, k):
        _, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return indices[0]  # first query output 

#query_embedding = the numbers representing the question
#K > how many closest matches we want to find

#_ → how far each match is 
#indices → which positions in the box are the closest chunks