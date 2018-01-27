from django.shortcuts import render

from problem.models import ProblemSet


# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'set_list': ProblemSet.objects.all(),
    })
