"""
PCI Device Discovery

Collects PCI device information using lspci.

Author: R Premo
"""

from __future__ import annotations

from dataclasses import dataclass
from subprocess import CalledProcessError
from subprocess import run


@dataclass(slots=True)
class PCIDevice:
    slot: str
    device_class: str
    vendor: str
    device: str


def _parse_line(line: str) -> PCIDevice | None:
    """
    Parse one line of lspci output.

    Example:

    01:00.0 Network controller: Qualcomm Atheros AR9462 Wireless Network Adapter
    """

    if ":" not in line:
        return None

    try:
        slot, remainder = line.split(" ", 1)

        device_class, description = remainder.split(":", 1)

        description = description.strip()

        parts = description.split()

        vendor = "Unknown"

        device = description

        #
        # Handle common vendors
        #

        if description.startswith("Intel"):
            vendor = "Intel"
            device = description[len("Intel") :].strip()

        elif description.startswith("Realtek"):
            vendor = "Realtek"
            device = description[len("Realtek") :].strip()

        elif description.startswith("Qualcomm Atheros"):
            vendor = "Qualcomm Atheros"
            device = description[len("Qualcomm Atheros") :].strip()

        elif description.startswith("Advanced Micro Devices"):
            vendor = "AMD"
            device = description

        elif len(parts) > 1:
            vendor = parts[0]
            device = " ".join(parts[1:])

        return PCIDevice(
            slot=slot,
            device_class=device_class.strip(),
            vendor=vendor,
            device=device.strip(),
        )

    except Exception:
        return None


def collect() -> list[PCIDevice]:
    """
    Collect PCI devices.

    Returns
    -------
    list[PCIDevice]
    """

    try:
        result = run(
            ["lspci"],
            capture_output=True,
            text=True,
            check=True,
        )

    except (FileNotFoundError, CalledProcessError):
        return []

    devices: list[PCIDevice] = []

    for line in result.stdout.splitlines():
        parsed = _parse_line(line)

        if parsed:
            devices.append(parsed)

    return devices
