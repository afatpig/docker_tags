# -*- coding:utf-8 -*-
"""To list tags of a docker repo

Get from https://registry.hub.docker.com/v1/repositories/{repo}/tags

..
 @author XieY.J.
 Created on 2021.01.16

"""
from .dtags import get_tags
from .__main__ import main

__all__ = [
    'get_tags',
    'main'
]
