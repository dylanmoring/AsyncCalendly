class CalendlyObject:
    fields = {}

    def __init__(self, client, uri):
        self.client = client
        self.uri = uri

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.uuid}'

    @property
    def uuid(self):
        return self.uri.split('/')[-1]

    def update_from_dict(self, update_dict):
        for field_name, transform in self.fields.items():
            value = update_dict.get(field_name, None)
            setattr(self, field_name, value)

    @classmethod
    def create_from_dict(cls, client, update_dict):
        new_object = cls(client, update_dict['uri'])
        new_object.update_from_dict(update_dict)
        return new_object