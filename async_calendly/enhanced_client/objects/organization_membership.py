from .base_object import CalendlyObject


class OrganizationMembership(CalendlyObject):
    fields = {
        'created_at': 'datetime',
        'organization': '',
        'role': '',
        'updated_at': 'datetime',
        'uri': '',
        'user': ''
    }
