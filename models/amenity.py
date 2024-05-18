#!/usr/bin/python3
"""
This Module Contains :-
-   Amenity Class Which Inherit
    From Base Model Class

-   Amenity Describe The Type
    Of Comfort In The Hotel
    In AirBNB
"""


from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class Which Inherit
    From Base Model Class

    Attributes : name
    """

    name = ""
