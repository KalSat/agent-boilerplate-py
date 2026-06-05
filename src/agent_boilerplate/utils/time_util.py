from datetime import datetime


def now_str(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Returns the current local datetime as a formatted string."""
    return datetime.now().strftime(fmt)
