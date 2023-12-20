from django import template

from posts.models import Like

register = template.Library()


@register.simple_tag
def checking_like(user, post) -> bool:
    '''Проверка на наличие лайка пользователя у поста.

    Args:
        user: Пользователь.
        post: Пост.

    Returns:
        True, если лайк стоит и False, если лайк отсутствует.
    '''
    return Like.objects.filter(
        user=user,
        post=post,
    ).exists()
