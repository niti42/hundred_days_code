from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

if __name__ == "__main__":
    question_bank = []
    for q in question_data:
        question_bank.append(Question(q.get("question"), q.get("correct_answer")))
    q = QuizBrain(question_bank)
    while q.still_has_questions():
        q.next_question()
    print("You've completed the quiz")
    print(f"Your final score was: {q.score}/{q.question_number}")

