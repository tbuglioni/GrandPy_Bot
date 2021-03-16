from GrandPy.controller.process_post import ProcessPost
from GrandPy.views import app
from flask import json


def test_processing_views():
    with app.app_context():
        test = ProcessPost("antibes")
        result = test.processing()
        data = json.loads(result.get_data(as_text=True))
        expected_result = 200
        assert result.status_code == expected_result
        assert data["lat"] == 43.58041799999999
