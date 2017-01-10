from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignupForm
from twilio.rest import TwilioRestClient

def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            ACCOUNT_SID = "AC1ff17efc8a25502eacba5b59825d090f" 
            AUTH_TOKEN = "4321056c12f4ba6de2982cb2835504dc"    
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)     
            client.messages.create(
                to="+15163535462", 
                from_="+15162104088", 
                body= '\n' + name + '\n' + email,  
            ) 
            return HttpResponseRedirect('/thanks/')
    else:   
        form = SignupForm()
        
    return render(request, 'home/index.html', {'form': form})

def thanks(request):
    return render(request, 'home/thanks.html')

def portrait(request):
    return render(request, 'home/portrait.html')

