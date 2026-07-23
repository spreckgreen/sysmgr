#!/usr/bin/env bash

###############################################################################
# SysMgr Development Shell
###############################################################################

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$PROJECT_ROOT" || exit 1

if [ ! -d ".venv" ]; then
    echo "Virtual environment not found."
    echo
    echo "Run:"
    echo "    ./bootstrap.sh"
    exit 1
fi

source .venv/bin/activate

hash -r

clear

echo "========================================================="
echo "                 SysMgr Development Shell"
echo "========================================================="
echo

echo "Repository : $(pwd)"
echo "Branch     : $(git branch --show-current)"
echo "Python     : $(which python)"
echo "Pip        : $(which pip)"
echo "SysMgr     : $(which sysmgr)"
echo

echo "Useful commands"
echo "---------------"
echo "make test"
echo "make run"
echo "make lint"
echo "pytest"
echo

exec bash
