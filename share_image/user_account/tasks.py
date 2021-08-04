from celery import shared_task
from django.core.mail import send_mail

from django.contrib.auth.models import User
from post.models import Post

from django.shortcuts import get_list_or_404

@shared_task()
def  send_user_followd_email(followedTo_user_id, followedBy_user_id):
    followed_to = get_object_or_404(User,pk = followedTo_user_id)
    followed_by = get_object_or_404(User,pk = followedBy_user_id)

    subject = " new User followed you."
    
    msg = f" Dear {followed_to.username}, \n An User named {followed_by.username} followed you." 

    mail = send_mail( subject, msg, 'admin@share_image.com', [followed_to.email])