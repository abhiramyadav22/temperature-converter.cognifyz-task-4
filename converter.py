"""
converter.py

Contains temperature conversion functions between
Celsius and Fahrenheit.
"""

from typing import Union

Number = Union[int, float]


def celsius_to_fahrenheit(celsius: Number) -> float:
    """
    Convert Celsius to Fahrenheit.

    Formula:
        F = (C × 9/5) + 32
    """
    return (float(celsius) * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: Number) -> float:
    """
    Convert Fahrenheit to Celsius.

    Formula:
        C = (F − 32) × 5/9
    """
    return (float(fahrenheit) - 32) * 5 / 9
