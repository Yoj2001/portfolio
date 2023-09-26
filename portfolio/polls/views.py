from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Programmer, Project


# home page
def programmers_list(request):
    programmers = Programmer.objects.order_by("-age")
    contex = {"programmers": programmers}
    return render(request, "polls/index.html", contex)


# about users
def detail(request, prog_id):
    programmer = Programmer.objects.get(pk=prog_id)
    des = programmer.project_set.all()
    contex = {"programmer": programmer.user.first_name, "last_name": programmer.user.last_name,
              "age": programmer.age, "des": des, 'prog_id': programmer.id}
    return render(request, "polls/detail.html", contex)


# add User
def add_user(request):
    return render(request, "polls/add_user.html")


def user_save(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            name = request.POST["name"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            age = request.POST["age"]
            password = request.POST["password"]
            language = request.POST["language"]
            framework = request.POST["framework"]
            experience = request.POST["experience"]
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = name
            user.last_name = lastname
            user.save()
            programmer = Programmer(user=user, age=age, language=language, framework=framework, experience=experience)
            programmer.save()
        except:
            return redirect("/")
        else:
            return redirect("/")


# add project
def add_project_page(request, programmer_id):
    return render(request, "polls/add_project_page.html", {"programmer_id": programmer_id})


def add_project(request, programmer_id):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        new_project = Project(
            programmer=Programmer.objects.get(pk=programmer_id),
            name=name,
            description=description,
        )
        new_project.save()
        programmers = Programmer.objects.order_by("-age")
        contex = {"programmers": programmers, "success": "new Project successfully created"}
    return render(request, "polls/index.html", contex)
