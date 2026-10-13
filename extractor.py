import json

from core.llm import invoke
from prompts.Extractor_Prompt import EXTRACTOR_PROMPT


def extract_financial_data(user_input: str) -> dict:

    prompt = f"""
{EXTRACTOR_PROMPT}

User Input:
{user_input}
"""

    response = invoke(prompt)

    try:
        # print("\nRAW RESPONSE:")
        # print(response)
        return json.loads(response)
    except Exception:
        return {
            "error": "invalid_json",
            "raw_response": response
        }