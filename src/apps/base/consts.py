from enum import StrEnum


EMAIL_SUBJECT_PREFIX = "[Up-Study]"


class EmailSubject(StrEnum):
    VERIFY = "[Up-Study] Account Verification"
    RECOVERY_CODE = "[Up-Study] Recovery Code"
