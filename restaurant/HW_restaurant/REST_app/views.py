from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import Restaurant_list
# Create your views here.
def rest_app(request):
    template = loader.get_template('master.html')
    return HttpResponse(template.render())

def rest_list(request):
    #print(request)
    if request.method == 'POST':
        form = rest_list(request.POST)
        if form.is_valid():
            #first_name = form.cleaned_data['firstname']
            #last_name = form.cleaned_data['lastname']
            #greeting = f"Hi, {first_name} {last_name}!"
            #print(greeting)
            form.save()
            return render(request, 'home.html')