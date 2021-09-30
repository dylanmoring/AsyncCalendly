from ..exceptions import CalendlyException


class RequestException(CalendlyException):
    pass


class UserOrOrgRequired(RequestException):
    def __init__(self):
        super().__init__('Either an Organization or User URI must be specified.')
