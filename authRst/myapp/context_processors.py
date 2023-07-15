from .admin import UserCreationForm
def login_context(request):
    form = UserCreationForm
    context = {'form':form}
    return context