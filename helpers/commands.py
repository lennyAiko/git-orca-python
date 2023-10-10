#!/usr/bin/env python3

import requests, os, json
from .creator import write_json_issues, write_txt_issues, write_json_pr, write_txt_pr

def ask_question(question, type):
    pass

def CLI(token, args):
    print("\n<==> git-orca <==>\n")

    owner = None
    if not args["owner"]:
        owner = input("\nWho is the owner of the repo?\n")
        if not owner:
            owner = "lennyaiko"
            print(owner)

    repo = None
    if not args["name"]:
        repo = input("\nWhat is the name of the repo?\n")
        if not repo:
            repo = "git-orca"
            print(repo)

    selection = None
    if not args["issues"] and not args["pr"]:
        selection = input("\nDo you want to view issues or PR?\n")
    if args["issues"]: selection = "issues"
    if args["pr"]: selection = "pr"
    print(selection)

    state = None
    if not args["opened"] and not args["closed"]:
        state = input("\nDo you want open or closed?\n")
    if args["opened"]: state = "open"
    if args["closed"]: state = "closed"
    print(state)

    page = None
    if args["p"] == 0:
        page = int(input("\nWhat page do you want to view?\n"))
        if page < 1:
            page = "1"
    print(page)

    per_page = None
    if args["pp"] == 0:
        per_page = int(input("\nHow many per page?\n"))
        if per_page < 1:
            per_page = "30"
    print(per_page)

    file_format = None
    if not args["json"] and not args["txt"]:
        file_format = input("\nSelect a file format (json/txt):\n")
    if args["json"]: file_format = "json"
    if args["txt"]: file_format = "txt"
    print(file_format)

    print("\nFetching...\n")

    r = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "Authorization": f"Bearer {token}"
            },
            params={
                "state": f"{state}",
                "per_page": f"{per_page}",
                "page": f"{page}"
            }
        )
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