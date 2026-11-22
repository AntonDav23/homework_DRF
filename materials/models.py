from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )

    preview = models.ImageField(
        upload_to="courses/",
        verbose_name="Превью",
        help_text="Загрузите изображение курса",
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name="Описание курса",
        help_text="Укажите описание курса",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )

    description = models.TextField(
        verbose_name="Описание урока",
        help_text="Укажите описание урока",
        blank=True,
        null=True,
    )

    preview = models.ImageField(
        upload_to="lessons/",
        verbose_name="Превью",
        help_text="Загрузите изображение урока",
        blank=True,
        null=True,
    )

    link = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите Ссылка на видео",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons",
        verbose_name="Курс",
        help_text="Выберите курс, к которому относится урок",
    )

    def __str__(self):
        return self.name
