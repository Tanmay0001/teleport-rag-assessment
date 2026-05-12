from src.retrieval_engine import RetrievalEngine


def test_strategy_a_returns_results():

    engine = RetrievalEngine()

    results = engine.strategy_a(
        "How does autoscaling work?"
    )

    assert len(results) == 3