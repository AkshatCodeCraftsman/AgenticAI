import json

from core.llm import invoke
from prompts.planner_prompt import PLANNER_PROMPT


def create_execution_plan(user_input: str, financial_data: dict) -> dict:

    prompt = f"""
{PLANNER_PROMPT}

User Query:
{user_input}

Financial Data:
{json.dumps(financial_data, indent=4)}
"""

    response = invoke(prompt.strip())

    print("\nRAW RESPONSE:")
    print(response)

    try:
        return json.loads(response)

    except json.JSONDecodeError:
        return {
            "error": "invalid_json",
            "raw_response": response
        }