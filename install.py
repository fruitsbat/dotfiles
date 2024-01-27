#!/usr/bin/python3

import os
import pathlib

from dataclasses import dataclass


@dataclass
class Link:
    location: str
    target: str

    def real_target(self) -> str:
        return os.path.realpath(self.target)

    def real_location(self) -> str:
        return os.path.realpath(self.location)


def make_symlink(symlink: Link) -> None:
    print(f"creating symlink from {symlink.real_location()} to {symlink.real_target()} ")
    os.symlink(symlink.real_target(), symlink.real_location())


# check if a symlink already points to the right place
# if not make it point there
def fixup_symlink(symlink: Link) -> None:
    link_target = os.readlink(symlink.location)
    link_target = os.path.realpath(link_target)

    if link_target == symlink.real_target():
        print("... and points to the right place")

    else:
        print("... and points to the wrong place.\n fixing...")
        os.unlink(symlink.location)


def add_symlink(symlink: Link) -> None:
    location = pathlib.Path(symlink.location)
    # check if the symlink exists already
    if location.is_symlink():
        print(f"symlink at {symlink.real_location()} already exists...")
        fixup_symlink(symlink)

    elif location.exists():
        print(
            f"there is something at the location {symlink.real_location()}. \
            please check if you still need it and remove it if not."
        )

    else:
        make_symlink(symlink)


symlinks: Link = [Link(location="../fish", target="./fish")]

for symlink in symlinks:
    add_symlink(symlink)
