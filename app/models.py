from dataclasses import dataclass
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"


@dataclass
class Order:
    id: str
    total_cents: int
    status: OrderStatus = OrderStatus.PENDING
