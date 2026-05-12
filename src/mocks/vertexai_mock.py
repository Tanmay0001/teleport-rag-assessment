class GenerativeModel:

    def __init__(self, model_name="mock-gemini"):
        self.model_name = model_name

    def generate_content(self, prompt):

        prompt_lower = prompt.lower()

        if "peak load" in prompt_lower:
            expanded = """
How does the distributed system manage high traffic spikes using
autoscaling, load balancing, asynchronous queues, and scalable infrastructure?
"""

        elif "database" in prompt_lower:
            expanded = """
How are database operations optimized using pooling, concurrency
management, and efficient connection handling?
"""

        elif "retrieval" in prompt_lower:
            expanded = """
How does semantic vector retrieval work using embeddings,
cosine similarity, vector databases, and query expansion?
"""

        else:
            expanded = f"""
{prompt}

Include related technical concepts and semantic context.
"""

        return type(
            "Response",
            (),
            {"text": expanded}
        )