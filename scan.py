import json

from .inventory.scanner import collect


def collect_system_info():

    data = collect()

    with open("report.json", "w") as fp:
        json.dump(data, fp, indent=4)

    return data
