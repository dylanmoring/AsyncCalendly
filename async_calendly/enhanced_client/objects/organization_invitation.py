from .base_object import CalendlyObject


class OrganizationInvitation(CalendlyObject):
    fields = {
        'created_at': 'datetime',
        'email': '',
        'last_sent_at': 'datetime',
        'organization': '',
        'status': '',
        'updated_at': 'datetime',
        'uri': '',
        'user': ''
    }
