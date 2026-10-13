import json

from core.llm import invoke
from prompts.Market_prompt import MARKET_AGENT_PROMPT
from services.market_data import get_market_data


def get_market_data_for_query(user_input: str) -> dict:

    prompt = f"""
{MARKET_AGENT_PROMPT}

User Query:
{user_input}
"""

    response = invoke(prompt.strip())

    # print("\nRAW RESPONSE:")
    # print(response)

    try:
        result = json.loads(response)

    except json.JSONDecodeError:
        return {
            "error": "invalid_json",
            "raw_response": response
        }

    asset_type = result.get("asset_type")
    symbols = result.get("symbols", [])

    if asset_type != "stock" or not symbols:
        return {
            "asset_type": asset_type,
            "market_data": {}
        }

    market_data = get_market_data(symbols)

    return {
        "asset_type": asset_type,
        "market_data": market_data
    }