from django import template

register = template.Library()


@register.filter
def addclass(field, css):
    '''Добавляет CSS-класс к тегу шаблона.

    Args:
        field: Поле формы, к которому необходимо добавить атрибут.
        css: Название атрибута, который необходимо добавить к тегу.

    Returns:
        Атрибут CSS-класс.
    '''

    return field.as_widget(attrs={'class': css})
