from .base_object import CalendlyObject


class EventType(CalendlyObject):
    fields = {
        'active': '',
        'color': '',
        'created_at': 'datetime',
        'custom_questions': '',
        'description_html': '',
        'description_plain': '',
        'duration': 'minutes',
        'internal_note': '',
        'kind': '',
        'name': '',
        'pooling_type': '',
        'profile': '',
        'scheduling_url': '',
        'secret': '',
        'slug': '',
        'type': '',
        'updated_at': 'datetime',
        'uri': ''
    }
