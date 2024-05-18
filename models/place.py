#!/usr/bin/python3
"""
This Module Contains :-
-   Place Class Which Inherit
    From Base Model Class

-   It Has The Description
    Of The Appartement
"""


from .base_model import BaseModel


class Place(BaseModel):
    """
    Place Class Which Inherit
    From Base Model Class

    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
