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
        # If value is unchanged, don't update it
        if getattr(self, '_current_organization', None) == value:
            return
        from .organization import Organization
        self._current_organization = value
        self.Organization = Organization(self.client, value)

    async def get(self):
        update_dict = await self.client.get_user(self.uuid)
        self.update_from_dict(update_dict)

    async def list_event_types(self, per_page=50, max_pages=100):
        return await self.client.list_event_types(user=self.uri, count=per_page, max_pages=max_pages)

    async def list_events(
            self, invitee_email=None, max_start_time=None, min_start_time=None, status=None, per_page=50, max_pages=100
    ):
        return await self.client.list_events(
            user=self.uri, invitee_email=invitee_email, max_start_time=max_start_time,
            min_start_time=min_start_time, status=status, count=per_page, max_pages=max_pages
        )
