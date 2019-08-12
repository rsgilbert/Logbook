from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .forms import LogModelForm
from log.models import Log



def log(request):
    if request.method == "POST":
        form = LogModelForm(request.POST)
        if form.is_valid():
            data = form.save()
            print(data)
            return HttpResponseRedirect(reverse('log:log'))
    
    else:
        form = LogModelForm()
    
    return render(request, 'log.html', {'logform': form})
