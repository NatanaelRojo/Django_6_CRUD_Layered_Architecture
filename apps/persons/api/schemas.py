from ninja import ModelSchema, Schema
from pydantic import EmailStr, Field

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
        max_length=100,
        examples=["John Doe"],
        description="The full name of the person.",
    )
    email: EmailStr = Field(
        examples=["john.doe@example.com"],
        description="The email address of the person.",
    )
    age: int = Field(
        ge=0,
        examples=[30],
        description="The age of the person (must be a non-negative integer).",
    )
