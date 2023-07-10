#!/usr/bin/python3
"""Defines class myint"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override  == the opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        return self.real == value
