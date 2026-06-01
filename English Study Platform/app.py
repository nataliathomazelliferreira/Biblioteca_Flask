from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "english-study-platform-secret-key"

ACTIVITY_ORDER = ["grammar", "reading", "listening", "speaking", "quiz"]


def get_progress(activity_type):
    index = ACTIVITY_ORDER.index(activity_type) + 1
    return int((index / len(ACTIVITY_ORDER)) * 100)


LEVELS = {
    "iniciante": {
        "label": "Iniciante",
        "language": "pt",
        "activities": {
            "grammar": {
                "title": "Grammar",
                "instruction": "Complete as frases com a alternativa correta.",
                "questions": [
                    {
                        "question": "She ___ to the mall yesterday.",
                        "tip": "Dica: passado do verbo go.",
                        "options": ["go", "goes", "went", "going"],
                        "answer": "went"
                    },
                    {
                        "question": "I ___ happy today.",
                        "tip": "Dica: verbo to be com I.",
                        "options": ["am", "is", "are", "be"],
                        "answer": "am"
                    },
                    {
                        "question": "They ___ students.",
                        "tip": "Dica: verbo to be com they.",
                        "options": ["am", "is", "are", "was"],
                        "answer": "are"
                    }
                ]
            },
            "reading": {
                "title": "Reading",
                "instruction": "Leia o texto e responda às perguntas.",
                "text": """Anna is a student. She studies English every morning.
She likes music and movies.
On weekends, she visits her friends.
Anna wants to travel to Canada one day.
She is practicing English to speak better.""",
                "questions": [
                    {
                        "question": "What does Anna study?",
                        "options": ["English", "Math", "Science", "History"],
                        "answer": "English"
                    },
                    {
                        "question": "When does Anna study?",
                        "options": ["Every morning", "Every night", "Only Sunday", "Never"],
                        "answer": "Every morning"
                    },
                    {
                        "question": "Where does Anna want to travel?",
                        "options": ["Canada", "Brazil", "Japan", "France"],
                        "answer": "Canada"
                    }
                ]
            },
            "listening": {
                "title": "Listening",
                "instruction": "Assista ao vídeo e responda às perguntas.",
                "youtube_url": "https://www.youtube.com/embed/MfW9rkoDABg",
                "questions": [
                    {
                        "question": "Where is Todd from?",
                        "options": ["San Francisco", "Los Angeles", "Glasgow", "New York"],
                        "answer": "San Francisco"
                    },
                    {
                        "question": "What is Todd's job?",
                        "options": ["Teacher", "Doctor", "Engineer", "Manager"],
                        "answer": "Teacher"
                    },
                    {
                        "question": "How old is Todd?",
                        "options": ["34", "47", "52", "40"],
                        "answer": "47"
                    }
                ]
            },
            "speaking": {
                "title": "Speaking",
                "instruction": "Leia as frases em voz alta e pratique sua pronúncia.",
                "sentences": [
                    "Leia esta frase em voz alta: My name is Anna.",
                    "Repita a frase: I am learning English.",
                    "Responda falando: What is your favorite food?"
                ]
            }
        }
    },

    "basico": {
        "label": "Básico",
        "language": "pt",
        "activities": {
            "grammar": {
                "title": "Grammar",
                "instruction": "Complete as frases com a alternativa correta.",
                "questions": [
                    {
                        "question": "They ___ soccer every Saturday.",
                        "tip": "Dica: verbo play no presente.",
                        "options": ["plays", "play", "played", "playing"],
                        "answer": "play"
                    },
                    {
                        "question": "He ___ coffee every morning.",
                        "tip": "Dica: he/she/it no presente.",
                        "options": ["drink", "drinks", "drank", "drinking"],
                        "answer": "drinks"
                    },
                    {
                        "question": "We ___ English at school.",
                        "tip": "Dica: verbo study no presente.",
                        "options": ["study", "studies", "studied", "studying"],
                        "answer": "study"
                    }
                ]
            },
            "reading": {
                "title": "Reading",
                "instruction": "Leia o texto e responda às perguntas.",
                "text": """Tom works in a bookstore.
He likes helping people find books.
Every day, he talks to many customers.
At night, Tom reads stories in English.
He believes reading helps him learn new words.""",
                "questions": [
                    {
                        "question": "Where does Tom work?",
                        "options": ["At a bookstore", "At a hospital", "At a restaurant", "At a school"],
                        "answer": "At a bookstore"
                    },
                    {
                        "question": "What does Tom read at night?",
                        "options": ["Stories in English", "Math books", "Newspapers", "Comics in Spanish"],
                        "answer": "Stories in English"
                    },
                    {
                        "question": "Why does Tom read?",
                        "options": ["To learn new words", "To sleep", "To cook", "To play"],
                        "answer": "To learn new words"
                    }
                ]
            },
            "listening": {
                "title": "Listening",
                "instruction": "Assista ao vídeo e responda às perguntas.",
                "youtube_url": "https://www.youtube.com/embed/MfW9rkoDABg",
                "questions": [
                    {
                        "question": "Where is Todd's mother from?",
                        "options": ["Los Angeles", "Glasgow", "San Francisco", "Chicago"],
                        "answer": "Los Angeles"
                    },
                    {
                        "question": "What does Todd's mother do?",
                        "options": ["Teacher", "Manager", "Nurse", "Doctor"],
                        "answer": "Manager"
                    },
                    {
                        "question": "What does Todd's father do?",
                        "options": ["Teacher", "Pilot", "Manager", "Engineer"],
                        "answer": "Manager"
                    }
                ]
            },
            "speaking": {
                "title": "Speaking",
                "instruction": "Leia as frases em voz alta e responda oralmente.",
                "sentences": [
                    "Leia em voz alta: I usually study at night.",
                    "Repita com atenção: English is important for communication.",
                    "Responda falando: What do you do every morning?"
                ]
            }
        }
    },

    "intermediario": {
        "label": "Intermediate",
        "language": "en",
        "activities": {
            "grammar": {
                "title": "Grammar",
                "instruction": "Complete the sentences with the correct option.",
                "questions": [
                    {
                        "question": "If I ___ more time, I would study another language.",
                        "tip": "Tip: use the correct past form of have.",
                        "options": ["have", "has", "had", "having"],
                        "answer": "had"
                    },
                    {
                        "question": "She has ___ finished her homework.",
                        "tip": "Tip: use present perfect.",
                        "options": ["already", "yesterday", "tomorrow", "last week"],
                        "answer": "already"
                    },
                    {
                        "question": "I have lived here ___ 2020.",
                        "tip": "Tip: use since or for.",
                        "options": ["for", "since", "during", "at"],
                        "answer": "since"
                    }
                ]
            },
            "reading": {
                "title": "Reading",
                "instruction": "Read the text and answer the questions.",
                "text": """Learning English can open many opportunities.
People use English for travel, work, science, and entertainment.
However, learning a language requires practice and patience.
Students improve faster when they study a little every day.
Consistency is more important than perfection.""",
                "questions": [
                    {
                        "question": "What can English open?",
                        "options": ["Opportunities", "Doors only", "Cars", "Games"],
                        "answer": "Opportunities"
                    },
                    {
                        "question": "What does learning a language require?",
                        "options": ["Practice and patience", "Only luck", "No effort", "Silence"],
                        "answer": "Practice and patience"
                    },
                    {
                        "question": "What is more important than perfection?",
                        "options": ["Consistency", "Speed", "Translation", "Grammar only"],
                        "answer": "Consistency"
                    }
                ]
            },
            "listening": {
                "title": "Listening",
                "instruction": "Watch the video and answer the questions.",
                "youtube_url": "https://www.youtube.com/embed/MfW9rkoDABg",
                "questions": [
                    {
                        "question": "Where is Aimee from?",
                        "options": ["England", "Glasgow", "London", "California"],
                        "answer": "Glasgow"
                    },
                    {
                        "question": "How old is Aimee?",
                        "options": ["34", "47", "29", "40"],
                        "answer": "34"
                    },
                    {
                        "question": "What was Aimee's mother before retirement?",
                        "options": ["Teacher", "Manager", "Doctor", "Nurse"],
                        "answer": "Nurse"
                    }
                ]
            },
            "speaking": {
                "title": "Speaking",
                "instruction": "Practice speaking aloud.",
                "sentences": [
                    "Read this sentence aloud: I have been studying English for two years.",
                    "Repeat the sentence and focus on pronunciation.",
                    "Answer speaking: Why do you want to improve your English?"
                ]
            }
        }
    },

    "avancado": {
        "label": "Advanced",
        "language": "en",
        "activities": {
            "grammar": {
                "title": "Grammar",
                "instruction": "Choose the best option to complete the sentences.",
                "questions": [
                    {
                        "question": "By the time we arrived, the lecture ___ already started.",
                        "tip": "Tip: use past perfect.",
                        "options": ["has", "had", "was", "is"],
                        "answer": "had"
                    },
                    {
                        "question": "Had I known about the meeting, I ___ attended it.",
                        "tip": "Tip: third conditional.",
                        "options": ["would have", "will have", "have", "am"],
                        "answer": "would have"
                    },
                    {
                        "question": "The project, which was very complex, ___ completed on time.",
                        "tip": "Tip: passive voice.",
                        "options": ["was", "were", "has", "be"],
                        "answer": "was"
                    }
                ]
            },
            "reading": {
                "title": "Reading",
                "instruction": "Read the text and answer the questions.",
                "text": """Fluency is not only about knowing many words.
It also involves understanding context, tone, and cultural references.
Advanced learners often need to practice real conversations.
They should also read complex texts and express opinions clearly.
This helps them communicate with confidence.""",
                "questions": [
                    {
                        "question": "What is fluency not only about?",
                        "options": ["Knowing many words", "Driving", "Sleeping", "Cooking"],
                        "answer": "Knowing many words"
                    },
                    {
                        "question": "What does fluency involve?",
                        "options": ["Context, tone, and cultural references", "Only grammar", "Only translation", "Silence"],
                        "answer": "Context, tone, and cultural references"
                    },
                    {
                        "question": "What helps advanced learners communicate?",
                        "options": ["Confidence", "Avoiding speaking", "Ignoring texts", "Memorizing only"],
                        "answer": "Confidence"
                    }
                ]
            },
            "listening": {
                "title": "Listening",
                "instruction": "Watch the video and answer the questions.",
                "youtube_url": "https://www.youtube.com/embed/MfW9rkoDABg",
                "questions": [
                    {
                        "question": "Why does Todd say his father's job is a little dangerous?",
                        "options": [
                            "Because he cuts trees",
                            "Because he drives buses",
                            "Because he works at sea",
                            "Because he is a firefighter"
                        ],
                        "answer": "Because he cuts trees"
                    },
                    {
                        "question": "What do Todd and Aimee have in common?",
                        "options": [
                            "Both are teachers",
                            "Both are married",
                            "Both are from Glasgow",
                            "Both are retired"
                        ],
                        "answer": "Both are teachers"
                    },
                    {
                        "question": "Which statement is TRUE according to the conversation?",
                        "options": [
                            "Todd is married",
                            "Aimee's father used to be a teacher",
                            "Todd's mother is retired",
                            "Aimee is from Los Angeles"
                        ],
                        "answer": "Aimee's father used to be a teacher"
                    }
                ]
            },
            "speaking": {
                "title": "Speaking",
                "instruction": "Practice speaking aloud.",
                "sentences": [
                    "Read this sentence aloud: Communication requires clarity and confidence.",
                    "Repeat the sentence and focus on rhythm and intonation.",
                    "Answer speaking: How can English help your future career?"
                ]
            }
        }
    }
}


QUIZ = {
    "iniciante": [
        {"question": "What is the past of go?", "options": ["go", "went", "goes", "going"], "answer": "went"},
        {"question": "Choose the correct sentence.", "options": ["She are happy", "She is happy", "She am happy"], "answer": "She is happy"},
        {"question": "Complete: They ___ students.", "options": ["is", "am", "are"], "answer": "are"}
    ],
    "basico": [
        {"question": "Complete: I ___ English every day.", "options": ["study", "studies", "studying"], "answer": "study"},
        {"question": "What does bookstore mean?", "options": ["Livraria", "Hospital", "Escola"], "answer": "Livraria"},
        {"question": "Complete: He ___ coffee.", "options": ["drink", "drinks", "drinking"], "answer": "drinks"}
    ],
    "intermediario": [
        {"question": "Complete: If I had money, I ___ travel.", "options": ["will", "would", "am"], "answer": "would"},
        {"question": "What is important for language learning?", "options": ["Consistency", "Never practicing", "Avoiding mistakes"], "answer": "Consistency"},
        {"question": "Complete: I have lived here ___ 2020.", "options": ["since", "for", "at"], "answer": "since"}
    ],
    "avancado": [
        {"question": "Complete: The lecture had already ___ when we arrived.", "options": ["started", "start", "starting"], "answer": "started"},
        {"question": "Advanced fluency involves:", "options": ["Context and tone", "Only simple words", "No conversation"], "answer": "Context and tone"},
        {"question": "Complete: I would have gone if I ___ known.", "options": ["had", "have", "has"], "answer": "had"}
    ]
}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("levels"))

    return render_template("index.html")


@app.route("/levels", methods=["GET", "POST"])
def levels():
    if "username" not in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        session["level"] = request.form.get("level")
        return redirect(url_for("activity", activity_type="grammar"))

    return render_template("levels.html", username=session["username"])


@app.route("/activity/<activity_type>", methods=["GET", "POST"])
def activity(activity_type):
    if "level" not in session:
        return redirect(url_for("levels"))

    level = session["level"]
    level_data = LEVELS[level]
    activity_data = level_data["activities"].get(activity_type)
    progress = get_progress(activity_type)

    if request.method == "POST":
        score = 0
        questions = activity_data.get("questions", [])

        for index, question in enumerate(questions):
            user_answer = request.form.get(f"question_{index}")

            if user_answer == question["answer"]:
                score += 1

        if level_data["language"] == "pt":
            feedback = f"Você acertou {score} de {len(questions)} questões."
        else:
            feedback = f"You got {score} out of {len(questions)} questions correct."

        return render_template(
            "activity.html",
            activity_type=activity_type,
            activity=activity_data,
            level_data=level_data,
            feedback=feedback,
            progress=progress
        )

    return render_template(
        "activity.html",
        activity_type=activity_type,
        activity=activity_data,
        level_data=level_data,
        feedback=None,
        progress=progress
    )


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if "level" not in session:
        return redirect(url_for("levels"))

    level = session["level"]
    questions = QUIZ[level]
    level_data = LEVELS[level]
    progress = get_progress("quiz")

    if request.method == "POST":
        score = 0

        for index, question in enumerate(questions):
            user_answer = request.form.get(f"question_{index}")

            if user_answer == question["answer"]:
                score += 1

        return render_template(
            "result.html",
            username=session["username"],
            score=score,
            total=len(questions),
            level_data=level_data
        )

    return render_template(
        "activity.html",
        activity_type="quiz",
        quiz_questions=questions,
        level_data=level_data,
        feedback=None,
        progress=progress
    )


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)