from ninja import Field, ModelSchema

from .models import Badge


class BadgeSchemaOut(ModelSchema):
    owner_name: str = Field(None, alias="owner.name")

    class Meta:
        model = Badge
        fields = ("identifier", "expiration", "is_active")


class BadgeSchemaInCreate(ModelSchema):
    class Meta:
        model = Badge
        fields = ("identifier", "expiration", "is_active")
        extra = "forbid"


class BadgeSchemaInUpdate(ModelSchema):
    class Meta:
        model = Badge
        fields = ("expiration", "is_active")
        fields_optional = ("expiration", "is_active")

    model_config = {"extra": "forbid"}
