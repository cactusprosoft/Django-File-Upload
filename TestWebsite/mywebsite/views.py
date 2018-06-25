from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .models import Profile

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
            return redirect('index')
        else:
            context = {'form': ProfileForm()}
            return render(request, 'mywebsite/index.html', context)
    else:
        context = {'form': ProfileForm()}
        return render(request, 'mywebsite/index.html', context)
