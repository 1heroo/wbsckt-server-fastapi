def with_listener(mac, sequence):
    mac = mac.replace(' speaker', '')

    return mac in sequence


def is_speaker(mac):
    return 'speaker' in mac

