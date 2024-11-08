import torch
from sentence_transformers import SentenceTransformer, util

def retriever(retriever_model, query, documents):
    retriever = SentenceTransformer(retriever_model)
    doc_embeddings = retriever.encode(documents, convert_to_tensor=True)
    
    query_embedding = retriever.encode(query, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(query_embedding, doc_embeddings)
    
    # Retrieve the top document based on similarity score
    top_doc_index = torch.argmax(cosine_scores).item()
    retrieved_doc = documents[top_doc_index]
    
    return retriever, query_embedding, retrieved_doc
