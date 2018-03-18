from django.contrib import admin

from vivalviar.core.models import Banner, Sponsor, SpecialParticipation, Photo, PlayList, Video, Player, Team, Circuit, \
    Tournament, Ranking


admin.site.site_header = 'Vivalviar Poker'
admin.site.site_title = 'Vivalviar'
admin.site.index_title = 'Início'


class CustomModelAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(Banner)
class BannerModelAdmin(CustomModelAdmin):
    list_display = ('title', 'image_thumbnail_300')


@admin.register(Sponsor)
class SponsorModelAdmin(CustomModelAdmin):
    list_display = ('name', 'logo_thumbnail_350')


@admin.register(SpecialParticipation)
class SpecialParticipationModelAdmin(CustomModelAdmin):
    list_display = ('name', 'image_crop_300')


@admin.register(Photo)
class PhotoModelAdmin(CustomModelAdmin):
    list_display = ('title', 'image_thumbnail_300')


class VideoInline(admin.TabularInline):
    model = Video


@admin.register(PlayList)
class PlayListModelAdmin(CustomModelAdmin):
    list_display = ('title', 'code')
    inlines = [
        VideoInline,
    ]


@admin.register(Player)
class PlayerModelAdmin(CustomModelAdmin):
    list_display = ('name', 'team')
    search_fields = ('name', 'team')


@admin.register(Team)
class TeamModelAdmin(CustomModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Circuit)
class CircuitModelAdmin(CustomModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


class RankingInline(admin.TabularInline):
    model = Ranking


@admin.register(Tournament)
class TournamentModelAdmin(CustomModelAdmin):
    inlines = (RankingInline,)
