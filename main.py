from src.benchmarker import Benchmarker
import json


def main():

    benchmarker = Benchmarker()

    results = benchmarker.save_results()

    print("\n")
    print("=" * 70)
    print("Semantic RAG Benchmark Results")
    print("=" * 70)

    for result in results:

        print("\n")
        print(f"QUERY: {result['query']}")

        print("\nStrategy A Results:")

        for item in result["strategy_a"]:

            print(
                f"Rank: {item['rank']} | "
                f"Score: {round(item['score'], 4)}"
            )

        print("\nStrategy B Results:")

        print(
            f"Expanded Query: "
            f"{result['strategy_b']['expanded_query']}"
        )

        for item in result["strategy_b"]["results"]:

            print(
                f"Rank: {item['rank']} | "
                f"Score: {round(item['score'], 4)}"
            )

    print("\n")
    print("Benchmark JSON saved in outputs/")
    print("=" * 70)


if __name__ == "__main__":
    main()