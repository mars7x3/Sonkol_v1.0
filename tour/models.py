from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория тура')
    slug = models.CharField(max_length=100, verbose_name='Слаг на англ.')

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название тура')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория тура',
                                 related_name='tours')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='tour_banner', verbose_name='Баннер', blank=True, null=True)
    count_person = models.IntegerField(verbose_name='Количество людей')
    tour_days = models.IntegerField(verbose_name='Длительность тура в днях')
    min_price = models.IntegerField(verbose_name='Минимальная цена')
    start_session = models.CharField(max_length=100, verbose_name='Начало сезона')
    finish_session = models.CharField(max_length=100, verbose_name='Конец сезона')

    def __str__(self):
        return self.title


class Price(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='prices', verbose_name='Тур')
    person = models.IntegerField(verbose_name='Сколько человек')
    price = models.IntegerField(verbose_name='Цена')


class Day(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур', related_name='days')
    title = models.CharField(max_length=300, verbose_name='Название дня')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.tour} -- {self.title}'


class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='Тур', related_name='images')
    image = models.ImageField(upload_to='tour_images', verbose_name='Фото')
