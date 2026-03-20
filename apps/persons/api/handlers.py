from http import HTTPStatus

from django.http import HttpRequest
from ninja import NinjaAPI
from ninja.errors import ValidationError


def validation_errors_handler(
    api: NinjaAPI, request: HttpRequest, exc: ValidationError
):
    errors = []
    for error in exc.errors:
        field = error.get("loc", ["unknown"])[-1]
        message = error.get("msg", "Invalid input")
        if message.startswith("Value error, "):
            message = message.replace("Value error, ", "")
        errors.append(
            {
                "field": field,
                "message": message,
            }
        )
    return api.create_response(
        request, {"errors": errors}, status=HTTPStatus.UNPROCESSABLE_CONTENT
    )


def set_handlers(api: NinjaAPI):
    api.add_exception_handler(
        ValidationError,
        lambda request, exc: validation_errors_handler(api, request, exc),
    )
