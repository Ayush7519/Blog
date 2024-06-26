from django.core.validators import FileExtensionValidator, RegexValidator

# for the alphabet vlidations
isalphavalidator = RegexValidator(
    "^[a-z- A-z]+$", message="Invalide data to the fields........", code="Invalid name"
)

# fro the alphanumerical validations.
isalphanumericalvalidator = RegexValidator(
    "^[a-z- A-z 0-9]+$",
    message="Invalide data to the fields......",
    code="Invalide name",
)