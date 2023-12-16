import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите название темы",
                        max_length=200,
                        unique=True,
                        verbose_name="название",
                    ),
                ),
            ],
            options={
                "verbose_name": "тема",
                "verbose_name_plural": "темы",
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, db_index=True),
                ),
                (
                    "modified",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
                (
                    "content",
                    models.TextField(
                        help_text="Введите содержимое поста",
                        verbose_name="содержимое поста",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        help_text="Введите автора поста",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="автор",
                    ),
                ),
                (
                    "topic",
                    models.ManyToManyField(
                        help_text="Введите темы поста",
                        to="posts.topic",
                        verbose_name="темы поста",
                    ),
                ),
            ],
            options={
                "verbose_name": "пост",
                "verbose_name_plural": "посты",
                "ordering": ("-created",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        help_text="Выберите пост",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="posts.post",
                        verbose_name="пост",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Выберите пользователя, который ставит лайк",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "лайк",
                "verbose_name_plural": "лайки",
            },
        ),
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(
                fields=("user", "post"),
                name="unique_likes",
            ),
        ),
    ]
