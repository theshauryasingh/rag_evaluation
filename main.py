import torch, logging, os
from sentence_transformers import util
from generator import generator
from retriever import retriever
from document_extractor import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

query = "Explain the basics of AI"

documents = document_extractor(os.path.join(os.getcwd(), "documents.txt"))
retriever, query_encoding, retrieved_doc = retriever('all-MiniLM-L6-v2', query, documents)
generated_response = generator('t5-small', 't5-small', query_encoding)

logger.info(f"Query: {query}")
logger.info(f"Genrated response: {generated_response}")
logger.info(f"Retrieved doc: {retrieved_doc}")

response_embedding = retriever.encode(generated_response, convert_to_tensor=True)
similarity_score = util.pytorch_cos_sim(query_encoding, response_embedding).item()
logger.info(f"Evaluation : Cosine Similarity with Query: {similarity_score}")
