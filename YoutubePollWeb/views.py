import random
from django.shortcuts import render
from django.http import JsonResponse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from API_keys import API_KEY

def compare_videos(request):
    video_url1 = request.GET.get('video_url1')
    video_url2 = request.GET.get('video_url2')

    if video_url1 and video_url2:
        comparison = VideoComparison(video_url1, video_url2)
        result = comparison.compare()
        context = {'result': result}
        return render(request, 'compare_videos.html', context)
    else:
        return render(request, 'compare_videos.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    #these are not definate urls these are just for a shrt time due to strugles with API. will soon be fixed!
    thumbnail_url1 = "https://i.ytimg.com/an_webp/8wysIxzqgPI/mqdefault_6s.webp?du=3000&sqp=CPy5iKMG&rs=AOn4CLBAB95hbtqFLgS8mBAmACdEOxDRGw"
    thumbnail_url2 = "https://i.ytimg.com/an_webp/sW9npZVpiMI/mqdefault_6s.webp?du=3000&sqp=CObFiKMG&rs=AOn4CLDbkInDKkv4_22DvyKGOnDiLvuuog" 
    context = {
        'thumbnail_url1': thumbnail_url1,
        'thumbnail_url2': thumbnail_url2
    }

    return render(request, 'index.html', context)

def fetch_new_thumbnails(request):
    thumbnail_url1 = fetch_random_video()
    thumbnail_url2 = fetch_random_video()

    data = {
        'thumbnail_url1': thumbnail_url1,
        'thumbnail_url2': thumbnail_url2
    }

    return JsonResponse(data)

def fetch_random_video():
    api_key = API_KEY

    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            part='snippet',
            q='your_search_query',
            maxResults=10
        )
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
