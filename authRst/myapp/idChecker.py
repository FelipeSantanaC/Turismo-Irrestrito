from django.db import models

class IDChecker:
    @staticmethod
    def get_next_id(model_class):
        try:
            latest_obj = model_class.objects.latest('id')
            last_id = latest_obj.id
            next_id = last_id + 1
        except model_class.DoesNotExist:
            next_id = 1
        
        return next_id