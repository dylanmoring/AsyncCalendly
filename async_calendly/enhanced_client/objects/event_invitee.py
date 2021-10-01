from .base_object import CalendlyObject


class EventInvitee(CalendlyObject):
    fields = {
        'cancel_url': '',
        'canceled': '',
        'created_at': 'datetime',
        'email': '',
        'event': '',
        'first_name': '',
        'last_name': '',
        'name': '',
        'new_invitee': '',
        'old_invitee': '',
        'payment': '',
        'questions_and_answers': '',
        'reschedule_url': '',
        'rescheduled': '',
        'status': '',
        'text_reminder_number': '',
        'timezone': '',
        'tracking': '',
        'updated_at': 'datetime',
        'uri': ''
    }

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value):
        # If value is unchanged, don't update it
        if getattr(self, '_event', None) == value:
            return
        from .event import Event
        self._event = value
        self.Event = Event(self.client, value)
