import re
from utils.exceptions import ValidationError

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

class Validator:
    @staticmethod
    def validate_email(email: str) -> str:
        """يتحقق من صحة صيغة البريد الإلكتروني."""
        if not isinstance(email, str) or not re.match(EMAIL_REGEX, email.strip()):
            raise ValidationError(f"Invalid email address: '{email}'")
        return email.strip().lower()

    @staticmethod
    def validate_rating_score(score: float) -> float:
        """يتحقق من أن التقييم قيمته بين 1 و 10."""
        if not isinstance(score, (int, float)) or not (1 <= score <= 10):
            raise ValidationError(f"Rating score must be between 1 and 10. Got: {score}")
        return float(score)

    @staticmethod
    def validate_non_negative_int(value: int, field_name: str) -> int:
        """يتحقق من أن العدد الصحيح غير سلبى (مثل عدد النسخ المتاحة)."""
        if not isinstance(value, int) or value < 0:
            raise ValidationError(f"{field_name} must be a non-negative integer. Got: {value}")
        return value