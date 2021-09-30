from ..basic_client.client import CalendlyClient
from .objects import User


class CalendlyEnhancedClient(CalendlyClient):
    async def get_current_user(self):
        response = await super().get_current_user()
        current_user = response['resource']
        return User.create_from_dict(self, current_user)