class UserInfoException(Exception):
    ...


class UserInfoNotFoundError(UserInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "User Info Not Found"


class UserInfoInfoAlreadyExistError(UserInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "User Info Already Exists"
