from django.db import models
from django.dispatch import receiver
from django.utils.html import format_html
from django.utils.text import slugify
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer


def banner_directory_path(instance, _):
    # file will be uploaded to MEDIA_ROOT/banners/<filename>
    return 'banners/{0}'.format(slugify(instance.title))


class Banner(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    image = VersatileImageField('imagem', upload_to=banner_directory_path,
                                help_text='Imagem com: 800 X 800 pixels')

    def image_thumbnail_300(self):
        return format_html('<img src="{}"/>',
                           self.image.thumbnail['300x300'].url)

    image_thumbnail_300.allow_tags = True
    image_thumbnail_300.short_description = 'imagem'

    def __str__(self):
        return self.title


@receiver(models.signals.post_save, sender=Banner)
def warm_Banner_image(sender, instance, **kwargs):
    """Ensures Banner image files are created post-save"""
    banner_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='banner',
        image_attr='image'
    )
    banner_img_warmer.warm()


@receiver(models.signals.post_delete, sender=Banner)
def delete_Banner_files(sender, instance, **kwargs):
    """
    Deletes Banner file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.image.delete_all_created_images()
    # Deletes Original Image
    instance.image.delete(save=False)


def sponsor_directory_path(instance, _):
    # file will be uploaded to MEDIA_ROOT/sponsors/<filename>
    return 'sponsors/{0}'.format(slugify(instance.name))


class Sponsor(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    link = models.CharField(max_length=250)
    logo = VersatileImageField('logotipo', upload_to=sponsor_directory_path, help_text='Imagem com: 350 X 350 pixels')
    position = models.IntegerField('posição', default=0)

    def logo_thumbnail_350(self):
        return format_html('<img src="{}"/>',
                           self.logo.thumbnail['350x350'].url)

    logo_thumbnail_350.allow_tags = True
    logo_thumbnail_350.short_description = 'logotipo'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'patrocinador'
        verbose_name_plural = 'patrocinadores'
        ordering = ('position', 'name')


@receiver(models.signals.post_save, sender=Sponsor)
def warm_sponsor_image(sender, instance, **kwargs):
    """Ensures Sponsor image files are created post-save"""
    sponsor_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='sponsor',
        image_attr='logo'
    )
    sponsor_img_warmer.warm()


@receiver(models.signals.post_delete, sender=Sponsor)
def delete_sponsor_file(_, instance, **kwargs):
    """
    Deletes Sponsor file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.logo.delete_all_created_images()
    # Deletes Original Image
    instance.logo.delete(save=False)


def special_participation_directory_path(instance, _):
    # file will be uploaded to MEDIA_ROOT/special_participations/<filename>
    return 'special_participations/{0}'.format(slugify(instance.name))


class SpecialParticipation(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    image = VersatileImageField('imagem', upload_to=special_participation_directory_path,
                                help_text='Imagem com: 300 X 300 pixels')
    country = models.CharField('país', max_length=255, null=True, blank=True)

    def image_crop_300(self):
        return format_html('<img src="{}"/>',
                           self.image.crop['300x300'].url)

    image_crop_300.allow_tags = True
    image_crop_300.short_description = 'imagem'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'participação especial'
        verbose_name_plural = 'participações especiais'
        ordering = ('name',)


@receiver(models.signals.post_save, sender=SpecialParticipation)
def warm_special_participation_image(sender, instance, **kwargs):
    """Ensures Special Participation image files are created post-save"""
    special_participation_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='special_participation',
        image_attr='image'
    )
    special_participation_img_warmer.warm()


@receiver(models.signals.post_delete, sender=SpecialParticipation)
def delete_special_participation_files(sender, instance, **kwargs):
    """
    Deletes Special Participation file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.image.delete_all_created_images()
    # Deletes Original Image
    instance.image.delete(save=False)


def photo_directory_path(instance, _):
    # file will be uploaded to MEDIA_ROOT/photos/<filename>-<PK>
    return 'photos/{0}-{1}'.format(slugify(instance.title), instance.id)


class Photo(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    image = VersatileImageField('imagem', upload_to=photo_directory_path)

    def image_thumbnail_300(self):
        return format_html('<img src="{}"/>',
                           self.image.thumbnail['300x300'].url)

    image_thumbnail_300.allow_tags = True
    image_thumbnail_300.short_description = 'imagem'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'
        ordering = ('title',)


@receiver(models.signals.post_save, sender=Photo)
def warm_photo_image(sender, instance, **kwargs):
    """Ensures Photo image files are created post-save"""
    photo_img_warmer = VersatileImageFieldWarmer(
        instance_or_queryset=instance,
        rendition_key_set='photo',
        image_attr='image'
    )
    photo_img_warmer.warm()


@receiver(models.signals.post_delete, sender=Photo)
def delete_photo_files(sender, instance, **kwargs):
    """
    Deletes Photo file renditions on post_delete.
    """
    # Deletes Image Renditions
    instance.image.delete_all_created_images()
    # Deletes Original Image
    instance.image.delete(save=False)


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
