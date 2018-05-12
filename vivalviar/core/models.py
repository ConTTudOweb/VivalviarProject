import itertools
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models import Sum, Case, When, Value, IntegerField, Count, Q, F, PositiveIntegerField, Avg
from django.utils.html import format_html
from django_countries.fields import CountryField


class Banner(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
    image = CloudinaryField('imagem', help_text='Imagem com: 873 X 1280 pixels')

    def image_thumbnail_300(self):
        return format_html(self.image.image(width=300, height=300, crop="thumb"))

    image_thumbnail_300.allow_tags = True
    image_thumbnail_300.short_description = 'imagem'

    def __str__(self):
        return self.title


class Sponsor(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
    link = models.CharField(max_length=250)
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


class SpecialParticipation(models.Model):
    name = models.CharField('nome', max_length=250, unique=True)
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


class Photo(models.Model):
    title = models.CharField('título', max_length=250, unique=True)
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
    team = models.ForeignKey('Team', verbose_name=Team._meta.verbose_name, on_delete=models.SET_NULL, null=True,
                             blank=True)
    country = CountryField('país', default='BR')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'jogador'
        verbose_name_plural = 'jogadores'
        ordering = ('name',)


class Circuit(models.Model):
    description = models.CharField('descrição', max_length=250, unique=True)

    @property
    def players_list(self):
        qs = Ranking.objects.filter(tournament__in=self.tournament_set.all()) \
            .values('player__name', 'tournament') \
            .annotate(
            points=
            (
                (
                    Count('tournament__ranking__id', output_field=IntegerField())
                    - Avg('position', output_field=IntegerField())
                    + 1
                ) * 10
            ) +
            Case(
                When(position=1, then=Value(15)),
                When(position=2, then=Value(5)),
                default=Value(0),
                output_field=IntegerField(),
            ),

        ).order_by('player__name')

        grouped = itertools.groupby(qs, lambda d: d.get('player__name'))

        players_list = [{'player__name': label,
                         'points': int(sum([x['points'] for x in value])),
                         }
                        for label, value in grouped]

        return players_list

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'circuito'
        verbose_name_plural = 'circuitos'
        ordering = ('description',)


class Tournament(models.Model):
    description = models.CharField('descrição', max_length=250, unique=True)
    circuit = models.ForeignKey('Circuit', on_delete=models.SET_NULL, verbose_name='circuito', null=True, blank=True)
    players = models.ManyToManyField('Player', through='Ranking')
    date = models.DateField('data', null=True, blank=True)
    PRESENTIAL = 'P'
    ONLINE = 'O'
    TYPE_CHOICES = (
        (ONLINE, 'Online'),
        (PRESENTIAL, 'Presencial'),
    )
    type = models.CharField(
        'tipo',
        max_length=1,
        choices=TYPE_CHOICES,
        default=ONLINE,
    )

    @property
    def players_count(self):
        return self.players.count()

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
