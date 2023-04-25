class TestException(Exception):
    ...


class TestNotFoundError(TestException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Test Info Not Found"