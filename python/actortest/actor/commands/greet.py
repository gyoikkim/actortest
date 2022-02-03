# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2021-10-05
# @Filename: greet.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)


from __future__ import absolute_import, annotations, division, print_function

import datetime

import click
from clu.command import Command

from . import parser


__all__ = ["greet"]


@parser.group()
def greet():
    """tasks for greet"""
    pass


@greet.command()
async def say_hello(command: Command):
    command.write('i', text='Hi!')
    command.info(text="greet is completed")
    command.finish()

'''
@parser.group()
def greet():
    """tasks for greet"""
    pass


@greet.command()
@click.argument("NAME", type=str, required=False)
async def say_hello(command: Command, name: str):
    command.write('i', text=f'Hi {name}!')
    command.finish()
'''