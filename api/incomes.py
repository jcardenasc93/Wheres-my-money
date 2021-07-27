""" Definition of the API routes """

from fastapi import APIRouter, Body, Path, Query
from typing import Optional

from models.commons import AppObjectId
from models.incomes import Income
from db.crud import CRUDManager

from schemas.incomes import incomes_schema, income_schema

PREFIX = "/incomes"
COLLECTION = "income"
incomes_router = APIRouter(prefix=PREFIX)


@incomes_router.get("")
async def get_incomes(income_id: Optional[str] = None):
    """
    Retrieve incomes from DB

    Args:
        income_id (AppObjectId): Unique db identifier of the income
    """
    if income_id:
        query = {"_id": AppObjectId.validate(income_id)}
        income = await CRUDManager.find_one(collection=COLLECTION,
                                            model=Income,
                                            query=query)
        return income_schema(income)
    incomes = await CRUDManager.find_all(collection=COLLECTION, model=Income)
    return incomes_schema(incomes)


@incomes_router.post("")
async def create_income():
    """
    Inserte new income in the DB
    """
    return "Create new income"


@incomes_router.put("/{income_id}")
async def update_income(income_id: str):
    """
    Updates specified income
    """
    AppObjectId.validate(income_id)
    return f"Updates {income_id}"


@incomes_router.delete("/{income_id}")
async def delete_income(income_id: str):
    """
    Deletes specified income
    """
    AppObjectId.validate(income_id)
    return f"Deletes {income_id}"
