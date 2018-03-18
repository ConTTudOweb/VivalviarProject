from cloudinary.models import CloudinaryField
from django.db import models
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils.text import slugify
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


# def banner_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/banners/<instance.title>
#     ext = filename.split('.')[-1]
#     return 'banners/{0}.{1}'.format(slugify(instance.title), ext)


class Banner(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    # image = VersatileImageField('imagem', upload_to=banner_directory_path, help_text='Imagem com: 873 X 1280 pixels')
    image = CloudinaryField('imagem', help_text='Imagem com: 873 X 1280 pixels')

    def image_thumbnail_300(self):
        # return format_html('<img src="{}"/>', self.image.thumbnail['300x300'].url)
        return format_html(self.image.image(width=300, height=300, crop="thumb"))

    image_thumbnail_300.allow_tags = True
    image_thumbnail_300.short_description = 'imagem'

    def __str__(self):
        return self.title


# @receiver(models.signals.post_save, sender=Banner)
# def warm_Banner_image(sender, instance, **kwargs):
#     """Ensures Banner image files are created post-save"""
#     banner_img_warmer = VersatileImageFieldWarmer(
#         instance_or_queryset=instance,
#         rendition_key_set='banner',
#         image_attr='image'
#     )
#     banner_img_warmer.warm()
#
#
# @receiver(models.signals.post_delete, sender=Banner)
# def delete_Banner_files(sender, instance, **kwargs):
#     """
#     Deletes Banner file renditions on post_delete.
#     """
#     # Deletes Image Renditions
#     instance.image.delete_all_created_images()
#     # Deletes Original Image
#     instance.image.delete(save=False)


# def sponsor_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/sponsors/<instance.name>
#     ext = filename.split('.')[-1]
#     return 'sponsors/{0}.{1}'.format(slugify(instance.name), ext)


class Sponsor(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    link = models.CharField(max_length=250)
    # logo = VersatileImageField('logotipo', upload_to=sponsor_directory_path, help_text='Imagem com: 350 X 350 pixels')
    logo = CloudinaryField('logotipo', help_text='Imagem com: 350 X 350 pixels')
    position = models.IntegerField('posição', default=0)

    def logo_thumbnail_350(self):
        return format_html(self.logo.image(width=350, height=350, crop="thumb"))

    logo_thumbnail_350.allow_tags = True
    logo_thumbnail_350.short_description = 'logotipo'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'patrocinador'
        verbose_name_plural = 'patrocinadores'
        ordering = ('position', 'name')


# @receiver(models.signals.post_save, sender=Sponsor)
# def warm_sponsor_image(sender, instance, **kwargs):
#     """Ensures Sponsor image files are created post-save"""
#     sponsor_img_warmer = VersatileImageFieldWarmer(
#         instance_or_queryset=instance,
#         rendition_key_set='sponsor',
#         image_attr='logo'
#     )
#     sponsor_img_warmer.warm()
#
#
# @receiver(models.signals.post_delete, sender=Sponsor)
# def delete_sponsor_file(_, instance, **kwargs):
#     """
#     Deletes Sponsor file renditions on post_delete.
#     """
#     # Deletes Image Renditions
#     instance.logo.delete_all_created_images()
#     # Deletes Original Image
#     instance.logo.delete(save=False)


# def special_participation_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/special_participations/<instance.name>
#     ext = filename.split('.')[-1]
#     return 'special_participations/{0}.{1}'.format(slugify(instance.name), ext)


class SpecialParticipation(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    # image = VersatileImageField('imagem', upload_to=special_participation_directory_path, help_text='Imagem com: 300 X 300 pixels')
    image = CloudinaryField('imagem', help_text='Imagem com: 300 X 300 pixels')
    country = models.CharField('país', max_length=255, null=True, blank=True)

    def image_crop_300(self):
        return format_html(self.image.image(width=300, height=300, crop="fill", gravity="face"))

    image_crop_300.allow_tags = True
    image_crop_300.short_description = 'imagem'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'participação especial'
        verbose_name_plural = 'participações especiais'
        ordering = ('name',)


# @receiver(models.signals.post_save, sender=SpecialParticipation)
# def warm_special_participation_image(sender, instance, **kwargs):
#     """Ensures Special Participation image files are created post-save"""
#     special_participation_img_warmer = VersatileImageFieldWarmer(
#         instance_or_queryset=instance,
#         rendition_key_set='special_participation',
#         image_attr='image'
#     )
#     special_participation_img_warmer.warm()
#
#
# @receiver(models.signals.post_delete, sender=SpecialParticipation)
# def delete_special_participation_files(sender, instance, **kwargs):
#     """
#     Deletes Special Participation file renditions on post_delete.
#     """
#     # Deletes Image Renditions
#     instance.image.delete_all_created_images()
#     # Deletes Original Image
#     instance.image.delete(save=False)


# def photo_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/photos/<instance.title>-<PK>
#     ext = filename.split('.')[-1]
#     return 'photos/{0}-{1}.{2}'.format(slugify(instance.title), instance.id, ext)


class Photo(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    # image = VersatileImageField('imagem', upload_to=photo_directory_path)
    image = CloudinaryField('imagem')

    def image_thumbnail_300(self):
        return format_html(self.image.image(width=300, height=300, crop="thumb"))

    image_thumbnail_300.allow_tags = True
    image_thumbnail_300.short_description = 'imagem'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'
        ordering = ('title',)


# @receiver(models.signals.post_save, sender=Photo)
# def warm_photo_image(sender, instance, **kwargs):
#     """Ensures Photo image files are created post-save"""
#     photo_img_warmer = VersatileImageFieldWarmer(
#         instance_or_queryset=instance,
#         rendition_key_set='photo',
#         image_attr='image'
#     )
#     photo_img_warmer.warm()
#
#
# @receiver(models.signals.post_delete, sender=Photo)
# def delete_photo_files(sender, instance, **kwargs):
#     """
#     Deletes Photo file renditions on post_delete.
#     """
#     # Deletes Image Renditions
#     instance.image.delete_all_created_images()
#     # Deletes Original Image
#     instance.image.delete(save=False)


class PlayList(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    code = models.CharField('código', max_length=60, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Video(models.Model):
    title = models.CharField('título', max_length=250)
    code = models.CharField('código', max_length=60, unique=True)
    play_list = models.ForeignKey('PlayList', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    logo = CloudinaryField('logotipo', null=True, blank=True, help_text='Imagem com: 350 X 350 pixels')
    # players = models.ManyToManyField('Player', verbose_name='jogadores')

    def logo_fill_350(self):
        return format_html(self.logo.image(width=350, height=350, crop="fill"))

    logo_fill_350.allow_tags = True
    logo_fill_350.short_description = 'logotipo'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'time'
        verbose_name_plural = 'times'
        ordering = ('name',)


class Player(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'jogador'
        verbose_name_plural = 'jogadores'
        ordering = ('name',)


class Circuit(models.Model):
    description = models.CharField('descrição', max_length=250, unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'circuito'
        verbose_name_plural = 'circuitos'
        ordering = ('description',)


class Tournament(models.Model):
    description = models.CharField('descrição', max_length=250, unique=True)
    circuit = models.ForeignKey('Circuit', on_delete=models.PROTECT, verbose_name='circuito')
    players = models.ManyToManyField('Player', through='Ranking')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'torneio'
        verbose_name_plural = 'torneios'
        ordering = ('description',)


class Ranking(models.Model):
    player = models.ForeignKey('Player', on_delete=models.PROTECT)
    tournament = models.ForeignKey('Tournament', on_delete=models.PROTECT)
    position = models.PositiveIntegerField('posição')

    def __str__(self):
        return str(self.player)

    class Meta:
        verbose_name = 'classificação'
        verbose_name_plural = 'classificações'
        ordering = ('tournament', 'position')
        unique_together = ('tournament', 'position')
