import platform,socket,psutil
def collect_system_info():
    return {
      "hostname":socket.gethostname(),
      "os":platform.system(),
      "kernel":platform.release(),
      "cpu_logical":psutil.cpu_count(),
      "memory_gb":round(psutil.virtual_memory().total/1024**3,2),
    }
