from django.shortcuts import render
from .models import List
from django.shortcuts import redirect

# # Create your views here.

def index(request):
    if request.method == 'GET': 
        lists = List.objects.all()
        return render(request, 'listpage/index.html', {'lists': lists})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        due_date = request.POST.get('due_date',None)
        degree = request.POST['degree']
        if (due_date!=None) :
            List.objects.create(title=title, content=content, due_date=due_date, degree=degree)
        else :
            List.objects.create(title=title, content=content, degree=degree)
        return redirect('/lists')


def new(request):
    return render(request, 'listpage/new.html')

def show(request, id):
    if request.method == 'GET': # show
        list = List.objects.get(id=id)
        return render(request, 'listpage/show.html', {'list': list})
    elif request.method == 'POST': # update
        list = List.objects.get(id=id)
        title = request.POST['title']
        content = request.POST['content']
        due_date = request.POST.get('due_date','')
        degree = request.POST['degree']
        list.title = title
        list.content = content
        list.due_date = due_date
        list.degree = degree
        list.save()
        return redirect('/lists')
    

def delete(request, id):
    list = List.objects.get(id=id)
    list.delete()
    return redirect('/lists')

def edit(request, id):
    list = List.objects.get(id=id)
    return render(request, 'listpage/edit.html', {'list': list})