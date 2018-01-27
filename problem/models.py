from django.db import models

from account.models import User, OnlineJudge


# Create your models here.
class Problem(models.Model):
    platform = models.ForeignKey(OnlineJudge, on_delete=models.CASCADE)
    probId = models.CharField("Problem id for identification", max_length=30)
    title = models.CharField("Problem Title will be crawlled later", max_length=30, default="TODO")
    url = models.URLField()
    # RelProblem = models.ManyToManyField(
    #     User,
    #     through='Submission',
    #     through_fields=('problem', 'realUser'),
    # )
    RelProblem = models.ManyToManyField(
        User,
        through='ProblemStatus',
        through_fields=('problem', 'realUser'),
    )


class ProblemStatus(models.Model):
    is_AC = models.BooleanField(default=False)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    realUser = models.ForeignKey(User, on_delete=models.CASCADE)


class ProblemSet(models.Model):
    setName = models.CharField("name of ProblemSet", max_length=200, unique=True)
    hasProblem = models.ManyToManyField(
        Problem,
        through='ProblemInSet',
        through_fields=("set", "problem")
    )
    setCreator = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='root')
    author = models.CharField("author of this ProblemSet", default="Unknown", max_length=30)


class ProblemInSet(models.Model):
    set = models.ForeignKey(ProblemSet, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
