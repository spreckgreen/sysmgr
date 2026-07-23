from .inventory.scanner import collect
from .report.json_export import export


def collect_system_info():
    inventory = collect()

    export(inventory)

    return inventory.to_dict()
