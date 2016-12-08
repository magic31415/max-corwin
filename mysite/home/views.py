from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm

def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            with open('records.txt', 'w') as f:
                f.write(name + '\t' + email +'\n')
            return HttpResponseRedirect('/thanks/')
    else:   
        form = SignupForm()
        
    return render(request, 'home/index.html', {'form': form})

def thanks(request):
    return render(request, 'home/thanks.html')
