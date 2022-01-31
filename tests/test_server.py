import pytest 

# cliente = faz a request na nossa aplicação para teste
def test_request_returns_404(client):
    assert client.get("/url_aleatoria").status_code == 404
