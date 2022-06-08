from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=200, verbose_name='Почта')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')

    def __str__(self):
        return 'Контакты'


class Banner(models.Model):
    title = models.TextField(verbose_name='Название банера')

    def __str__(self):
        return 'Название банера'


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo_image')

    def __str__(self):
        return 'Логотип'


class About(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    image = models.ImageField(upload_to='about')
    text = models.TextField(verbose_name='Описание о нас')
    video = models.CharField(max_length=500, verbose_name='Ссылка на видео')
    favorite_text = models.TextField(verbose_name='Текст фаворита')

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя комментатора')
    text = models.TextField(verbose_name='Текст отзыва')

    def __str__(self):
        return self.name


class CategoryKGZ(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название категории')
    slug = models.CharField(max_length=300, verbose_name='Слаг', primary_key=True)


class Kyrgyzstan(models.Model):
    category = models.ForeignKey(CategoryKGZ, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=500, verbose_name='Название')
