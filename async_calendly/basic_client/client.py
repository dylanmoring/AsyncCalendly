import aiohttp

from .exceptions import UserOrOrgRequired


class CalendlyClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.active_requests = 0
        self.closing = False

    async def init_session(self):
        connector = aiohttp.TCPConnector()
        headers = {
            'authorization': 'Bearer ' + self.api_key
        }
        self.session = aiohttp.ClientSession(
            connector=connector,
            headers=headers
        )

    async def __aenter__(self):
        # Increment active request count
        self.active_requests += 1
        # Start a new session if one is needed
        if not hasattr(self, 'session') or self.closing or self.session.closed:
            await self.init_session()

    async def __aexit__(self, *args, **kwargs):
        # Decrement subscriber count
        self.active_requests -= 1
        # If there are no more subscribers, close the session
        if self.active_requests == 0:
            self.closing = True
            await self.session.__aexit__(*args, **kwargs)
            self.closing = False

    async def _request(self, method, path, params=None, data=None):
        url = f'https://api.calendly.com/{path}'
        # Open session if needed
        async with self:
            print('Making Request')
            response = await self.session.request(method=method, url=url, params=params, json=data)
        response_dict = await response.json()
        print('Response:', response_dict)
        return response_dict

    async def _list_request(self, path, count=None, sort=None, page_token=None, params=None):
        if params is None:
            params = {}
        if count:
            params['count'] = count
        if sort:
            params['sort'] = sort
        if page_token:
            params['page_token'] = page_token
        return await self._request('GET', path, params=params)

    # USER API Endpoints
    async def get_user(self, uuid):
        return await self._request('GET', f'users/{uuid}')

    async def get_current_user(self):
        return await self._request('GET', 'users/me')

    # EVENT TYPE API Endpoints
    async def get_event_type(self, uuid):
        return await self._request('GET', f'event_types/{uuid}')

    async def list_event_types(self, user=None, organization=None, count=None, sort=None, page_token=None):
        if not user and not organization:
            raise UserOrOrgRequired()
        params = {}
        if user:
            params['user'] = user
        if organization:
            params['organization'] = organization
        return await self._list_request('event_types', count=count, sort=sort, page_token=page_token, params=params)

    # EVENT API Endpoints
    async def get_event(self, uuid):
        return await self._request('GET', f'scheduled_events/{uuid}')

    async def list_events(self, user=None, organization=None, count=None, invitee_email=None, max_start_time=None,
                          min_start_time=None, status=None, sort=None, page_token=None):
        if not user and not organization:
            raise UserOrOrgRequired()
        params = {}
        if user:
            params['user'] = user
        if organization:
            params['organization'] = organization
        if invitee_email:
            params['invitee_email'] = invitee_email
        if max_start_time:
            params['max_start_time'] = max_start_time
        if min_start_time:
            params['min_start_time'] = min_start_time
        if status:
            params['status'] = status
        return await self._list_request(
            'scheduled_events', count=count, sort=sort, page_token=page_token, params=params
        )

    # EVENT INVITEE API Endpoints
    async def get_event_invitee(self, event_uuid, invitee_uuid):
        return await self._request('GET', f'scheduled_events/{event_uuid}/invitees/{invitee_uuid}')

    async def list_event_invitees(self, uuid, count=None, email=None, status=None, sort=None, page_token=None):
        params = {}
        if email:
            params['email'] = email
        if status:
            params['status'] = status
        return await self._list_request(
            f'scheduled_events/{uuid}/invitees', count=count, sort=sort, page_token=page_token, params=params
        )

    # SCHEDULING LINK API Endpoints
    async def create_single_use_scheduling_link(self, owner_uri, max_event_count=1, owner_type='EventType'):
        data = {
            'max_event_count': max_event_count,
            'owner': owner_uri,
            'owner_type': owner_type
        }
        return await self._request('POST', 'scheduling_links', data=data)

    # ORGANIZATION MEMBERSHIP API Endpoints
    async def get_organization_membership(self, uuid):
        return await self._request('GET', f'organization_memberships/{uuid}')

    async def remove_user_from_organization(self, uuid):
        return await self._request('DELETE', f'organization_memberships/{uuid}')

    async def list_organization_memberships(
            self, user=None, organization=None, count=None, email=None, page_token=None
    ):
        if not user and not organization:
            raise UserOrOrgRequired()
        params = {}
        if user:
            params['user'] = user
        if organization:
            params['organization'] = organization
        if email:
            params['email'] = email
        return await self._list_request('organization_memberships', count=count, page_token=page_token, params=params)

    # ORGANIZATION INVITATION API Endpoints
    async def get_organization_invitation(self, organization_uuid, invitation_uuid):
        return await self._request('GET', f'organizations/{organization_uuid}/invitations/{invitation_uuid}')

    async def invite_user_to_organization(self, organization_uuid, invitee_email_address=None):
        return await self._request('POST', f'organizations/{organization_uuid}/invitations',
                                   data={'email': invitee_email_address})

    async def revoke_organization_invitation(self, organization_uuid, invitation_uuid):
        return await self._request('DELETE', f'organizations/{organization_uuid}/invitations/{invitation_uuid}')

    async def list_organization_invitations(
            self, organization_uuid, count=None, email=None, status=None, sort=None, page_token=None
    ):
        params = {}
        if email:
            params['email'] = email
        if status:
            params['status'] = status
        return await self._list_request(
            f'organizations/{organization_uuid}/invitations',
            count=count, sort=sort, page_token=page_token, params=params
        )

    # WEBHOOK API Endpoints
    async def get_webhook_subscription(self, uuid):
        return await self._request('GET', f'webhook_subscriptions/{uuid}')

    async def create_webhook_subscription(self, url, events, organization, scope, user=None, signing_key=None):
        data = {
            'url': url,
            'events': events,
            'organization': organization,
            'user': user,
            'scope': scope,
            'signing_key': signing_key
        }
        return await self._request('POST', 'webhook_subscriptions', data=data)

    async def delete_webhook_subscription(self, uuid):
        return await self._request('DELETE', f'webhook_subscriptions/{uuid}')

    async def list_webhook_subscriptions(self, organization, scope, count=None, user=None, sort=None, page_token=None):
        params = {
            'organization': organization,
            'scope': scope
        }
        if user:
            params['user'] = user
        return await self._list_request(
            f'webhook_subscriptions', count=count, sort=sort, page_token=page_token, params=params
        )
