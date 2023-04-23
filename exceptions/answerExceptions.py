class AnswerInfoException(Exception):
    ...


class AnswerInfoNotFoundError(AnswerInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Answer Info Not Found"

