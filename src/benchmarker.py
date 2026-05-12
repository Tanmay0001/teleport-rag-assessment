import json
from src.retrieval_engine import RetrievalEngine


QUERIES = [
    "How does the system handle peak load?",
    "How does query expansion improve retrieval?",
    "How are database operations optimized?"
]


class Benchmarker:

    def __init__(self):

        self.engine = RetrievalEngine()

    def run(self):

        benchmark_results = []

        for query in QUERIES:

            strategy_a_results = self.engine.strategy_a(query)

            strategy_b_results = self.engine.strategy_b(query)

            benchmark_results.append({

                "query": query,

                "strategy_a": strategy_a_results,

                "strategy_b": strategy_b_results
            })

        return benchmark_results

    def save_results(self):

        results = self.run()

        with open(
            "outputs/retrieval_benchmark.json",
            "w"
        ) as f:

            json.dump(results, f, indent=2)

        return results