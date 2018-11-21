from django.db import models


# Create your models here.

class Question(models.Model):
    question_text =  models.CharField(max_length=200)
    closed =  models.BooleanField(default=False)
    pub_date = models.DateField(null=True)

    def is_close(self):
        self.closed = not self.closed
        self.save()

    def __str__(self):
        return self.question_text

    def result(self):
        total =  (self.choice_set.aggregate(models.Sum('votes')))["votes__sum"]
        choices =  self.choice_set.all()
        for choice in choices:
            choice.percentual = round(choice.votes / total * 100, 2)
        return {
                "total": total,
                "choices": choices
            }


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    choice_text =  models.CharField(max_length=100)
    votes =  models.IntegerField(default=0)

    def vote(self):
        self.votes += 1
        self.save()

    def attach(self, question):
        self.question = question
        self.save()

    def remove(self):
        self.question = None
        self.save()

    @staticmethod
    def unrealted():
        return Choice.objects.filter(question__isnull=True)

    def __str__(self):
        return self.choice_text