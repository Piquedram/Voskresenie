from celery import shared_task
import datetime

from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Category, Post, CategorySubscribers


@shared_task
def weekly_notify():

    for cat in Category.objects.all():

        rl = []
        for sub in CategorySubscribers.objects.filter(category_id=cat.id):
            for u in User.objects.filter(id=sub.subscriber.id).values('email'):
                rl.append(u['email'])

        msg = f'Список публикаций:\n'
        for post in Post.objects.filter(category=cat.id, added__gt=datetime.datetime.now()-datetime.timedelta(days=7)):
            msg += f'{post.name} - http://127.0.0.1:8000/posts/{post.id}\n'

        subj = f'Здравствуй! Публикации в категории {cat.name} за прошедшую неделю.'

        send_mail(
            subject=subj,
            message=msg,
            from_email='mail@yandex.ru',
            recipient_list=rl,
            fail_silently=True,
        )
