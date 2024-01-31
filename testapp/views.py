from django.shortcuts import render
from testapp.form import StudentForm

# Create your views here.
def forms(request):
    form = StudentForm()
    return render(request,'testapp/register.html', {'form':form})