"""ForumApp URL Configuration

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
from django.urls import path
from quora.views import signup, signin,signout, dashboard, questions,discussion,upvote, delete_questions, delete_answers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup),
    path('signin/',signin),
    path('signout/',signout),
    path('dashboard/',dashboard),
    path('questions/',questions),
    path('delete_questions/<int:question_id>/', delete_questions),
    path('discussion/<int:question_id>/',discussion),
    path('upvote/<int:answer_id>/',upvote),
    path('delete_answers/<int:answer_id>/',delete_answers),

]
