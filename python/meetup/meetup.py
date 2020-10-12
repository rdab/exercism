import calendar
from datetime import date


WEEKS = ["1st", "2nd", "3rd", "4th", "5th"]


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):
    cal = calendar.Calendar()
    day_of_week_index = calendar.day_name[:].index(day_of_week)
    days = [
        week[day_of_week_index]
        for week in cal.monthdayscalendar(year, month)
        if week[day_of_week_index] != 0
    ]
    if week == "teenth":
        day = next(day for day in days if day > 12)

    elif week == "last":
        day = days[-1]

    else:
        try:
            day = days[WEEKS.index(week)]
        except IndexError:
            raise MeetupDayException(f"'{year} {month}' doesnt have a {week} week")

    return date(year, month, day)
