#!/usr/bin/env python3

import os, sys, typer
from dotenv import load_dotenv
load_dotenv()

from helpers.commands import CLI

args_store = {}

def main(token, args):
    try:
        CLI(token, args)
    except KeyboardInterrupt:
        print("\n\nThanks for using git-orca, see you next time Champ!")
        sys.exit()
    
def get_args(
        owner: str = "lennyaiko",
        name: str = "git-orca",
        issues: bool = False,
        pr: bool = False,
        opened: bool = False,
        closed: bool = True,
        p: int = 1,
        pp: int = 30,
        txt: bool = False,
        json: bool = True,
    ):
    """
    Glad you made it here! The available commands are: \n
    owner => The owner of the repo (--owner=<repo_owner>) \n
    name => The name of the repo (--name=<repo_name>) \n
    issues or pr => The kind of data you want to fetch (--issues or --pr) \n
    opened or closed => The state of the PRs or issues (--opened or --closed) \n
    p and pp => The page number and how many per page (--p=1 and --pp=30) \n
    txt or json => The format of the output (--txt --json)
    """
    args_store["owner"] = owner
    args_store["name"] = name
    args_store["issues"] = issues
    args_store["pr"] = pr
    args_store["opened"] = opened
    args_store["closed"] = closed
    args_store["p"] = p
    args_store["pp"] = pp
    args_store["txt"] = txt
    args_store["json"] = json
    main(os.getenv("TOKEN"), args_store)

if __name__ == "__main__":
    typer.run(get_args)