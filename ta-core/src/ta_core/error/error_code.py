from enum import IntEnum


class ErrorCode(IntEnum):
    ENVIRONMENT_VARIABLE_NOT_SET = 1

    SMTP_ERROR = 11

    USERNAME_OR_EMAIL_ALREADY_REGISTERED = 1001
    ACCOUNT_NOT_FOUND = 1002
    USERNAME_NOT_EXIST = 1003
    PASSWORD_INCORRECT = 1004
    REFRESH_TOKEN_INVALID = 1005

    EMAIL_NOT_REGISTERED = 2001
    EMAIL_ALREADY_VERIFIED = 2002

    VERIFICATION_TOKEN_NOT_EXIST = 3001
    VERIFICATION_TOKEN_INVALID = 3002
    VERIFICATION_TOKEN_EXPIRED = 3003

    EVENT_NOT_FOUND = 4001
    EVENT_NOT_ATTENDABLE = 4002
    EVENT_NOT_LEAVEABLE = 4003

    ML_SERVER_ERROR = 5001
    ML_SERVER_TIMEOUT = 5002
