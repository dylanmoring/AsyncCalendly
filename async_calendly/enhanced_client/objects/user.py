from .base_object import CalendlyObject


class User(CalendlyObject):
    fields = {
        'uri': '',
        'name': '',
        'slug': '',
        'email': '',
        'scheduling_url': '',
        'timezone': '',
        'avatar_url': '',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }