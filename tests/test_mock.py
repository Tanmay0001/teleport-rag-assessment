from src.mocks.vertexai_mock import GenerativeModel


def test_query_expansion():

    model = GenerativeModel()

    response = model.generate_content(
        "How does the system handle peak load?"
    )

    assert len(response.text) > 0