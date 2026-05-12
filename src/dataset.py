TECHNICAL_CORPUS = [
    {
        "id": "doc_001",
        "text": """
Auto-scaling allows distributed systems to handle peak traffic efficiently.
When CPU or memory usage exceeds thresholds, additional compute instances
are automatically provisioned. Kubernetes Horizontal Pod Autoscaler monitors
resource metrics and scales workloads dynamically to maintain low latency.
"""
    },
    {
        "id": "doc_002",
        "text": """
Load balancers distribute incoming traffic across multiple backend services.
Round-robin and least-connections routing strategies help prevent overload
on individual servers and improve system availability during traffic spikes.
"""
    },
    {
        "id": "doc_003",
        "text": """
Retrieval-Augmented Generation improves factual accuracy by retrieving
relevant documents before generating responses. User queries are embedded,
matched against vector indexes, and the top chunks are passed into the LLM.
"""
    },
    {
        "id": "doc_004",
        "text": """
FAISS enables efficient similarity search across dense vector embeddings.
Cosine similarity is commonly used for semantic retrieval because it compares
vector direction rather than magnitude.
"""
    },
    {
        "id": "doc_005",
        "text": """
Query expansion improves semantic retrieval by rewriting short user queries
into richer context-aware descriptions. Expanded queries often improve recall
by including related technical terminology and synonyms.
"""
    },
    {
        "id": "doc_006",
        "text": """
Kafka supports event-driven microservices through asynchronous message queues.
Services can process traffic independently, absorb bursts, and scale consumers
horizontally without blocking upstream systems.
"""
    },
    {
        "id": "doc_007",
        "text": """
Database connection pooling improves throughput under high concurrency.
PgBouncer reduces connection overhead by reusing active database sessions
instead of creating new connections for every request.
"""
    },
    {
        "id": "doc_008",
        "text": """
Vertex AI Vector Search provides a managed vector database service on GCP.
FAISS indexes can be migrated by exporting embeddings to Cloud Storage and
deploying them into Vertex AI Matching Engine indexes.
"""
    }
]