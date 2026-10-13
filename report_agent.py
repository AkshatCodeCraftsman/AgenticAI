import json

from core.llm import invoke
from prompts.report_prompt import REPORT_PROMPT


def generate_report(
    user_input: str,
    financial_data: dict,
    calculated_data: dict,
    savings_analysis: str = "",
    investment_analysis: str = "",
) -> str:

    prompt = f"""
{REPORT_PROMPT}

User Query:
{user_input}

Financial Data:
{json.dumps(financial_data, indent=4)}

Calculated Data:
{json.dumps(calculated_data, indent=4)}

Savings Analysis:
{savings_analysis}

Investment Analysis:
{investment_analysis}
"""

    response = invoke(prompt.strip())

    # print("\nRAW RESPONSE:")
    # print(response)

    return response