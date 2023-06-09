from django import template
import datetime

register = template.Library()

# from network.models import *

@register.filter
def make_range(b, a=0):
    new = list(range(int(a),int(b)))
    return new

@register.filter
def get_time(date):
    n = datetime.datetime.now()
    y = n.year - date.year

    if y == 0:
        m = n.month - date.month
        if m == 0:
            d = n.day - date.day
            if d == 0:
                h = n.hour - date.hour
                if h == 0:
                    mn = n.minute - date.minute
                    if mn == 0:
                        s = n.second - date.second
                        return f"{s} seconds"
                    else:
                        return f"{mn} min"
                else:
                    if h == 1:
                        return f"{h} hour ago"
                    else:
                        return f"{h} hours ago"
            else:
                if d == 1:
                    return f"{d} day ago"
                else: 
                    return f"{d} days ago"
        else:
            return f"{m} month"
    return date.strftime("%d/%m/%Y")