import datetime
from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Due to the pandemic, "
                                     "everyone should have a vaccine")
        if datetime.date.today() > visitor["vaccine"]["expiration_date"]:
            raise OutdatedVaccineError("The vaccine is outdated")
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The mask should be put on the face")
        return f"Welcome to {self.name}"
