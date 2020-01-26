from django.shortcuts import render,redirect 
from django.urls import reverse       
from ToDoListApp.models import NoteSave
from ToDoListApp.forms import save
# Create your views here.
def index(req):
    notes=NoteSave.objects.all().order_by('time').reverse()
    print(notes)
         
    return render(req,'index.html',{'note':notes})
def submit(req):
        if req.method=='POST':
            form1 = save(req.POST)
            if form1.is_valid:
                form1.save(commit=True)
                msg='NOTE HAS BEEN SAVED'
                
                
            else:
                print('invalid data')
        return redirect(reverse('index'))

def delete(req,n):
    print(n)
    note = NoteSave.objects.filter(Note=n)
    note.delete()
    return redirect(reverse('index'))

