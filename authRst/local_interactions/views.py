from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from local_interactions.models import Post
from myapp.models import Local
from .forms import RatingForm, PostForm


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

def local_rate(request):
    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        post_form = PostForm(request.POST)
        user = request.user
        local = Local.objects.get(id=2) # isso aqui tem que rever, não consegui puxar o id nem a instancia de Local da página, 

        if rating_form.is_valid() and post_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = user
            rating.local = local
            rating.save()  
            
            post = post_form.save(commit=False)
            post.rating = rating
            post.local = local
            post.user = user
            post.save()
            return HttpResponse('Agradecemos sua contribuição.')
        else:
            return HttpResponse('Algo deu errado, preencha novamente os campos.')

    
