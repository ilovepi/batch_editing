# -*- coding: utf-8 -*-
# Good Text
#Good Text
# Good Text
from .replace import replace


def main():
    replace("__init__.py", "#\sGood\sText", "#bad text", True)