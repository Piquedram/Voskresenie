from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template import loader

from .models import PostCategory


@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, **kwargs):
    rl = []
    for c in PostCategory.objects.filter(post_id=instance.id):
        for u in User.objects.filter(category=c.category_id).values('email'):
            rl.append(u['email'])
    rl = list(set(rl))

    sub = 'Здравствуй! Новая статья в твоём любимом разделе!'
    msg = ''
    html_msg = loader.render_to_string(
        'new_post_msg.html',
        {
            'head': instance.name,
            'body': instance.content[:50],
            'link': f'http://127.0.0.1:8000/{instance.id}'
        }
    )

    send_mail(
        subject=sub,
        message=msg,
        from_email='email@yandex.ru',
        recipient_list=rl,
        fail_silently=False,
        html_message=html_msg
    )
