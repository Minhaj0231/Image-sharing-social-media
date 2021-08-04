from django.db.models.signals import m2m_changed  # for many to many feild 

from django.dispatch import receiver

from .models import Post 


@receiver(m2m_changed, sender=Post.liked_users.through)
def liked_users_modified(sender, instance, **kwargs):

    print("")
    print("")
    print("signal called")
    print("")
    print("")
    
    instance.total_likes = instance.liked_users.count()
    instance.save()



