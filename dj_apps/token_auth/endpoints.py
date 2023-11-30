from django.contrib.auth import authenticate, get_user_model
from django.db import transaction

from ninja import Router

from profiles.exceptions import EmailAlreadyExists, InvalidLogin, UnexistingUser

from .exceptions import MagicLinkNotFound
from .models.magic_link_token import MagicLinkToken, MagicLinkUsage
from .models.password_less_token import LoginPasswordLessToken, SignupPasswordLessToken
from .schemas import (
    EmailSchemaIn,
    ResetPasswordSchemaIn,
    UserSchemaInCreate,
    UserSchemaInLogin,
    UserSchemaOut,
)

User = get_user_model()
router = Router()


##########################################################################################
# Classical Authentication
##########################################################################################


@router.post("classical/signup", response=UserSchemaOut, auth=None)
def signup(request, payload: UserSchemaInCreate):
    """By Design, the signup will also log the user in, that's why it return the same schema"""

    if User.objects.filter(email=payload.email).exists():
        raise EmailAlreadyExists()

    new_user = User.objects.create_user(**payload.dict(exclude_unset=True))
    return new_user


@router.post("classical/login", response=UserSchemaOut, auth=None)
def login(request, payload: UserSchemaInLogin):
    """NOTE: logout does not require an endpoint, as it's just a front-end operation"""
    user = authenticate(request, email=payload.email, password=payload.password)
    if user is not None:
        return user
    else:
        raise InvalidLogin()


@router.post("classical/send-reset-password-link", auth=None)
def send_reset_password_link(request, payload: EmailSchemaIn):
    try:
        user = User.objects.get(email=payload.email)
    except User.DoesNotExist:
        raise UnexistingUser()
    else:
        MagicLinkToken.send_new_to(user=user, usage=MagicLinkUsage.RESET_PASSWORD)


@router.post("classical/reset-password", auth=None)
def reset_password(request, payload: ResetPasswordSchemaIn):
    try:
        magic_link = MagicLinkToken.objects.get(key=payload.key)
    except MagicLinkToken.DoesNotExist:
        raise MagicLinkNotFound()
    else:
        assert magic_link.usage == MagicLinkUsage.RESET_PASSWORD
        user = magic_link.user
        with transaction.atomic():
            user.set_password(payload.new_password)  # WARN: unchecked
            user.save()
            magic_link.consume()


##########################################################################################
# Passwordless Authentication
##########################################################################################


@router.post("passwordless/enter-email", response=UserSchemaOut, auth=None)
def enter_email(request, payload: EmailSchemaIn):
    # WARN: until the user is not signed up, someone can sign up.
    try:
        user = User.objects.get(email=payload.email)
    except User.DoesNotExist:
        SignupPasswordLessToken.send_to(email=payload.email)
    else:
        LoginPasswordLessToken.send_to(user=user)
