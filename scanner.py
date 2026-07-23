from . import cpu
from . import memory
from . import osinfo


def collect():
    return {
        "system": osinfo.collect(),
        "cpu": cpu.collect(),
        "memory": memory.collect(),
    }
