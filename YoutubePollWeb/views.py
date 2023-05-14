from django.shortcuts import render
from django.http import HttpResponse
from .models import Thumbnail


def compare(request):
    if request.method == 'GET':
        # Retrieve two random thumbnails from the database
        thumbnails = Thumbnail.objects.order_by('?')[:2]

        # Render the compare.html template with the thumbnails as context
        context = {'thumbnails': thumbnails}
        return render(request, 'compare.html', context)

def compare_thumbnails(request):
    # Retrieve two random thumbnails from the database
    thumbnails = Thumbnail.objects.order_by('?')[:2]

    # Render the compare.html template with the thumbnails as context
    context = {'thumbnails': thumbnails}
    return render(request, 'compare.html', context)

