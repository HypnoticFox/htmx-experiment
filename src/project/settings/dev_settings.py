import socket

DEBUG = True

# Additional Settings

STAFF_EMAIL_DOMAIN = "example.com"
STAFF_GROUP_NAME = "example"

# Django Debug Toolbar settings
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True
}