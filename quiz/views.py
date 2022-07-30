from django.shortcuts import render

# Create your views here.

# create view to get all quizes
from quiz.models import Quiz, Question, Answer, Result, QuizType


def get_all_quizes(request):
    quiz = Quiz.objects.get(title='Test1')      # возвращает обьект
    print(quiz.title, quiz.quiz_type, quiz.teacher)
    # получить все вопросы для теста
    questions = quiz.question_set.all()     # список
    first_question = questions[0]
    # список ответов для первого вопроса
    answers = first_question.answer_set.all()       # <QuerySet [<Answer: 1.Do you love me?(Test1) : Yes>, <Answer: 1.Do you love me?(Test1) : No>, <Answer: 1.Do you love me?(Test1) : Vasya>, <Answer: 1.Do you love me?(Test1) : What?>]>
    print(answers)
    for answer in answers:
        print(answer.isCorrect)
    # quiz.questions = Question.objects.filter(test=quiz)
    # for question in quiz.questions:
    #    print("question ", question)
    #    question.answers = Answer.objects.filter(question=question)
    #    for answer in question.answers:
    #        print("answer ", answer)

    return render(request, 'staff/teachers.html', {'quizes': quiz})
