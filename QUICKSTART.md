# 🚀 Quick Start Guide

## How to Run the Season Quiz App

This guide will help you get the quiz application running on your computer in just a few minutes!

### Step 1: Get the Code

1. **Install Git** (if not already installed)
   - Mac: `git --version` (should be pre-installed)
   - If needed: https://git-scm.com/downloads

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Cuthbert20/season_quiz_discovery.git
   cd season_quiz_discovery
   ```

### Step 2: Install UV (Package Manager)

UV is a modern Python package manager that handles dependencies automatically.

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Restart your terminal or run:
source ~/.zshrc
```

### Step 3: Run the Application

First, sync the dependencies to create the environment:
```bash
uv sync
```

Then run the app:
```bash
uv run python app.py
```

You should see something like:
```
 * Running on http://127.0.0.1:5001
 * Debug mode: on
```

### Step 4: Take the Quiz!

Open your web browser and visit: **http://localhost:5001**

## What to Expect

- **7 Random Questions**: Each quiz shows 7 questions selected from 25 total
- **Beautiful Interface**: Colorful design with animations
- **Season Results**: Get assigned Summer ☀️, Fall 🍂, Winter ❄️, or Spring 🌸
- **Share Results**: Share your season personality with friends

## Troubleshooting

**Port already in use?**
The app automatically uses port 5001. If you see an error, try:
```bash
pkill -f "python app.py"  # Stop any existing app
uv run python app.py      # Start fresh
```

**UV command not found?**
Make sure your PATH includes UV:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Questions?

If you have any issues running the app, please reach out! This was designed to be easy to set up and run.

---

**Enjoy the quiz!** 🎉
