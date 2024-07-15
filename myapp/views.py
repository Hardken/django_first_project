from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.


def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })


def about(request):
    username = 'fazt'
    """
        username = {
             'name': "fazt"
        }
        """
    return render(request, 'about.html', {
        'username': username
    })


def hello(request, username):
    # result = id + 100 *2
    return HttpResponse("<h2>Hello %s</h2>" % username)


def projects(request):
    # projects= list(Project.objects.values())
    projects = Project.objects.all()
    # return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task=Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


"""
def tasks(request, title):
    #task=Task.objects.get(id=id)
    #task=Task.objects.get(title=title)
    task=get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s' % task.title)
    return render(request, 'tasks.html')
"""


def create_tasks(request):
    """
    print(request.GET['title'])
    print(request.GET['description'])
    Task.objects.create(title = request.GET['title'], description=request.GET['description'], project_id=2)
    return render(request, 'create_task.html', {
         'form': CreateNewTask()
    })
    """
    if request.method == 'GET':
        # show interface
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(requets):
    if requets.method == 'GET':
        return render(requets, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        #print(requets.POST)
        project= Project.objects.create(name=requets.POST["name"])
        #print(project)
        return redirect('projects')

def project_detail(request, id):
    #print(id)
    #project= Project.objects.get(id=id)
    project= get_object_or_404(Project, id=id )
    #print(project)
    tasks= Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project' : project,
        'tasks':tasks
    })