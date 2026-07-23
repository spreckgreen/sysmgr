#!/usr/bin/env bash
#
# SysMgr Bootstrap
#

set -e

echo "======================================="
echo " SysMgr Bootstrap"
echo "======================================="

if ! command -v python3 >/dev/null; then
    echo "Python 3 not found."
    exit 1
fi

echo "Python Version:"
python3 --version

if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

echo "Upgrading packaging tools..."

python -m pip install --upgrade \
    pip \
    setuptools \
    wheel

echo "Installing project..."

pip install -e .

echo
echo "Bootstrap complete."

echo
echo "Try:"
echo
echo "    sysmgr version"
echo "    sysmgr scan"
