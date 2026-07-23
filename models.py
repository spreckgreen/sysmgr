from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class Inventory:
    system: dict[str, Any]
    cpu: dict[str, Any]
    memory: dict[str, Any]
    pci: list[dict[str, Any]]
    usb: list[dict[str, Any]]
    network: list[dict[str, Any]]
    bluetooth: list[dict[str, Any]]
    storage: list[dict[str, Any]]

    def to_dict(self):
        return asdict(self)
