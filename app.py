"""
Season Quiz Application - Flask Backend
A fun quiz app that assigns seasons based on personality traits.
"""

import secrets
import random

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
# Secret key for session management
# RYKER LEARNING: Here is where we create the lock for our session data. Like a backback of data that the user carries with them as they navigate the app.
# You can view the signed/encrypted data in the chrome dev-tools (remember when showing teacher: F12, application, cookies, localhost)
app.secret_key = secrets.token_hex(16)

# Quiz questions with options that map to seasons
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What's your favorite type of weather?",
        "options": [
            {"text": "Sunny and warm! ☀️", "season": "summer"},
            {"text": "Cool and crisp 🍂", "season": "fall"},
            {"text": "Snowy and magical ❄️", "season": "winter"},
            {"text": "Fresh and blooming 🌸", "season": "spring"},
        ],
    },
    {
        "id": 2,
        "question": "Which activity sounds the most fun?",
        "options": [
            {"text": "Swimming at the beach 🏖️", "season": "summer"},
            {"text": "Jumping in leaf piles 🍁", "season": "fall"},
            {"text": "Building a snowman ⛄", "season": "winter"},
            {"text": "Planting flowers 🌺", "season": "spring"},
        ],
    },
    {
        "id": 3,
        "question": "Pick your favorite color palette:",
        "options": [
            {"text": "Bright yellows and ocean blues 🌞", "season": "summer"},
            {"text": "Orange, red, and deep browns 🧡", "season": "fall"},
            {"text": "White, silver, and icy blues ❄️", "season": "winter"},
            {"text": "Pastels and soft greens 💐", "season": "spring"},
        ],
    },
    {
        "id": 4,
        "question": "What's your ideal drink?",
        "options": [
            {"text": "Ice-cold lemonade 🍋", "season": "summer"},
            {"text": "Pumpkin spice latte 🎃", "season": "fall"},
            {"text": "Hot chocolate with marshmallows ☕", "season": "winter"},
            {"text": "Fresh fruit smoothie 🍓", "season": "spring"},
        ],
    },
    {
        "id": 5,
        "question": "Which vibe describes you best?",
        "options": [
            {"text": "Adventure mode activated! 🌊", "season": "summer"},
            {"text": "Thoughtful and reflective 🍂", "season": "fall"},
            {"text": "Cozy introvert energy 🧣", "season": "winter"},
            {"text": "Ready for new beginnings 🌱", "season": "spring"},
        ],
    },
    {
        "id": 6,
        "question": "Which outfit are you most likely to wear?",
        "options": [
            {"text": "Shorts and a graphic tee 😎", "season": "summer"},
            {"text": "Flannel + jeans 🍁", "season": "fall"},
            {"text": "Hoodie + fuzzy socks ❄️", "season": "winter"},
            {"text": "Light jacket + bright colors 🌸", "season": "spring"},
        ],
    },
    {
        "id": 7,
        "question": "Choose a school vibe:",
        "options": [
            {"text": "Recess all day, please ☀️", "season": "summer"},
            {"text": "Reading under a tree 🍂", "season": "fall"},
            {"text": "Snow day energy ❄️", "season": "winter"},
            {"text": "Field trip season 🌼", "season": "spring"},
        ],
    },
    {
        "id": 8,
        "question": "Pick a perfect weekend plan:",
        "options": [
            {"text": "Pool party with friends 🏊‍♂️", "season": "summer"},
            {"text": "Corn maze + apple cider 🍎", "season": "fall"},
            {"text": "Movie marathon in blankets 🎬", "season": "winter"},
            {"text": "Picnic in the park 🌿", "season": "spring"},
        ],
    },
    {
        "id": 9,
        "question": "Which snack do you pick first?",
        "options": [
            {"text": "Popsicles! 🍧", "season": "summer"},
            {"text": "Caramel apples 🍏", "season": "fall"},
            {"text": "Warm cookies fresh from the oven 🍪", "season": "winter"},
            {"text": "Fruit cups or berries 🍇", "season": "spring"},
        ],
    },
    {
        "id": 10,
        "question": "What’s your main-character moment?",
        "options": [
            {"text": "Walking into school with summer glow 😎", "season": "summer"},
            {"text": "Crunching leaves dramatically 🍂", "season": "fall"},
            {"text": "Breathing dragon air in cold weather 😤❄️", "season": "winter"},
            {"text": "Dancing in spring rain 🌧️💐", "season": "spring"},
        ],
    },
    {
        "id": 11,
        "question": "Which pet matches your vibe?",
        "options": [
            {"text": "A playful golden retriever 🐶", "season": "summer"},
            {"text": "A wise old cat 🐱", "season": "fall"},
            {"text": "A cuddly bunny 🐰", "season": "winter"},
            {"text": "A hyper baby goat 🐐", "season": "spring"},
        ],
    },
    {
        "id": 12,
        "question": "Which holiday energy matches you best?",
        "options": [
            {"text": "Fourth of July fireworks 🎆", "season": "summer"},
            {"text": "Halloween chaos 🎃👻", "season": "fall"},
            {"text": "Winter holidays + hot cocoa 🎄", "season": "winter"},
            {"text": "Easter eggs and sunshine 🐣🌷", "season": "spring"},
        ],
    },
    {
        "id": 13,
        "question": "Pick a soundtrack:",
        "options": [
            {"text": "Beach party playlist 🎵", "season": "summer"},
            {"text": "Calm indie-school vibes 🍁🎧", "season": "fall"},
            {"text": "Lo-fi beats in a blanket fort ❄️🎶", "season": "winter"},
            {"text": "Upbeat spring-cleaning songs 🌱🎵", "season": "spring"},
        ],
    },
    {
        "id": 14,
        "question": "Your energy in the morning:",
        "options": [
            {"text": "Ready to go!! 😤🔥", "season": "summer"},
            {"text": "Give me 5 minutes… or 10 🍂😴", "season": "fall"},
            {"text": "Absolutely not. ☕❄️", "season": "winter"},
            {"text": "Optimistic and fresh 🌸✨", "season": "spring"},
        ],
    },
    {
        "id": 15,
        "question": "Which meme energy do you match?",
        "options": [
            {"text": "‘I’m just built like that’ summer confidence 💪😎", "season": "summer"},
            {"text": "Fall aesthetic influencer 📸🍂", "season": "fall"},
            {"text": "Winter goblin mode 🧌❄️", "season": "winter"},
            {"text": "Spring glow-up arc 🌱✨", "season": "spring"},
        ],
    },
    {
        "id": 16,
        "question": "Pick a classroom seat:",
        "options": [
            {"text": "By the window with sunshine ☀️", "season": "summer"},
            {"text": "Middle row — cozy but focused 🍂", "season": "fall"},
            {"text": "Back corner, hoodie up 😶‍🌫️❄️", "season": "winter"},
            {"text": "Front row ready for a fresh start 🌸", "season": "spring"},
        ],
    },
    {
        "id": 17,
        "question": "Which sound is most satisfying?",
        "options": [
            {"text": "Waves crashing 🌊", "season": "summer"},
            {"text": "Leaves crunching 🍁", "season": "fall"},
            {"text": "Snow crunching under boots ❄️", "season": "winter"},
            {"text": "Birds chirping 🌼", "season": "spring"},
        ],
    },
    {
        "id": 18,
        "question": "Choose a hairstyle moment:",
        "options": [
            {"text": "Messy beach hair 🏖️", "season": "summer"},
            {"text": "The perfect ‘seven fade’ 🍂✂️", "season": "fall"},
            {"text": "Beanie hair don’t care ❄️", "season": "winter"},
            {"text": "Fresh, fluffy spring hair 🌸", "season": "spring"},
        ],
    },
    {
        "id": 19,
        "question": "Pick a magical creature:",
        "options": [
            {"text": "Mermaid 🧜‍♀️", "season": "summer"},
            {"text": "Forest elf 🍂🧝", "season": "fall"},
            {"text": "Ice dragon ❄️🐉", "season": "winter"},
            {"text": "Flower fairy 🌺🧚", "season": "spring"},
        ],
    },
    {
        "id": 20,
        "question": "Your ideal after-school vibe:",
        "options": [
            {"text": "Hanging out outdoors ☀️", "season": "summer"},
            {"text": "Reading or drawing 🍁", "season": "fall"},
            {"text": "Gaming wrapped in a blanket 🎮❄️", "season": "winter"},
            {"text": "Exploring or bike riding 🚲🌱", "season": "spring"},
        ],
    },
    {
        "id": 21,
        "question": "How would friends describe you?",
        "options": [
            {"text": "Energetic and social 😎", "season": "summer"},
            {"text": "Creative and thoughtful ✏️🍂", "season": "fall"},
            {"text": "Calm and comforting ❄️", "season": "winter"},
            {"text": "Optimistic and cheerful 🌼", "season": "spring"},
        ],
    },
    {
        "id": 22,
        "question": "Pick a dream vacation:",
        "options": [
            {"text": "Hawaii beaches 🏝️", "season": "summer"},
            {"text": "Cabin in the woods 🍂🏕️", "season": "fall"},
            {"text": "Cozy ski lodge ❄️⛷️", "season": "winter"},
            {"text": "Flower-filled countryside 🌸", "season": "spring"},
        ],
    },
    {
        "id": 23,
        "question": "Choose a sport or hobby:",
        "options": [
            {"text": "Surfing or swimming 🌊", "season": "summer"},
            {"text": "Hiking or photography 🍁📸", "season": "fall"},
            {"text": "Ice skating or reading indoors ❄️", "season": "winter"},
            {"text": "Gardening or art 🌷", "season": "spring"},
        ],
    },
    {
        "id": 24,
        "question": "Pick your mood of the day:",
        "options": [
            {"text": "Hyped and sunny ☀️😤", "season": "summer"},
            {"text": "Cozy with deep thoughts 🍁🧠", "season": "fall"},
            {"text": "Sleepy but sweet 😴❄️", "season": "winter"},
            {"text": "Fresh start energy 🌱✨", "season": "spring"},
        ],
    },
    {
        "id": 25,
        "question": "Which decoration aesthetic do you love?",
        "options": [
            {"text": "Beachy shells and bright colors 🐚☀️", "season": "summer"},
            {"text": "Pumpkins, lanterns, and warm lights 🍂🕯️", "season": "fall"},
            {"text": "Fairy lights and snowflakes ✨❄️", "season": "winter"},
            {"text": "Plants, vines, and pastel colors 🌿🌸", "season": "spring"},
        ],
    },
]

# Season descriptions with emojis and characteristics
SEASON_INFO = {
    "summer": {
        "name": "Summer",
        "emoji": "☀️",
        "color": "#FFD700",
        "description": "You're bright, energetic, and full of life! Like summer, you bring warmth and joy to everyone around you. You love adventure and making the most of every moment!",
        "traits": [
            "Energetic and adventurous",
            "Loves being outdoors",
            "Optimistic and cheerful",
            "Social and outgoing",
        ],
    },
    "fall": {
        "name": "Fall",
        "emoji": "🍂",
        "color": "#FF8C42",
        "description": "You're thoughtful, creative, and love cozy moments! Like fall, you appreciate change and find beauty in transitions. You're warm, comforting, and reflective.",
        "traits": [
            "Thoughtful and introspective",
            "Appreciates comfort and warmth",
            "Creative and artistic",
            "Values deep connections",
        ],
    },
    "winter": {
        "name": "Winter",
        "emoji": "❄️",
        "color": "#4A90E2",
        "description": "You're calm, peaceful, and magical! Like winter, you bring serenity and wonder. You appreciate quiet moments and have a unique, cool perspective on life.",
        "traits": [
            "Calm and peaceful",
            "Loves quiet reflection",
            "Unique and individual",
            "Enjoys cozy indoor activities",
        ],
    },
    "spring": {
        "name": "Spring",
        "emoji": "🌸",
        "color": "#98D8C8",
        "description": "You're fresh, optimistic, and full of growth! Like spring, you represent new beginnings and endless possibilities. You're nurturing, positive, and always blooming!",
        "traits": [
            "Optimistic and hopeful",
            "Loves growth and learning",
            "Nurturing and kind",
            "Embraces new experiences",
        ],
    },
}


@app.route("/")
def index():
    """Landing page for the quiz application."""
    session.clear()  # Clear any previous quiz data
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    """Select 7 random questions from the quiz & display them."""
    random_questions = random.sample(QUIZ_QUESTIONS, k=7)
    
    # Shuffle the options for each question
    for question in random_questions:
        random.shuffle(question["options"])
    
    session["quiz_questions"] = random_questions
    return render_template("quiz.html", questions=random_questions)


@app.route("/submit", methods=["POST"])
def submit():
    """Process quiz answers and calculate the season result."""
    # Count votes for each season
    season_votes = {"summer": 0, "fall": 0, "winter": 0, "spring": 0}
    
    # DEBUG: Print what we received from the form
    print("=== DEBUG: Form Data Received ===")
    print(f"All form data: {dict(request.form)}")
    
    questions_asked = session.get("quiz_questions")
    print(f"=== DEBUG: Questions in Session ===")
    print(f"Number of questions: {len(questions_asked) if questions_asked else 0}")
    if questions_asked:
        for q in questions_asked:
            print(f"  - Question ID: {q['id']}, Text: {q['question'][:50]}...")
    
    if not questions_asked:
        # Handling empty session, we redirect to the start of the quiz.
        return redirect(url_for("index"))
    # Process each answer based on the questions stored in the session
    for question in questions_asked:
        answer_key = f"question_{question['id']}"
        selected_option = request.form.get(answer_key)

        if selected_option:
            try:
                option_index = int(selected_option)
                if 0 <= option_index < len(question["options"]):
                    season = question["options"][option_index]["season"]
                    season_votes[season] += 1
            except (ValueError, IndexError):
                pass

    # Find the season with the most votes
    result_season = max(season_votes, key=season_votes.get)

    # Store in session
    session["result_season"] = result_season
    session["votes"] = season_votes

    return render_template(
        "result.html", season=result_season, season_info=SEASON_INFO[result_season]
    )


@app.route("/restart")
def restart():
    """Restart the quiz."""
    session.clear()
    return render_template("index.html")

@app.route("/crash")
def crash():
    # This will cause a ZeroDivisionError
    # Using so as to triger the debugger.
    return 1 / 0


if __name__ == "__main__":
    # Run the Flask development server
    app.run(debug=True, host="0.0.0.0", port=5001)
