import cloudinary.uploader
from django.shortcuts import redirect, render

from .forms import EntryForm
from .models import Entry


def guestbook(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)

        if form.is_valid():
            image = form.cleaned_data.get('image')
            pic_link = None

            if image:
                result = cloudinary.uploader.upload(
                    image,
                    resource_type='image',
                    timeout=10
                )
                pic_link = result['secure_url']

            Entry.objects.create(
                name=form.cleaned_data.get('name') or 'anonymous',
                message=form.cleaned_data.get('message') or '',
                pic_link=pic_link
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
