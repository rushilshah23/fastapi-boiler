#!/bin/bash
# git-init.sh
# Usage: ./git-init.sh
# This script reinitializes the current folder as a new git repository
# while keeping submodules intact and safe for development.

set -e  # exit on error

echo "➡️  Starting Git initialization for a new independent repo..."

# 1️⃣ Remove old Git metadata
if [ -d ".git" ]; then
    echo "Removing existing .git folder..."
    rm -rf .git
fi

# 2️⃣ Initialize new git repo
echo "Initializing new Git repository..."
git init

# 3️⃣ Ensure current directory is safe
echo "Marking directory as safe for Git..."
git config --global --add safe.directory "$(pwd)"


# 4 Initialize submodules
if [ -f ".gitmodules" ]; then
    echo "Initializing submodules..."
    git submodule init
    git submodule update --init --recursive
else
    echo "No submodules found."
fi

echo "✅ Git initialization completed successfully!"
