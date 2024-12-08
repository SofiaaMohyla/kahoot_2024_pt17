from DBManager import DBManager

db_manager = DBManager("kahoot.db")
#db_manager.create_tables()

#db_manager.add_quiz(2,
#                    "Квіз про Логіка",
#                    "деякий опис")
#print(db_manager.get_quizzes())
print(db_manager.get_questions(1))
#db_manager.add_question(2, 1, "Хто був 1 президентом?")
#db_manager.add_question(2, 1, "Хто був 1 президентом?")

#db_manager.add_options(3,1, "1992", 0)
