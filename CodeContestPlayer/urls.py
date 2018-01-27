"""CodeContestPlayer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import login_page, add_account, profile_page
from problem.views import problem_set_page, add_problem_set, insert_problem_to_set

urlpatterns = [
    path('', include('index.urls')),
    path('login/', login_page),
    path('add_account/', add_account),

    path('profile/', profile_page),
    path('admin/', admin.site.urls),
    path('problem_set/', problem_set_page),
    path('add_problem_set/', add_problem_set),
    path('insert_problem_to_set/', insert_problem_to_set)

]
