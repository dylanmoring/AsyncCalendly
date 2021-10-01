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

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        from .user import User
        self._user = User('')
        self._user.update_from_dict(value)
