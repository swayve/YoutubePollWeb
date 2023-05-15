from django.http import HttpResponse
from django.shortcuts import render
from .video_comparison import VideoComparison
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random

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
    thumbnail_url = fetch_random_video()

    context = {
        'thumbnail_url': thumbnail_url
    }

    return render(request, 'index.html', context)


def fetch_random_video():
    api_key = 'YOUR_API_KEY'  # Replace with your own YouTube API key

    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            part='snippet',
            q='your_search_query',  # Replace with your own search query
            maxResults=10
        )
        response = request.execute()
        items = response['items']
        random_video = random.choice(items)
        thumbnail_url = random_video['snippet']['thumbnails']['medium']['url']
        return thumbnail_url
    except HttpError as e:
        print(f'An HTTP error occurred: {e}')
        return None
