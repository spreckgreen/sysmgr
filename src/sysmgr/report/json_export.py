import json
from pathlib import Path

from sysmgr.inventory.models import Inventory


def export(inv: Inventory, filename: str = "report.json") -> None:
    Path(filename).write_text(
        json.dumps(inv.to_dict(), indent=4),
        encoding="utf-8",
    )
