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
        'updated_at': 'datetime',
        'current_organization': ''
    }

    @property
    def current_organization(self):
        return self._current_organization

    @current_organization.setter
    def current_organization(self, value):
        from .organization import Organization
        self._current_organization = value
        self.Organization = Organization(self.client, value)
