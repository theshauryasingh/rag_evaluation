Retrieval-Augmented Generation (RAG)

Retrieval-Augmented Generation (RAG) is a method that combines information retrieval with text generation to produce more accurate and contextually relevant responses. In RAG, a model is augmented with external knowledge retrieved from a large corpus of documents, enabling it to generate responses that go beyond its pre-trained knowledge. This approach is particularly useful for tasks requiring up-to-date information, domain-specific knowledge, or factual accuracy, such as question-answering, summarization, and knowledge-grounded conversation.

How RAG Works

1. Retrieval Phase: Given a query, a retriever model (e.g., a dense retriever like DPR or a bi-encoder such as all-MiniLM-L6-v2) searches a document corpus for relevant passages. These retrieved passages act as reference material for the next stage, providing factual grounding for the response.

2. Generation Phase: The query and retrieved passages are then fed to a generative model (e.g., T5 or GPT) to synthesize a coherent and relevant response. By integrating retrieved information, the generative model is less likely to “hallucinate” and more likely to provide accurate information based on the retrieved documents.

This two-phase setup allows RAG models to dynamically access external knowledge, producing responses that are both informed and responsive to the query context.

Basic RAG Evaluation with Cosine Similarity

\===========================================

This project demonstrates a simple evaluation of a \*\*Retrieval-Augmented Generation (RAG)\*\* model. The script retrieves relevant documents based on a query, generates a summary, and evaluates the generated summary using relevance scoring (cosine similarity).

Types of RAG Evaluation Metrics

\-------------------------------

Evaluating RAG models can involve various metrics, depending on the task type and objective. Here's an overview:

1\. \*\*BLEU (Bilingual Evaluation Understudy)\*\*:

\- Typically used in machine translation.

\- Measures overlap between generated and reference text at the n-gram level.

\- Effective for assessing content similarity but may not align well with RAG tasks where wording diversity is high.

2\. \*\*ROUGE (Recall-Oriented Understudy for Gisting Evaluation)\*\*:

\- Commonly used for summarization tasks.

\- Measures n-gram and longest common subsequence overlap.

\- Good for evaluating content capture, especially in text summarization.

3\. \*\*Precision/Recall Metrics\*\*:

\- Useful for binary relevance tasks, where specific terms or phrases need to be detected in generated content.

\- Suitable for retrieval tasks but limited for assessing nuanced responses in generative tasks.

4\. \*\*Relevance Scoring (Cosine Similarity)\*\*:

\- Measures semantic similarity between query and response embeddings.

\- Ideal for assessing relevance in RAG systems, where the generated text should semantically align with the query.

\- Used here for its simplicity and effectiveness in capturing semantic context in RAG tasks.

5\. \*\*Human Evaluation\*\*:

\- Involves direct assessment by human evaluators for fluency, coherence, and relevance.

\- While reliable, human evaluation is time-consuming and may introduce bias. It's often used as a benchmark.

Chosen Evaluation Type: Cosine Similarity

\-----------------------------------------

For this task, we use \*\*cosine similarity\*\* to measure relevance. This metric is well-suited for RAG systems as it captures the semantic closeness of the generated response to the input query without relying on exact text matching. Cosine similarity offers a quantitative assessment of content relevance, essential for verifying if generated responses align with the user's query intent.
