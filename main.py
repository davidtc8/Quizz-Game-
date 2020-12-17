from question_model import Question
from data import question_data
import random

question_bank = []

for dic in question_data:
    for key in dic.items():
        question = Question(dic["text"], dic["answer"])
    print('{}, {}'.format(question.text, question.answer))
        #q_text = question.text + " " + question.answer
        #print(q_text)
        #question_bank.append(q_text)
        #print(question_bank)

