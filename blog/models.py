from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=200, verbose_name='Область')
    text = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='region')
    country = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return self.region


class Destination(models.Model):
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING, verbose_name='Область', related_name='destinations')
    title = models.CharField(max_length=500, verbose_name='Название достопримичательноти')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class ImageDestination(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, verbose_name='Достопримичательность',
                                    related_name='images')
    image = models.ImageField(upload_to='destination', verbose_name='Фото')


class Blog(models.Model):
    author = models.CharField(verbose_name='Имя автора', max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def main_title(self):
        desc_obj = self.descriptions.filter(is_main=True, is_title=True)
        return desc_obj.first().description if desc_obj else ''

    @property
    def main_description(self):
        desc_obj = self.descriptions.filter(is_main=True, is_title=False)
        return desc_obj.first().description if desc_obj else ''

    @property
    def main_images(self):
        img_objs = self.images.filter(is_banner=True)
        return img_objs[:2]

    @property
    def first_main_img(self):
        return self.main_images[0] if self.main_images else None

    @property
    def second_main_img(self):
        return self.main_images[1] if self.main_images else None

    @property
    def single_descriptions(self):
        des_objs = self.descriptions.filter(is_main=False, is_title=False, is_list_item=False)
        return des_objs.values_list('description')

    @property
    def single_descriptions_up(self):
        return self.single_descriptions[:2]

    @property
    def single_descriptions_after_img(self):
        return self.single_descriptions[2:6]

    @property
    def single_descriptions_after_list(self):
        return self.single_descriptions[6:]

    @property
    def single_images(self):
        img_objs = self.images.filter(is_banner=False)
        return img_objs[:3]

    @property
    def single_title(self) -> str:
        des_obj = self.descriptions.filter(is_main=False, is_title=True, is_list_item=False)
        return des_obj.first().description if des_obj else ''

    @property
    def list_descriptions(self):
        des_objs = self.descriptions.filter(is_main=False, is_title=False, is_list_item=True)
        for i in des_objs:
            yield i


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images', verbose_name='Блог')
    image = models.ImageField(verbose_name='Фото')
    is_banner = models.BooleanField(default=False, verbose_name='На обложку')

    def save(self, **kwargs):
        if self.is_banner and self.__class__.objects.filter(blog=self.blog, is_banner=True).count() > 2:
            raise ValueError({'is_banner': 'there are already two banners for this blog'})
        return super().save(**kwargs)


class BlogDescription(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='descriptions',
                             verbose_name='Блог')
    is_main = models.BooleanField(default=False, verbose_name='На главную')
    is_title = models.BooleanField(default=False, verbose_name='На заглавие')
    is_list_item = models.BooleanField(default=False, verbose_name='Элемент списка')
    description = models.TextField(verbose_name='Описание')

    def save(self, **kwargs):
        if self.is_main and self.is_title and self.__class__.objects.filter(
                blog=self.blog, is_main=True, is_title=True).count() > 1:
            raise ValueError({'detail': 'Main title for blog already exists'})

        if (self.is_main and self.is_list_item) or (self.is_title and self.is_list_item):
            raise ValueError({'detail': 'Options invalid!'})
        return super().save(**kwargs)



