from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from quora.models import Question, Answer, Upvote
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(
            username = username,
            password = password,
            email = email)
        login(request,user)
        return redirect('/dashboard/')
    return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username = username, password = password)

        if user != None:
            login(request,user)
            return redirect('/dashboard/')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('/signin/')

def dashboard(request):
	all_questions = Question.objects.all().order_by('-timestamp')
	all_answers = Answer.objects.all().order_by('-timestamp')
	return render(request, "dashboard.html", {"all_questions":all_questions, "all_answers":all_answers})

def questions(request):
	if request.method == "POST":
		question = request.POST['question']
		question_instance = Question.objects.create(
			question=question,
			author=request.user
			)
		return redirect("/dashboard/")
	all_questions = Question.objects.all().order_by('-timestamp')
	return render(request, "question.html", {"all_questions":all_questions})

def discussion(request, question_id):
	question = Question.objects.get(pk=question_id)
	if request.method == "POST":
		answer = request.POST["answer"]
		answer_instance = Answer.objects.create(
			answer=answer,
			question=question,
			author=request.user,
			upvotes=1)
		return redirect(f"/discussion/{question.id}")

	all_answers = Answer.objects.filter(question=question_id)
	return render(request, "discussion.html", {"question":question, "all_answers":all_answers})

def upvote(request, answer_id):
	answer = Answer.objects.get(pk=answer_id)
	upvotes = Upvote.objects.filter(reader=request.user, answer=answer)
	if len(upvotes) == 0:
		answer.upvotes += 1
		answer.save()
		upvote = Upvote.objects.filter(reader=request.user, answer=answer)
		upvote.save()
	return redirect(f"/discussion/{answer.question.id}")