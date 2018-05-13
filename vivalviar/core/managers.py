import itertools
from django.db.models import QuerySet, Sum, Case, When, Value, IntegerField, Count, Avg


class RankingQuerySet(QuerySet):
    def __champions_base(self):
        return self.filter(position__lte=3) \
            .annotate(
            player_position_1st=Sum(
                Case(
                    When(position=1, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ),
            player_position_2nd=Sum(
                Case(
                    When(position=2, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ),
            player_position_3rd=Sum(
                Case(
                    When(position=3, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ),
            player_position_total=Sum(
                Case(
                    When(position__lte=3, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ),
        )

    def champions_individual(self):
        return self.values('player__name', 'player__country') \
            .__champions_base() \
            .order_by('-player_position_1st',
                      '-player_position_2nd',
                      '-player_position_3rd',
                      'player__name')

    def champions_team(self):
        return self.values('player__team__name', 'player__team__logo') \
            .filter(player__team__isnull=False) \
            .__champions_base() \
            .order_by('-player_position_1st', '-player_position_2nd', '-player_position_3rd',
                      'player__team__name', 'player__team__logo')

    def __score_base(self, field):
        qs = self.values(field, 'tournament') \
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

        ).order_by(field)

        grouped = itertools.groupby(qs, lambda d: d.get(field))

        players_list = [{field: label,
                         'points': int(sum([x['points'] for x in value])),
                         }
                        for label, value in grouped]

        return players_list

    def score_players(self):
        return self.__score_base('player__name')

    def score_teams(self):
        return self.__score_base('player__team__name')
