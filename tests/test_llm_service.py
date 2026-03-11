import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from service.llm_service import classify_question
from unittest.mock import patch


def test_classify_question():

    class FakeResponse:
        output_text = "student_courses"

    with patch("service.llm_service.client.responses.create") as mock_create:

        mock_create.return_value = FakeResponse()

        result = classify_question("What courses am I taking?")

        assert result == "student_courses"