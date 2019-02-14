# coding: UTF-8


def is_valid_ip(ip_string):
    result = False

    ip_octets = ip_string.split('.')

    if len(ip_octets) != 4:
        return result

    for ip_octet in ip_octets:
        if not ip_octet.isdigit():
            return result

        if len(ip_octet) > 1 and not int(ip_octet[0]):
            return result

        if int(ip_octet) > 255:
            return result

    result = True
    return result
