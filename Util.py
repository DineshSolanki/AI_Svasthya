from easysettings import EasySettings

settings = EasySettings("config.conf")


def set_timeout(timeout=15):
    settings.setsave("timeout", timeout)


def set_blink_monitoring(is_enabled=False):
    settings.setsave("blink-monitoring", is_enabled)


def set_screen_rest_monitoring(is_enabled=True):
    settings.setsave("rest-monitoring", is_enabled)


def set_notification_enabled(is_enabled=True):
    settings.setsave("notification-enabled", is_enabled)


def set_smart_notification():
    pass


def get_timeout():
    return settings.get("timeout")


def get_blink_monitoring():
    return settings.get("blink-monitoring")


def get_screen_rest_monitoring():
    return settings.get("rest-monitoring")


def get_notification_enabled():
    return settings.get("notification-enabled")


def get_smart_notification():
    return False
