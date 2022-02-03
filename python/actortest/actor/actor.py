#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: Mingyeong Yang (mingyeong@khu.ac.kr)
# @Date: 2021-09-30
# @Filename: actor.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

from __future__ import absolute_import, annotations, division, print_function

import asyncio

from clu.actor import AMQPActor

from .commands import parser as greet_command_parser


# from scpactor import __version__

__all__ = ["testactor"]


class testactor(AMQPActor):
    """lvmscp controller actor.
    In addition to the normal arguments and keyword parameters for
    `~clu.actor.AMQPActor`, the class accepts the following parameters.
    Parameters
    ----------
    """

    parser = greet_command_parser

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

    async def start(self):
        """Start the actor and connect the controllers."""
        await super().start()

    async def stop(self):
        return super().stop()

    @classmethod
    def from_config(cls, config, *args, **kwargs):
        instance = super(testactor, cls).from_config(config, *args, **kwargs)
        assert isinstance(instance, testactor)
        assert isinstance(instance.config, dict)

        return instance