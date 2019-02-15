# coding: UTF-8


def is_valid_ip(ip_string):
    max_octet_amount = 4
    max_octet_value = 255

    ip_octets = ip_string.split('.')

    if len(ip_octets) != max_octet_amount:
        return False

    for ip_octet in ip_octets:
        if not ip_octet.isdigit():
            return False

        if len(ip_octet) > 1 and ip_octet.startswith('0'):
            return False

        if int(ip_octet) > max_octet_value:
            return False

    return True
