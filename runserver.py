from flask import *

from DBManager import DBManager

app = Flask("Kahoot")
db_name = "kahoot.db"
app.secret_key = "123"


@app.route("/")
def index():
    db_manager = DBManager(db_name)
    quizzes = db_manager.get_quizzes()
    return render_template("index.html",quizzes=quizzes )

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/quizz/<int:quizz_id>")
def get_question(quizz_id):
    db_manager = DBManager(db_name)
    questions = db_manager.get_questions(quizz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0
    return redirect(url_for("show_question", quizz_id=quizz_id))


@app.route("/quizz/<int:quizz_id>/question")
def show_question(quizz_id):
    nomer = session["quest_index"]
    q = session["questions"][nomer]
    db_manager = DBManager(db_name)
    options = db_manager.get_options(q[0])

    return render_template("question.html",
                           question=q,
                           options=options,
                           quizz_id=quizz_id)


@app.route("/quizz/<int:quizz_id>/answer", methods=["POST"])
def answer_func(quizz_id):
    session["quest_index"] += 1

    if len(session["questions"]) <= session["quest_index"]:
        return redirect(url_for("result", quizz_id=quizz_id))
    else:
        return redirect(url_for("show_question", quizz_id=quizz_id))


@app.route("/quizz/<int:quizz_id>/result")
def result(quizz_id):
    return "РЕЗУЛЬТАТ"

app.run()