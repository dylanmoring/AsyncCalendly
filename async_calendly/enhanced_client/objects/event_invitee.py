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
