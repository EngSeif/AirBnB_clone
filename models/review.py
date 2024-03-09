#!/usr/bin/python3
"""
This Module Contains :-
-   Review Class Which Inherit
    From Base Model Class

-   It Has Reviews On
    That Appartment
"""


from .base_model import BaseModel


class Review(BaseModel):
    """
    Review Class Which Inherit
    From Base Model Class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
