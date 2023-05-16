import random
from django.shortcuts import render
from django.http import JsonResponse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from API_keys import API_KEY
import os

API_KEY = os.environ.get(API_KEY)

def compare_videos(request):
    video_url1 = request.GET.get('video_url1')
    video_url2 = request.GET.get('video_url2')

    if video_url1 and video_url2:
        # Perform the video comparison logic here
        result = perform_video_comparison(video_url1, video_url2)
        context = {'result': result}
        return render(request, 'compare.html', context)
    else:
        return render(request, 'compare.html')

def perform_video_comparison(video_url1, video_url2):
    # Compare the video URLs and thumbnails
    if video_url1 != video_url2:
        # Perform the actual video comparison logic here
        # Replace this code with your custom logic to compare videos
        # and return the result
        result = {
            'video_url1': video_url1,
            'video_url2': video_url2,
            'comparison_result': random.choice(['Similar', 'Different'])
        }
    else:
        result = {
            'video_url1': video_url1,
            'video_url2': video_url2,
            'comparison_result': 'Same Video'
        }
    
    return result


def about(request):
    return render(request, 'about.html')

def index(request):
    thumbnail_url1 = fetch_random_video_thumbnail()
    thumbnail_url2 = fetch_random_video_thumbnail()

    context = {
        'thumbnail_url1': thumbnail_url1,
        'thumbnail_url2': thumbnail_url2
    }

    return render(request, 'index.html', context)

def fetch_new_thumbnails(request):
    thumbnail_url1 = fetch_random_video_thumbnail()
    thumbnail_url2 = fetch_random_video_thumbnail()

    data = {
        'thumbnail_url1': thumbnail_url1,
        'thumbnail_url2': thumbnail_url2
    }

    return JsonResponse(data)


def fetch_random_video_thumbnail():
    try:
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.videos().list(
            part='snippet',
            chart='mostPopular'
        )
        print(1)
        response = request.execute()
        items = response.get('items', [])

        if items:
            random_video = random.choice(items)
            thumbnail_url = random_video['snippet']['thumbnails']['medium']['url']
            return thumbnail_url
        else:
            print('No videos found.')
    except HttpError as e:
        print(f'An HTTP error occurred: {e}')

    return None
