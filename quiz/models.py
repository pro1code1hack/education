from django.db import models


# Create your models here.


class QuizType(models.Model):
    name = models.CharField(max_length=100)  # TODO rewrite for options

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey('staff.Student', on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='+')
    user_score = models.PositiveIntegerField()


class Quiz(models.Model):
    title = models.CharField(max_length=80, blank=True)
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE, null=True)
    number_of_questions = models.IntegerField(null=True)
    required_score_to_pass = models.IntegerField()
    difficulty = models.CharField(max_length=6, choices=(('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')))
    test_type = models.ForeignKey('QuizType', on_delete=models.CASCADE)
    teacher = models.ForeignKey('staff.Teacher', on_delete=models.CASCADE)

    # pass_amount = models.IntegerField(default=3)
    # the_whole_score_in_points = models.IntegerField(default=10)

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    question_body = models.CharField(max_length=300)
    test = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}.{self.question_body}({self.test})'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_body = models.CharField(max_length=64)
    isCorrect = models.BooleanField()

    def __str__(self):
        return f'{self.question} : {self.answer_body}'


"""
Create the model Schedule which will have the array of days and related times for specific subject and group.
"""


# TODO прописать данные автоматически из гугл календаря + обработать их во внешнем вьюшке
