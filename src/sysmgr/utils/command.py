"""
Command execution utilities.

Centralized helper for executing external commands safely.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass


@dataclass(slots=True)
class CommandResult:
    success: bool
    stdout: str
    stderr: str
    returncode: int


def run_command(command: list[str], timeout: int = 10) -> CommandResult:
    """
    Execute an external command.

    Parameters
    ----------
    command
        Command and arguments.

    timeout
        Timeout in seconds.

    Returns
    -------
    CommandResult
    """

    executable = shutil.which(command[0])

    if executable is None:
        return CommandResult(
            success=False,
            stdout="",
            stderr=f"{command[0]} not installed",
            returncode=-1,
        )

    try:
        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )

        return CommandResult(
            success=(proc.returncode == 0),
            stdout=proc.stdout,
            stderr=proc.stderr,
            returncode=proc.returncode,
        )

    except subprocess.TimeoutExpired:
        return CommandResult(
            success=False,
            stdout="",
            stderr="command timed out",
            returncode=-2,
        )
