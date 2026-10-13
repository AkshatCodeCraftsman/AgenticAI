import json

from core.llm import invoke
from prompts.Investement_prompt import INVESTMENT_PROMPT


def get_investment_analysis(
    user_input: str,
    financial_data: dict,
    calculated_data: dict,
    market_data: dict | None = None
) -> str:

    prompt = f"""
{INVESTMENT_PROMPT}

User Query:
{user_input}

Financial Data:
{json.dumps(financial_data, indent=4)}

Calculated Data:
{json.dumps(calculated_data, indent=4)}
"""

    if market_data is not None:
        prompt += f"""

Market Data:
{json.dumps(market_data, indent=4)}
"""

    response = invoke(prompt.strip())

    # print("\nRAW RESPONSE:\n")
    # print(response)

    return response