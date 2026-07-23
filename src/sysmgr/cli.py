import json
import typer
from rich.console import Console
from . import __version__
from .scan import collect_system_info

app = typer.Typer()
console = Console()


@app.command()
def version():
    console.print(f"SysMgr {__version__}")


@app.command()
def scan(output: str = "report.json"):
    data = collect_system_info()
    console.print(data)
    with open(output, "w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    app()
