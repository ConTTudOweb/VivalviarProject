from django.db.models import QuerySet, Sum, Case, When, Value, IntegerField
from sqlparse import split


class RankingQuerySet(QuerySet):
    def base(self):
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
        return self.values('player__name', 'player__country').base().order_by('-player_position_1st',
                                                                              '-player_position_2nd',
                                                                              '-player_position_3rd',
                                                                              'player__name')

    def champions_team(self):
        return self.values('player__team__name', 'player__team__logo')\
            .filter(player__team__isnull=False)\
            .base()\
            .order_by('-player_position_1st', '-player_position_2nd', '-player_position_3rd',
                      'player__team__name', 'player__team__logo')
