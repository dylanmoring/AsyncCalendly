from .base_object import CalendlyObject


class Event(CalendlyObject):
    fields = {
        'created_at': 'datetime',
        'end_time': 'datetime',
        'event_guests': '',
        'event_memberships': '',
        'event_type': '',
        'invitees_counter': '',
        'location': '',
        'name': '',
        'start_time': 'datetime',
        'status': '',
        'updated_at': 'datetime',
        'uri': ''
    }
