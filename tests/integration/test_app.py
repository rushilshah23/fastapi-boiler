# tests/test_app.py
def test_health_check(test_app):
    response = test_app.get("/api/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert "healthy" in json_data["message"]
