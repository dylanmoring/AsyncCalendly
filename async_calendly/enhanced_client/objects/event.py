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

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        from .event_type import EventType
        self._event_type = value
        self.EventType = EventType(self.client, value)
