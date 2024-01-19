def format_time(time):
    return ':'.join(str(time).split(':')[0:2])

def get_session(request):
    ssid = request.COOKIES.get("session_id")

    if ssid is None:
        ssid = request.headers.get("authorization")

    return ssid