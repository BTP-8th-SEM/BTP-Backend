class OptionsInfoException(Exception):
    ...


class OptionsInfoNotFoundError(OptionsInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Options Info Not Found"

