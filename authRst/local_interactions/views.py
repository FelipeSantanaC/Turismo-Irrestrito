from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from local_interactions.models import Post , LocalTags
from myapp.models import Local, TiposRecursos
from .forms import RatingForm, PostForm
from django.shortcuts import get_object_or_404

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
    local_id =request.POST.get("local_id")
    print(local_id)
    if request.method == 'POST':
        rating_form = RatingForm(request.POST)
        post_form = PostForm(request.POST)
        user = request.user
        local = Local.objects.get(id=local_id) # isso aqui tem que rever, não consegui puxar o id nem a instancia de Local da página, 

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

            selected_tags_ids = post_form.cleaned_data['tag_list'].values_list('id' , flat=True)
            for tag_id in selected_tags_ids:
                tag_instance = TiposRecursos(tag_id)
                local_tag_instance = LocalTags(local = local , tag =tag_instance)
                local_tag_instance.save()  
            return HttpResponse('Agradecemos sua contribuição.')

        else:
            return HttpResponse('Algo deu errado, preencha novamente os campos.')

def get_tags_for_local(request, local_id):
    local = get_object_or_404(Local, pk=local_id)
    tags = LocalTags.objects.filter(local=local)
    tag_info = [{'title': tag.tag.title, 'description': tag.tag.description} for tag in tags]
    return JsonResponse({'tags': tag_info})