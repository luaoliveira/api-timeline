import pytest 

def simounao(app):

    assert app.name == 'Simporter.app'

def test_config_is_loaded(config):
    assert config["DEBUG"] is False

# cliente = faz a request na nossa aplicação para teste
def test_request_returns_404(client):
    assert client.get("/url_aleatoria").status_code == 404

#def test_request_succeeded(client):
    #assert client.get("/api/info").status_code == 200

def test_request(live_server):
    assert client.get("/api/info").status_code == 200