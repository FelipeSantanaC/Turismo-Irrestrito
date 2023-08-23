from django.shortcuts import render
from django.http import JsonResponse
from local_interactions.models import Post


def get_posts_by_local(request, local_id):
    posts = Post.objects.select_related('rating_id', 'user_id__userprofile').filter(local_id=local_id).values('rating_id__rating', 'content', 'timestamp', 'user_id__name', 'user_id__userprofile__foto_perfil')
    data = [
        {
            'rating': post['rating_id__rating'],
            'content': post['content'],
            'timestamp': post['timestamp'],
            'name': post['user_id__name'],
            'profile_picture': post['user_id__userprofile__foto_perfil']
        }
        for post in posts
    ]
    return JsonResponse(data, safe=False)

    
