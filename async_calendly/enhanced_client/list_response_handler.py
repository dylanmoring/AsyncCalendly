class ListResponseHandler:
    def __init__(self, client, response_dict, max_page=50):
        self.client = client
        self.current_page = 1
        self.max_page = max_page
        self.result_list = []
        self.next_page = None
        self.handle_response(response_dict)

    def __aiter__(self):
        return self

    async def __anext__(self):
        # If max page has been reached, or no pages are left, stop here
        if self.current_page >= self.max_page or not self.next_page:
            raise StopAsyncIteration
        self.current_page += 1
        # Get path to pass to client _request
        next_page_path = self.next_page.split('api.calendly.com/')[-1]
        # Get next page
        response_dict = await self.client._request('GET', next_page_path)
        self.handle_response(response_dict)

    def handle_response(self, response_dict):
        self.result_list.extend(response_dict['collection'])
        self.next_page = response_dict['pagination']['next_page']

    async def get_all(self):
        async for page in self:
            # Do nothing since all heavy lifting done within iteration
            pass
        return self.result_list

    @classmethod
    async def get_all_for_list_response(cls, client, response_dict, max_page=50):
        self = cls(client, response_dict, max_page)
        return await self.get_all()
