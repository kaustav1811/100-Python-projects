from question_model import Question
from brain import QuizBrain
import random

from data import Question_data1

Question_bank = []

for question in Question_data1:
    question_text = question["question"]
    question_answer = question["answer"]
    new_question = Question(question=question_text, answer=question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{len(Question_bank)}")

"""
Future improvements - we can create a loop of 14 question data sets and to pass from one to another 
                      player should get atleast 7 correct out of 10 else he fails to go to next 
                      level.

                      divide the datasets as per easy medium difficult. 
                      each consist of 5 levels, so in total we will have 15 levels.
"""