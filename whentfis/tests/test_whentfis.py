import datetime
from unittest import TestCase

from whentfis.scripts.whentfis import get_rational_date


class TestWhentfis(TestCase):

    def test_get_rational_date_returns_today_on_same_day(self):
        day = datetime.date(day=21, month=10, year=2010)
        self.assertEqual("That's today!", get_rational_date(day, day))

    def test_get_rational_date_returns_tomorrow_on_next_day(self):
        day_from = datetime.date(day=21, month=1, year=2010)
        next_day = datetime.date(day=22, month=1, year=2010)
        self.assertEqual(
            "That's tommorrow!",
            get_rational_date(day_from, next_day)
        )

    def test_get_rational_date_returns_yesterday_on_prev_day(self):
        day_from = datetime.date(day=21, month=1, year=2010)
        prev_day = datetime.date(day=20, month=1, year=2010)
        self.assertEqual(
            "That was yesterday!",
            get_rational_date(day_from, prev_day)
        )
