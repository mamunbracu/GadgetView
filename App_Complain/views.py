from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from App_Complain.forms import ComplainForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here

@login_required
def complain(request):
    
    form = ComplainForm()
    if request.method == 'POST':
        form = ComplainForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, "Your Complain has been Submitted! We will give investigate your complain")
            return HttpResponseRedirect(reverse('App_Shop:home'))

    return render(request, 'App_Complain/complain.html', context={'title':'Complain', 'form':form})