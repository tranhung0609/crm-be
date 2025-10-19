import datetime

def get_timestamp_utc():
    ts = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
    return ts

def is_blank(chars: str):
    return not (chars and chars.strip())