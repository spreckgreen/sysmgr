from typer.testing import CliRunner
from sysmgr.cli import app
runner=CliRunner()
def test_version():
    r=runner.invoke(app,["version"])
    assert r.exit_code==0
    assert "0.1.0" in r.stdout
