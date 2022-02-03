#!/usr/bin/env python
# encoding: utf-8
#
# @Author: José Sánchez-Gallego
# @Date: Dec 1, 2017
# @Filename: cli.py
# @License: BSD 3-Clause
# @Copyright: José Sánchez-Gallego

import os

import click
from click_default_group import DefaultGroup
from clu.tools import cli_coro

from sdsstools.daemonizer import DaemonGroup

from actortest.actor.actor import testactor as TESTActorInstance


@click.group(cls=DefaultGroup, default="actor", default_if_no_args=True)
@click.option(
    "-c",
    "--config",
    "config_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Path to the user configuration file.",
)
@click.option(
    "-v",
    "--verbose",
    count=True,
    help="Debug mode. Use additional v for more details.",
)
@click.pass_context
def actortest(ctx, config_file, verbose):
    """brings the configuration .yaml file"""

    ctx.obj = {"verbose": verbose, "config_file": config_file}


@actortest.group(cls=DaemonGroup, prog="actortest_actor", workdir=os.getcwd())
@click.pass_context
@cli_coro
async def actor(ctx):
    """Runs the actor."""
    default_config_file = os.path.join(os.path.dirname(__file__), "etc/actortest.yml")
    config_file = ctx.obj["config_file"] or default_config_file

    actortest_obj = TESTActorInstance.from_config(config_file)

    if ctx.obj["verbose"]:
        actortest_obj.log.fh.setLevel(0)
        actortest_obj.log.sh.setLevel(0)

    await actortest_obj.start()
    await actortest_obj.run_forever()


if __name__ == "__main__":
    actortest()