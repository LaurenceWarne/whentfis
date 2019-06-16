import datetime
from unittest import TestCase

from whentfis.scripts.whentfis import DayRelationEvaluator


class TestWhentfis(TestCase):

    def setUp(self):
        self.day_relator = DayRelationEvaluator(
            datetime.date(day=19, month=6, year=2019)
        )

    def test_get_rational_date_returns_today_on_same_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date
        )
        self.assertEqual(
            self.day_relator.same_day_fstring,
            relation
        )

    def test_get_rational_date_returns_tomorrow_on_next_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=1)
        )
        self.assertEqual(
            self.day_relator.day_after_fstring,
            relation
        )

    def test_get_rational_date_returns_yesterday_on_prev_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=-1)
        )
        self.assertEqual(
            self.day_relator.day_before_fstring,
            relation
        )

    def test_get_rational_date_returns_this_on_day_later_in_current_week(self):
        # I know this is a saturday
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=3)
        )
        self.assertEqual(
            self.day_relator.later_this_week_fstring.format("Saturday"),
            relation
        )
