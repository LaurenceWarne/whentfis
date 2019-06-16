import datetime
from unittest import TestCase

from whentfis.scripts.whentfis import DayRelationEvaluator


class TestWhentfis(TestCase):

    def setUp(self):
        self.day_relator = DayRelationEvaluator(
            datetime.date(day=19, month=6, year=2019)
        )

    def test_init_only_accepts_datetime_objs(self):
        self.assertRaises(
            TypeError,
            lambda date: DayRelationEvaluator(date),
            "Not a datetime obj"
        )

    def test_relation_with_raises_exception_on_invalid_date_obj(self):
        self.assertRaises(
            TypeError,
            self.day_relator.relation_with,
            "Not a datetime obj"
        )

    def test_relation_with_returns_today_on_same_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date
        )
        self.assertEqual(
            self.day_relator.same_day_fstring,
            relation
        )

    def test_relation_with_returns_tomorrow_on_next_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=1)
        )
        self.assertEqual(
            self.day_relator.day_after_fstring,
            relation
        )

    def test_relation_with_returns_yesterday_on_prev_day(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=-1)
        )
        self.assertEqual(
            self.day_relator.day_before_fstring,
            relation
        )

    def test_relation_with_returns_correct_string_on_day_later_in_current_week(self):
        # I know this is a saturday
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=3)
        )
        self.assertEqual(
            self.day_relator.later_this_week_fstring.format("Saturday"),
            relation
        )

    def test_relation_with_returns_correct_string_on_day_earlier_in_current_week(self):
        # I know this is a monday
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=-2)
        )
        self.assertEqual(
            self.day_relator.earlier_this_week_fstring.format("Monday"),
            relation
        )

    def test_relation_with_returns_correct_string_on_day_next_week(self):
        # I know this is a Tuesday
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=6)
        )
        self.assertEqual(
            self.day_relator.day_next_week_fstring.format("Tuesday"),
            relation
        )

    def test_relation_with_returns_correct_string_on_day_last_week(self):
        # I know this is a Sunday
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=-3)
        )
        self.assertEqual(
            self.day_relator.day_last_week_fstring.format("Sunday"),
            relation
        )

    def test_relation_with_returns_correct_string_on_day_in_2_weeks(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=15)
        )
        self.assertEqual(
            self.day_relator.generic_future_week_fstring.format(2, "Thursday"),
            relation
        )

    def test_relation_with_returns_correct_string_on_day_2_weeks_ago(self):
        relation = self.day_relator.relation_with(
            self.day_relator.base_date + datetime.timedelta(days=-16)
        )
        self.assertEqual(
            self.day_relator.generic_past_week_fstring.format(2, "Monday"),
            relation
        )
