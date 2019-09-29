from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Category


# Create your views here.

def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect("/")
        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "index.html", {"todos": todos, "categories": categories})


def details(request, todo_id):
    try:
        # todo = TodoList.objects.get(pk=todo_id)
        todo = get_object_or_404(TodoList, pk=todo_id)
    except TodoList.DoesNotExist:
        raise Http404("Object does not exist")
    return render(request, 'detail.html', {'todo': todo})
