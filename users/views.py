from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
      form = SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('index-blog')

    else:
       form = SignUpForm()  
    context = {
        'form' : form,
    }
    return render(request, 'users/sign_up.html', context)
