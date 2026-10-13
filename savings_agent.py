import json

from core.llm import invoke
from prompts.Savings_prompt import SAVINGS_PROMPT


def get_savings_analysis(
    user_input: str,
    financial_data: dict,
    calculated_data: dict,
) -> str:

    prompt = f"""
{SAVINGS_PROMPT}

User Query:
{user_input}

Financial Data:
{json.dumps(financial_data, indent=4)}

Calculated Data:
{json.dumps(calculated_data, indent=4)}
"""

    response = invoke(prompt)

    # print("\nRAW RESPONSE:")
    # print(response)

    return response