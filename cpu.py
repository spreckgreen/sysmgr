import psutil


def collect():
    return {
        "physical": psutil.cpu_count(logical=False),
        "logical": psutil.cpu_count(logical=True),
        "load": psutil.cpu_percent(interval=0.5),
    }
