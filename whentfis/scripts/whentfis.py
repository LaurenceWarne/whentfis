#!/usr/bin/env python3

import argparse
import calendar
import datetime
import sys
from dateutil.parser import parse


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
    today = datetime.date.today()
    print(get_rational_date(input_date, today))


def get_rational_date(input_date, date_from):
    start_of_week = date_from - datetime.timedelta(days=input_date.weekday())
    day_difference = (input_date - start_of_week).days
    # Rounds down, even for negatives
    week = day_difference // 7
    # calendar module's weeks start on monday
    day_of_week = calendar.day_name[input_date.weekday()]

    # Today
    if input_date == date_from:
        return "That's today!"
    # A day later this week
    elif week == 0 and input_date > date_from:
        return "This {day}".format(week_num=week, day=day_of_week)
    # A day earlier this week
    elif week == 0 and input_date < date_from:
        return "It was this {day}".format(week_num=week, day=day_of_week)
    # Some day next week
    elif week == 1:
        return "Next {day}".format(week_num=week, day=day_of_week)
    # A day last week
    elif week == -1 and input_date.weekday() > date_from.weekday():
        return "It was this {day}".format(week_num=week, day=day_of_week)
    # A day further forward than next week
    elif week > 1:
        return "{weeks} weeks {day}".format(
            weeks=week,
            day=day_of_week
        )
    # A day further behind than last week
    else:
        return "{weeks} Weeks ago {day}".format(
            weeks=abs(week),
            day=day_of_week
        )


if __name__ == "__main__":
    main()
