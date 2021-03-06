import itertools

from django.http import JsonResponse
from django.views.generic import TemplateView, DetailView, ListView

from .models import Banner, Sponsor, SpecialParticipation, Photo, PlayList, Ranking, Circuit, Player


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['banner_list'] = Banner.objects.all()
        context['sponsor_list'] = Sponsor.objects.all()
        return context


home = HomePageView.as_view()

history = TemplateView.as_view(
    template_name="history.html"
)


class SpecialParticipationPageView(TemplateView):
    template_name = "special_participation.html"

    def get_context_data(self, **kwargs):
        context = super(SpecialParticipationPageView, self).get_context_data(**kwargs)
        context['special_participation_list'] = SpecialParticipation.objects.all()
        return context


special_participation = SpecialParticipationPageView.as_view()


class PhotosPageView(TemplateView):
    template_name = "photos.html"

    def get_context_data(self, **kwargs):
        context = super(PhotosPageView, self).get_context_data(**kwargs)
        context['photo_list'] = Photo.objects.all()
        return context


photos = PhotosPageView.as_view()


class PlayListPageView(TemplateView):
    template_name = "videos.html"

    def get_context_data(self, **kwargs):
        context = super(PlayListPageView, self).get_context_data(**kwargs)
        context['playlist_list'] = PlayList.objects.all()
        return context


playlist = PlayListPageView.as_view()

contact_us = TemplateView.as_view(
    template_name="contact_us.html"
)


# TODO: Falta todos os campos necessários
def get_player_stats(request):
    player__pk = request.GET.get('pk', None)
    data = {
        'name': Player.objects.get(pk=player__pk).name,
        'tournament_count': Ranking.objects.filter(player__pk=player__pk).count()
    }
    return JsonResponse(data)


class ChampionsPageView(TemplateView):
    template_name = "champions_individual.html"

    def get_context_data(self, **kwargs):
        context = super(ChampionsPageView, self).get_context_data(**kwargs)
        # ranking_first_list = Ranking.objects.filter(position__lte=3)\
        #     .values('player__name', 'player__country') \
        #     .annotate(
        #         player_position_1st=Sum(
        #             Case(
        #                 When(position=1, then=Value(1)),
        #                 default=Value(0),
        #                 output_field=IntegerField(),
        #             )
        #         ),
        #         player_position_2nd=Sum(
        #             Case(
        #                 When(position=2, then=Value(1)),
        #                 default=Value(0),
        #                 output_field=IntegerField(),
        #             )
        #         ),
        #         player_position_3rd=Sum(
        #             Case(
        #                 When(position=3, then=Value(1)),
        #                 default=Value(0),
        #                 output_field=IntegerField(),
        #             )
        #         ),
        #         player_position_total=Sum(
        #             Case(
        #                 When(position__lte=3, then=Value(1)),
        #                 default=Value(0),
        #                 output_field=IntegerField(),
        #             )
        #         ),
        #     ) \
        #     .order_by('-player_position_1st', '-player_position_2nd', '-player_position_3rd', 'player__name')
        ranking_list = Ranking.objects.champions_individual()
        context['ranking_list'] = ranking_list
        return context


champions = ChampionsPageView.as_view()


class ChampionsTeamPageView(TemplateView):
    template_name = "champions_team.html"

    def get_context_data(self, **kwargs):
        context = super(ChampionsTeamPageView, self).get_context_data(**kwargs)
        ranking_list = Ranking.objects.champions_team()
        context['ranking_list'] = ranking_list
        return context


champions_team = ChampionsTeamPageView.as_view()


class CircuitDetailView(DetailView):
    model = Circuit


class CircuitListView(ListView):
    model = Circuit


class BestYearPageView(TemplateView):
    template_name = "best_year.html"

    def get_context_data(self, **kwargs):
        context = super(BestYearPageView, self).get_context_data(**kwargs)
        ranking_list = []
        for circuit in Circuit.objects.all():
            ranking_list += circuit.players_list

        ranking_list = sorted(ranking_list, key=lambda k: k['player__name'])

        grouped = itertools.groupby(ranking_list, lambda d: d.get('player__name'))
        ranking_list = [{'player__name': label,
                         'points': int(sum([x['points'] for x in value])),
                         }
                        for label, value in grouped]

        context['ranking_list'] = ranking_list
        return context
