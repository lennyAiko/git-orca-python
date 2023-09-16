#!/usr/bin/env python3

import requests, os, json
from .creator import write_json_issues, write_txt_issues, write_json_pr, write_txt_pr

def default_value(var, value):
    if not var:
        var = value
        print(var)
    return var

def CLI(TOKEN):
    print("\n<==> git-orca <==>\n")

    owner = input("\nWho is the owner of the repo?\n")
    owner = default_value(var=owner, value="lennyaiko")

    repo = input("\nWhat is the name of the repo?\n")
    repo = default_value(var=repo, value="mantasails")

    selection = input("\nDo you want to view issues or PR?\n")
    selection = default_value(var=selection, value="issues")

    state = input("\nDo you want open or closed?\n")
    state = default_value(var=state, value="closed")

    page = input("\nWhat page do you want to view?\n")
    page = default_value(var=page, value="1")

    per_page = input("\nHow many per page?\n")
    per_page = default_value(var=per_page, value="30")

    file_format = input("\nSelect a file format:\n" )
    file_format = default_value(var=file_format, value="txt")

    print("\nFetching...\n")

    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues",
                    headers={
                        "Accept": "application/vnd.github+json",
                        "X-GitHub-Api-Version": "2022-11-28",
                        "Authorization": f"Bearer {TOKEN}"
                    },
                    params={
                        "state": f"{state}",
                        "per_page": f"{per_page}",
                        "page": f"{page}"
                    })
    r = r.json()

    print("\nDone fetching")

    if len(r) < 1:
        print(f"Found no {selection}'s here")
    else:
        match(selection):
            case "issues":
                print("\nGenerating file...\n")
                match(file_format):
                    case "json":
                        write_json_issues(r)                
                    case "txt":
                        write_txt_issues(r)
            case "pr":
                print("\nGenerating file...\n")
                match (file_format):
                    case "json":
                        write_json_pr(r)
                    case "pr":
                        write_txt_pr(r)
            case _:
                print(f"Found no {selection}'s here")

if __name__ == "__main__":
    CLI()