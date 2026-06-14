from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

def guestbook(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            Entry.objects.create(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message']
            )
            return redirect('/guestbook')
    else:
        form = EntryForm()

    entries = Entry.objects.all().order_by('-date')
    return render(request, 'guestbook.html', {
        'form': form,
        'entries': entries
    })

def home(request):
    return render(request, 'index.html')

def manifesto(request):
    return render(request, 'manifesto.html')

