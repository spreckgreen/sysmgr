#!/usr/bin/env bash

echo
echo "Repository"
git rev-parse --show-toplevel

echo
echo "Branch"
git branch --show-current

echo
echo "Git Status"
git status --short

echo
echo "Python"
which python

echo
echo "Pip"
which pip

echo
echo "SysMgr"
which sysmgr

echo
echo "Tests"

pytest -q

echo
echo "Tree"

tree -a -I '.git|.venv|__pycache__|*.egg-info|.pytest_cache'
