class QuestionInfoException(Exception):
    ...


class AnswerInfoNotFoundError(QuestionInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Question Info Not Found"

