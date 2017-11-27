from django.shortcuts import render
from django.http import HttpResponse

from booths.models import Employee

# Create your views here.
def index(request):
	name="manoj"
	return render(request, 'index.html', {name:'name'})


def home(request):
	if request.method == "POST":
		x = request.POST
		name = x.get('name')
		salary = x.get('salary')
		Employee.objects.create(name=name, salary=salary)
		return render(request, 'home.html')
		# import pdb; pdb.set_trace()
	# name='jaggu'
	# salry=2000
	if request.method == "GET":
		e = Employee.objects.all()
	return render(request, 'emp.html', {'Employee': e})



# def form(request):
# 	return render(request, 'form.html')
