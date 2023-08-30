from django.db import models
from myapp.models import MyUser, Local, TiposRecursos
from django.db.models import Avg

class Rating(models.Model):       
    user = models.ForeignKey(MyUser, verbose_name="user", on_delete=models.CASCADE)
    local = models.ForeignKey(Local,verbose_name="local", on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        average_score = Rating.objects.filter(local=self.local).aggregate(Avg('rating'))['rating__avg']
        self.local.nota = average_score
        self.local.save()

class Post(models.Model): 
    user = models.ForeignKey(MyUser, verbose_name="user", on_delete=models.CASCADE) # further create a get to retrieve its profile picture and name from user profile
    local = models.ForeignKey(Local, verbose_name="local", on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, verbose_name="rating", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class LocalTags(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    tag = models.ForeignKey(TiposRecursos, on_delete=models.CASCADE)


