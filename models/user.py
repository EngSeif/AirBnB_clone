#!/usr/bin/python3
"""
This Module Contains :-
-   User Class Which Inherit
    From Base Model Class

-   It Has All The Info
    Of The Login User
"""


from .base_model import BaseModel


class User(BaseModel):
    """
    User Class Which Inherit
    From Base Model Class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
