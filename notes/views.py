from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Notes

def list(requests):
    all_notes = Notes.objects.all()

    return render(requests, 'notes/notes_list.html', {'notes': all_notes})

def detail(requests, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")

    return render(requests, 'notes/notes_detail.html', {'note': note})
