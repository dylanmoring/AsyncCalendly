from .base_object import CalendlyObject


class Organization(CalendlyObject):
    fields = {
        'uri': ''
    }

    async def list_event_types(self, per_page=50, max_pages=100):
        return await self.client.list_event_types(organization=self.uri, count=per_page, max_pages=max_pages)

    async def list_events(
            self, invitee_email=None, max_start_time=None, min_start_time=None, status=None, per_page=50, max_pages=100
    ):
        return await self.client.list_events(
            organization=self.uri, invitee_email=invitee_email, max_start_time=max_start_time,
            min_start_time=min_start_time, status=status, count=per_page, max_pages=max_pages
        )

