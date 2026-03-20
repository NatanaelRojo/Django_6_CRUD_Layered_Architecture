from ninja import ModelSchema, Schema
from pydantic import EmailStr, Field, field_validator

from apps.persons.models.person import Person

# --- SCHEMAS ---


class PersonSchema(ModelSchema):
    """Schema basado en el modelo para devolver datos (Output)"""

    class Meta:
        model = Person
        fields = ["id", "name", "email", "age", "created_at", "updated_at"]


class PersonCreateSchema(Schema):
    """Schema para recibir datos al crear o actualizar (Input)"""

    name: str = Field(
        min_length=4,
        max_length=100,
        examples=["John Doe"],
        description="The full name of the person.",
    )
    email: EmailStr = Field(
        examples=["john.doe@example.com"],
        description="The email address of the person.",
    )
    age: int = Field(
        gt=0,
        lt=120,
        examples=[30],
        description="The age of the person (must be a non-negative integer).",
    )

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        name_without_spaces = value.replace(" ", "")
        if not name_without_spaces.isalpha():
            raise ValueError("Name must contain only letters and spaces")

    @field_validator("email")
    @classmethod
    def validate_email_unique(cls, value: str) -> str:
        """Valida que el email sea único en la base de datos"""
        if Person.objects.filter(email=value).exists():
            raise ValueError("Email already exists")
        return value
