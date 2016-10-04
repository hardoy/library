# -*- coding: utf-8 -*-
"""
    __init__.py

    :copyright: (c) 2016 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from .library import Book


def register():
    Pool.register(
        Book, 
        module='library', type_='model'
    )
