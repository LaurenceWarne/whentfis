#!/usr/bin/env python3

import argparse
import calendar
import datetime

from dateutil.parser import parse


class DayRelationEvaluator:

    def __init__(self, base_date):
        self.base_date = base_date
        if not isinstance(self.base_date, datetime.date):
            raise TypeError(
                """Expected instance of datetime.date for
                   base_date but got: """ + type(base_date)
            )
        # Default format strings
        self.same_day_fstring = "That's today!"
        self.day_after_fstring = "That's tomorrow!"
        self.day_before_fstring = "That was yeserday!"
        self.later_this_week_fstring = "This {}"
        self.earlier_this_week_fstring = "It was this {}"
        self.day_last_week_fstring = "It was last {}"
        self.day_next_week_fstring = "Next {}"
        self.generic_future_week_fstring = "{} weeks {}"
        self.generic_past_week_fstring = "{} weeks ago {}"

    def relation_with(self, date):
        # A little validation
        if not isinstance(date, datetime.date):
            raise TypeError(
                """Expected instance of datetime.date for date but
                   got: """ + str(type(date))
            )
        days_into_week = datetime.timedelta(days=self.base_date.weekday())
        week_start = self.base_date - days_into_week
        day_difference = (date - week_start).days
        # Rounds down, even for negatives
        week = day_difference // 7
        # calendar module's weeks start on monday
        day_of_week = calendar.day_name[date.weekday()]

        # Today
        if date == self.base_date:
            return self.same_day_fstring
        # Tomorrow
        elif date + datetime.timedelta(days=-1) == self.base_date:
            return self.day_after_fstring
        # Yesterday
        elif date + datetime.timedelta(days=1) == self.base_date:
            return self.day_before_fstring
        # A day later this week
        elif week == 0 and date > self.base_date:
            return self.later_this_week_fstring.format(day_of_week)
        # A day earlier this week
        elif week == 0 and date < self.base_date:
            return self.earlier_this_week_fstring.format(day_of_week)
        # Some day next week
        elif week == 1:
            return self.day_next_week_fstring.format(day_of_week)
        # A day last week
        elif week == -1 and date.weekday() > self.base_date.weekday():
            return self.day_last_week_fstring.format(day_of_week)
        # A day further forward than next week
        elif week > 1:
            return self.generic_future_week_fstring.format(
                week,
                day_of_week
            )
        # A day further behind than last week
        else:
            return self.generic_past_week_fstring.format(
                abs(week),
                day_of_week
            )


def main():
    # Set up argparse
    description = """Transforms dates in the form dd/mm/yyyy or mm/dd/yyy to
                     a human readable format."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("date", help="Date you want to rationalise")
    args = parser.parse_args()

    # Attempt to parse date
    try:
        # For the rules of day, month, year ordering for dateutil.parse() see:
        # https://labix.org/python-dateutil#head-c0e81a473b647dfa787dc11e8c69557ec2c3ecd2
        input_datetime = parse(args.date, dayfirst=True, yearfirst=False)
        # We need to call date() as parse returns a datetime.datetime obj not a
        # datetime.date obj
        input_date = input_datetime.date()
    except ValueError:
        print("Cannot guess date format for: " + args.date)
        return
    day_relator = DayRelationEvaluator(datetime.date.today())
    print(day_relator.relation_with(input_date))


if __name__ == "__main__":
    main()
