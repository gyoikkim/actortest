import os

import click


from sdsstools.daemonizer import DaemonGroup


@click.group(cls=DaemonGroup, prog="ecp_actor", workdir=os.getcwd())

def acting():
    """Runs the actor."""
    print("acting starting now")

if __name__ == "__main__":
    acting()