# utils.py

import datetime

def parse_date(date_str):
    """Convert string YYYY-MM-DD to datetime.date"""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def format_date(date_obj):
    """Format datetime.date to string YYYY-MM-DD"""
    if date_obj:
        return date_obj.strftime("%Y-%m-%d")
    return None
