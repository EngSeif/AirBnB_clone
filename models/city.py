#!/usr/bin/python3
"""
This Module Contains :-
-   City Class Which Inherit
    From Base Model Class

-   It Has The State Id
    In Which The Hotel
    In
"""


from .base_model import BaseModel


class City(BaseModel):
    """
    City Class Which Inherit
    From Base Model Class
    """

    state_id = ""
    name = ""
