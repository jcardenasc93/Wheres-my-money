""" Schema for income entity """

# from models.incomes import Income

def income_schema(income: dict) -> dict:
    income["_id"] = str(income["_id"])
    return income

def incomes_schema(incomes: list[dict]) -> list:
    return [income_schema(income) for income in incomes]

