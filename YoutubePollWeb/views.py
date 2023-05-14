from django.http import HttpResponse
from django.shortcuts import render
from .video_comparison import VideoComparison

def compare_videos(request):
    # Get the video URLs from the request
    video_url1 = request.GET.get('video_url1')
    video_url2 = request.GET.get('video_url2')

    # If both URLs are present, perform the comparison
    if video_url1 and video_url2:
        # Initialize the VideoComparison object
        comparison = VideoComparison(video_url1, video_url2)

        # Get the comparison results
        result = comparison.compare()

        # Pass the results to the template
        context = {'result': result}
        return render(request, 'compare_videos.html', context)

    # If the URLs are not present, just render the page
    else:
        return render(request, 'compare_videos.html')




def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')