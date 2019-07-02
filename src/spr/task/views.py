from django.shortcuts import render,redirect
from .models import *


# def index(request, *args, **kwargs):  # the index view
#     todos = TodoList.objects.all() #quering all todos with the object manager
#     if request.method == "POST": #checking if the request method is a POST
#         if "taskAdd" in request.POST: #checking if there is a request to add a todo
#             title = request.POST["title"] #title
#             date = str(request.POST["date"]) #date
#             completed = request.POST["completed"]
#             in_progress = request.POST["in_progress"]
#             priority = request.POST["priority"]
#             milestone = request.POST["milestone"]
#             Todo = TodoList(title=title, due_date=date, completed=completed, in_progress=in_progress, priority=priority, milestone=milestone)
#             Todo.save() #saving the todo
#             return redirect("/") #reloading the page
#         if "taskDelete" in request.POST: #checking if there is a request to delete a todo
#             checkedlist = request.POST["checkedbox"] #checked todos to be deleted
#             for todo_id in checkedlist:
#                 todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
#                 todo.delete() #deleting todo
#     return render(request, "task.html", {"todos": todos})

def index(request, *args, **kwargs):
    todos = TodoList.objects.all()
    milestones = Milestone.objects.all()

    context = {
        "todos":todos,
        "milestones":milestones
    }
    return render(request, 'task.html', context)


