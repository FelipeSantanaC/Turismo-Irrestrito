from .forms import RatingForm, PostForm
def post_rating(request):
    context = {'rating_form': RatingForm , 'post_form':PostForm}
    return context