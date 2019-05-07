"""Utils module."""
from datetime import datetime


def date2str(value):
    """Return the current date as a string formatted as DD/MM/YYYY."""
    return value.strftime("%d/%m/%Y") if value else None


def str2date(value):
    """Convert a given string to datetime object."""
    return datetime.strptime(value, "%d %b %Y")
