from django.contrib import admin

from problem.models import Problem, ProblemStatus, ProblemSet, ProblemInSet

# Register your models here.
admin.site.register(ProblemStatus)
admin.site.register(Problem)
admin.site.register(ProblemSet)
admin.site.register(ProblemInSet)
