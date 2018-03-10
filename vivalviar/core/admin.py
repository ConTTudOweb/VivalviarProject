from django.contrib import admin

from vivalviar.core.models import Banner, Sponsor, SpecialParticipation, Photo, PlayList, Video


@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail_300')


@admin.register(Sponsor)
class SponsorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_thumbnail_350')


@admin.register(SpecialParticipation)
class SpecialParticipationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_crop_300')


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail_300')


class VideoInline(admin.TabularInline):
    model = Video


@admin.register(PlayList)
class PlayListModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    inlines = [
        VideoInline,
    ]
