import re

from rest_framework.serializers import ValidationError


class LetterAndDigitValidator:

    def validate(self, password, user=None):

        if not re.search(r'\d', password):
            raise ValidationError(
                "The password must contain at least 1 digit",
                code='password_no_contain_digit',
            )

        if not re.search(r'[a-zA-Zа-яА-ЯёЁ]', password):
            raise ValidationError(
                "The password must contain at least 1 latin or russian letter",
                code='password_no_contain_letter',
            )
