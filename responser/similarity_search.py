import numpy as np
from scipy.spatial import distance
from responser.find_answer_db import matrix
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('keepitreal/vietnamese-sbert')


# embedding question
def encode(question):
    embedding = [model.encode(question)]
    return embedding


# Find the most similar question
def find_similar(question):
    vector = encode(question)
    matrix_plus = np.vstack(matrix)
    distances = distance.cdist(vector, matrix_plus, "cosine")[0]
    min_index = np.argmin(distances)
    min_distance = distances[min_index]
    max_similarity = 1 - min_distance
    return max_similarity, matrix[min_index]

