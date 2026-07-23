from .models import Inventory
from . import cpu
from . import memory
from . import osinfo


def collect() -> Inventory:

    return Inventory(
        system=osinfo.collect(),
        cpu=cpu.collect(),
        memory=memory.collect(),
        pci=[],
        usb=[],
        network=[],
        bluetooth=[],
        storage=[],
    )
