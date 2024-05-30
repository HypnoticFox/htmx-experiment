import os
import socket
import mimetypes

DEBUG = True

SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "OAUTH_PKCE_ENABLED": True,
        "APPS": [
            {
                "provider_id": "keycloak",
                "name": "Keycloak",
                "client_id": os.getenv("KEYCLOAK_CLIENT_ID"),
                "secret": os.getenv("KEYCLOAK_CLIENT_SECRET"),
                "settings": {
                    "server_url": os.getenv("KEYCLOAK_URL"),
                },
            }
        ]
    }
}

# Additional Settings

STAFF_EMAIL_DOMAIN = "example.com"
STAFF_GROUP_NAME = "example"

# Django Debug Toolbar settings
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_COLLAPSED": True,
    "UPDATE_ON_FETCH": True,
    "RENDER_PANELS": False,
}

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]