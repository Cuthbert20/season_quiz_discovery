# 🌈 Season Personality Quiz

A fun and interactive quiz application that assigns you a season based on your personality! Built with Python, Flask, and lots of colorful design.

## ✨ Features

- **5 Fun Questions**: Answer personality-based questions with emoji-filled options
- **Season Assignment**: Get assigned to Summer ☀️, Fall 🍂, Winter ❄️, or Spring 🌸
- **Beautiful UI**: Colorful gradients, animations, and responsive design
- **Confetti Celebration**: Animated confetti on the results page!
- **Share Results**: Share your season with friends and family

## 🛠️ Tech Stack

- **Python 3.10+**: Programming language
- **Flask**: Web framework
- **UV**: Modern Python package manager
- **Ruff**: Lightning-fast Python linter and formatter
- **HTML/CSS/JavaScript**: Frontend with animations

## 📁 Project Structure

```
quiz_app/
├── app.py                 # Flask application with quiz logic
├── static/
│   └── style.css         # Colorful CSS styling with animations
├── templates/
│   ├── index.html        # Landing page
│   ├── quiz.html         # Quiz questions page
│   └── result.html       # Results page with confetti
├── pyproject.toml        # UV project configuration
├── .python-version       # Python version specification
├── .gitignore           # Git ignore file
└── README.md            # This file!
```

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.10 or higher
- [UV](https://docs.astral.sh/uv/) - Python package manager

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd quiz_app
   ```

2. **Install dependencies using UV**:
   ```bash
   uv sync
   ```
   
   This will create a virtual environment and install Flask automatically.

### Running the Application

1. **Start the Flask development server**:
   ```bash
   uv run python app.py
   ```

2. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

3. **Take the quiz** and discover your season! 🎉

## 🧹 Code Quality

### Using Ruff

This project uses Ruff for linting and formatting. Ruff is configured in `pyproject.toml`.

**Check code quality**:
```bash
uv run ruff check .
```

**Auto-fix issues**:
```bash
uv run ruff check --fix .
```

**Format code**:
```bash
uv run ruff format .
```

## 📝 How It Works

1. **Welcome Page**: Users are greeted with an animated welcome page featuring all four season emojis
2. **Quiz Questions**: Users answer 5 personality-based questions
3. **Season Calculation**: The app counts which season received the most votes from the answers
4. **Results**: Users see their assigned season with:
   - A description of their personality
   - Key traits that match the season
   - Animated confetti celebration!
   - Option to share results or retake the quiz

## 🎨 Customization

### Adding More Questions

Edit the `QUIZ_QUESTIONS` list in `app.py`:

```python
QUIZ_QUESTIONS = [
    {
        "id": 6,  # Increment the ID
        "question": "Your new question here?",
        "options": [
            {"text": "Option 1 🎈", "season": "summer"},
            {"text": "Option 2 🍁", "season": "fall"},
            {"text": "Option 3 ⛄", "season": "winter"},
            {"text": "Option 4 🌻", "season": "spring"},
        ],
    },
    # ... existing questions
]
```

### Modifying Season Descriptions

Update the `SEASON_INFO` dictionary in `app.py` to change descriptions, traits, or colors.

### Styling Changes

Edit `static/style.css` to customize:
- Colors and gradients
- Animations
- Font sizes
- Responsive breakpoints

## 🔮 Future Features (Coming Soon!)

- [ ] Google ADK agent integration
- [ ] Dynamic follow-up questions based on answers
- [ ] Save results to database
- [ ] User accounts and quiz history
- [ ] Social media sharing with images
- [ ] Multiple quiz types
- [ ] Multi-language support

## 🎓 Learning Objectives

This project is perfect for learning:
- Flask web application basics
- HTML templating with Jinja2
- CSS animations and gradients
- Form handling and validation
- Modern Python tooling (UV, Ruff)
- Project structure and organization

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Improve the design
- Fix bugs
- Add more questions

## 📄 License

This project is created for educational purposes. Feel free to use and modify it!

## 🎉 Credits

Made with ❤️ as a fun programming learning project!

---

**Happy Quizzing!** 🌈✨
