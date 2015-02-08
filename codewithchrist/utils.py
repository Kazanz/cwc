def ip_from_request(request):
    """Returns string of clients IP Adress."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    x_real_ip = request.META.get('HTTP_X_REAL_IP')
    remote_addr = request.META.get('REMOTE_ADDR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    elif x_real_ip:
        ip = x_real_ip
    else:
        ip = remote_addr
    return ip
