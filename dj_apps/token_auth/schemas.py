from django.contrib.auth import get_user_model

from ninja import ModelSchema, Schema
from pydantic import validator

User = get_user_model()


class BaseNormalizedEmail(Schema):
    email: str

    @validator("email")
    def normalize_email(cls, value):
        """Normalize the email address to lowercase. This is not required for signup as it is done at Django validation level."""
        return value.lower()


class UserSchemaInCreate(ModelSchema):
    class Meta:
        model = User
        fields = ("title", "first_name", "last_name", "email", "password")
        extra = "forbid"


class UserSchemaInLogin(BaseNormalizedEmail, Schema):
    password: str


class UserSchemaOut(Schema):
    sid: str
    email: str
    api_token_key: str


class UserProfileOut(ModelSchema):
    class Meta:
        model = User
        fields = ("sid", "email")


class EmailSchemaIn(BaseNormalizedEmail):
    ...


class EnterVerificationCodeSchemaIn(BaseNormalizedEmail, Schema):
    code: str


class ResetPasswordSchemaIn(Schema):
    key: str
    new_password: str
