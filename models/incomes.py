""" Schema definiton for incomes """

from pydantic import Field
from models.commons import DateTimeModelMixin, DocumentIdMixin
from typing import Optional
from decimal import Decimal


class Income(DateTimeModelMixin, DocumentIdMixin):
    """ Income schema definiton """
    ammount: Decimal
    description: Optional[str] = None
