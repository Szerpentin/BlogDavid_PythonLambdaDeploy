import datetime

def handler(event, context) -> str:
    dt = datetime.datetime.now(datetime.timezone.utc)
    utc_time = dt.replace(tzinfo=datetime.timezone.utc)

    return str(utc_time)