from data_temporary.classes import Test
from data_quest.questions import quest_iter, data


def quest_gen(option=None):
    if option is True:
        key = quest_iter.__next__()
        Test.question = key

        question = f'Вопрос {Test.question} из 70:\n{data[key][0]}'
        answer_a = data[key][1]
        answer_b = data[key][2]

        return question, answer_a, answer_b

    else:
        question = f'ℹ️ Вопрос {Test.question} из 70:\n\n{data[Test.question][0]}'
        answer_a = data[Test.question][1]
        answer_b = data[Test.question][2]

        return question, answer_a, answer_b
