from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class OnlineJudge(models.Model):
    name = models.CharField("OnlineJudge Name", primary_key=True, max_length=30, unique=True)
    url = models.URLField("OnlineJudge Website Index")


class OJUser(models.Model):
    platform = models.ForeignKey(OnlineJudge, on_delete=models.CASCADE)
    userId = models.CharField("Username for identification", max_length=60)
    realUser = models.ForeignKey(User, on_delete=models.CASCADE)

#
# class Submission(models.Model):
#     platform = models.ForeignKey(OnlineJudge, on_delete=models.CASCADE)
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     realUser = models.ForeignKey(User, on_delete=models.CASCADE)
#     subId = models.CharField("SubmissionId on certain OJ", primary_key=True, max_length=30)
#     QUEUEING = 'QU'
#     COMPILING = 'CO'
#     RUNNING = 'RU'
#     ACCEPTED = 'AC'
#     WRONG_ANSWER = 'WA'
#     RUNTIME_ERROR = 'RE'
#     PRESENTATION_ERROR = 'PE'
#     TIME_LIMIT_EXCEEDED = 'TLE'
#     MEMORY_LIMIT_ECEEDED = 'MLE'
#     OUTPUT_LIMIT_EXCEEDED = 'OLE'
#     COMPILATION_ERROR = 'CE'
#     SYSTEM_ERROR = 'SE'
#     RESULT_CHOICES = (
#         (QUEUEING, 'Queuing'),
#         (COMPILING, 'Compiling'),
#         (RUNNING, 'Running'),
#         (ACCEPTED, 'Accepted'),
#         (WRONG_ANSWER, 'Wrong Answer'),
#         (RUNTIME_ERROR, 'Runtime Error'),
#         (PRESENTATION_ERROR, 'Presentation Error'),
#         (TIME_LIMIT_EXCEEDED, 'Time Limit Exceeded'),
#         (MEMORY_LIMIT_ECEEDED, 'Memory Limit Exceeded'),
#         (OUTPUT_LIMIT_EXCEEDED, 'Output Limit Exceeded'),
#         (COMPILATION_ERROR, 'Compilation Error'),
#         (SYSTEM_ERROR, 'System Error')
#     )
#     result = models.CharField('Result of Submission', max_length=30)
#
#     #result = models.CharField('Result of Submission', max_length=3, choices=RESULT_CHOICES)
#     uploadTime = models.CharField('The Time you Submit', max_length=30)
#
