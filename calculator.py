INCOME_SUFFIXES = (
    "_salary",
    "_income",
    "_bonus",
    "_ctc",
    "_package",
)

EXPENSE_SUFFIXES = (
    "_expense",
)

INVESTMENT_SUFFIXES = (
    "_investment",
)


def calculate(financial_data: dict) -> dict:

    monthly_total_income = 0
    annual_total_income = 0

    monthly_total_expenses = 0
    annual_total_expenses = 0

    monthly_total_investments = 0
    annual_total_investments = 0

    for key, value in financial_data.items():

        # Ignore non-numeric values
        if not isinstance(value, (int, float)):
            continue

        # Monthly values
        if key.startswith("monthly_"):

            if key.endswith(INCOME_SUFFIXES):
                monthly_total_income += value

            elif key.endswith(EXPENSE_SUFFIXES):
                monthly_total_expenses += value

            elif key.endswith(INVESTMENT_SUFFIXES):
                monthly_total_investments += value

        # Annual values
        elif key.startswith("annual_"):

            if key.endswith(INCOME_SUFFIXES):
                annual_total_income += value

            elif key.endswith(EXPENSE_SUFFIXES):
                annual_total_expenses += value

            elif key.endswith(INVESTMENT_SUFFIXES):
                annual_total_investments += value

    monthly_remaining_balance = (
        monthly_total_income
        - monthly_total_expenses
        - monthly_total_investments
    )

    return {
        "monthly_total_income": monthly_total_income,
        "annual_total_income": annual_total_income,
        "monthly_total_expenses": monthly_total_expenses,
        "annual_total_expenses": annual_total_expenses,
        "monthly_total_investments": monthly_total_investments,
        "annual_total_investments": annual_total_investments,
        "monthly_remaining_balance": monthly_remaining_balance,
    }