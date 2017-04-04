#!/usr/bin/python

from enum import Enum

class Color(Enum):
    Black = 1
    White = 2

class Status(Enum):
    Dead = 1
    Alive = 2

class Type(Enum):
    Pon = 1
    Castle = 2
    Knight = 3
    Bishop = 4
    Queen = 5
    King = 6
