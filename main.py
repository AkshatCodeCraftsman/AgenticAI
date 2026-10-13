from services.extractor import extract_financial_data
from services.calculator import calculate

from agents.planner_agent import create_execution_plan
from agents.market_agent import get_market_data_for_query
from agents.savings_agent import get_savings_analysis
from agents.investment_agent import get_investment_analysis
from agents.report_agent import generate_report


def main():

    while True:

        user_input = input("\nEnter query (type 'exit' to quit): ").strip()

        if user_input.lower() == "exit":
            break

        #  Extract Financial Data
        financial_data = extract_financial_data(user_input)

        #  Create Execution Plan
        plan = create_execution_plan(user_input, financial_data)

        execution_plan = plan.get("execution_plan", [])

        calculated_data = {}
        savings_analysis = ""
        investment_analysis = ""
        market_data = {}

        #  Calculator
        if "calculator" in execution_plan:

            calculated_data = calculate(financial_data)

        #  Market Agent
        if "market_agent" in execution_plan:

            result = get_market_data_for_query(user_input)

            market_data = result.get("market_data", {})

        #  Savings Agent
        if "savings_agent" in execution_plan:

            savings_analysis = get_savings_analysis(
                user_input,
                financial_data,
                calculated_data
            )

        #  Investment Agent
        if "investment_agent" in execution_plan:

            investment_analysis = get_investment_analysis(
                user_input,
                financial_data,
                calculated_data,
                market_data
            )

        #  Report Agent
        final_response = generate_report(
            user_input,
            financial_data,
            calculated_data,
            savings_analysis,
            investment_analysis
        )

        print("\n" + "=" * 80)
        print("FINAL RESPONSE\n")
        print(final_response)
        print("=" * 80)


if __name__ == "__main__":
    main()