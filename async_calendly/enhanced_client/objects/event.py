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

    async def list_event_invitees(self, email=None, status=None, per_page=50, max_pages=100):
        return await self.client.list_event_invitees(
            uuid=self.uuid, email=email, status=status, count=per_page, max_pages=max_pages
        )

