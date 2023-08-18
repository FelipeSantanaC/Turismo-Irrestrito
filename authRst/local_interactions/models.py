from django.db import models
from myapp.models import MyUser, Local

class Rating(models.Model):       
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    local_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    rating = models.IntegerField()

class Post(models.Model): 
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE) # further create a get to retrieve its profile picture and name from user profile
    local_id = models.ForeignKey(Local, on_delete=models.CASCADE)
    rating_id = models.ForeignKey(Rating, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



