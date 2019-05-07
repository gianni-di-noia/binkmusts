"""Utils module."""
import string
from datetime import datetime
from difflib import get_close_matches

pool_name = list()


def date2str(value):
    """Return the current date as a string formatted as DD/MM/YYYY."""
    return value.strftime("%d/%m/%Y") if value else None


def str2date(value):
    """Convert a given string to datetime object."""
    return datetime.strptime(value, "%d %b %Y")


def clean_tenant_name(name):
    """Cleanup the name of tenant."""
    name = "".join(c for c in name if c not in string.punctuation)
    existing = get_close_matches(name, pool_name, 1, 0.8)
    if existing:
        return existing[0]
    pool_name.append(name)
    return name
