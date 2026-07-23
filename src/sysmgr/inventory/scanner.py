from .models import Inventory

from . import cpu
from . import memory
from . import osinfo
from . import pci


def collect() -> Inventory:
    return Inventory(
        system=osinfo.collect(),
        cpu=cpu.collect(),
        memory=memory.collect(),
        pci=pci.collect(),
        usb=[],
        network=[],
        bluetooth=[],
        storage=[],
    )
