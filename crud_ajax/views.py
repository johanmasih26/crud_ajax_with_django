from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User


# Create your views here.
def index(request):
    form = UserForm()
    data = User.objects.all()
    return render(request,'user_example/index.html',{'form':form,'data':data})



def save_data(request):
    if request.method == "POST":
        form=UserForm(request.POST)
        if form.is_valid():
         sid=request.POST.get('sid')
         name = request.POST['name']
         email = request.POST['email']
         password = request.POST['password']
         if(sid == ''):
            reg = User(name=name,email=email,password=password)
         else:
            reg = User(id=sid,name=name,email=email,password=password)
         reg.save()
         stud = User.objects.values()
         stud_data = list(stud)
          


        return JsonResponse({'status':'save','stud_data':stud_data})
    else:        
        # return JsonResponse({'status':'Save'})

        return JsonResponse({'status':'fail'})

def delete(request):
    if request.method == "POST":
        id = request.POST['id']
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':'deleted'})
    else:
        return JsonResponse({'status':'failed'})    



def edit(request):
    if request.method == "POST":
        id = request.POST['id']
        student = User.objects.get(pk=id)
        student_data = {'id':student.id,'name':student.name,'email':student.email,'password':student.password}
        return JsonResponse(student_data)
    else:
        return HttpResponse('get')   










