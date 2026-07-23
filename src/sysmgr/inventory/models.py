from __future__ import annotations

from dataclasses import asdict
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Inventory:
    system: dict[str, Any]
    cpu: dict[str, Any]
    memory: dict[str, Any]

    pci: list[Any]
    usb: list[Any]
    network: list[Any]
    bluetooth: list[Any]
    storage: list[Any]

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the entire inventory to JSON-serializable objects.
        """

        return asdict(self)
