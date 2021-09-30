from .base_object import CalendlyObject


class WebhookSubscription(CalendlyObject):
    fields = {
        'callback_url': '',
        'created_at': 'datetime',
        'creator': '',
        'events': '',
        'organization': '',
        'retry_started_at': 'datetime',
        'scope': '',
        'state': '',
        'updated_at': 'datetime',
        'uri': '',
        'user': ''
    }
