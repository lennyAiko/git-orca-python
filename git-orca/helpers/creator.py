#!/usr/bin/env python3

import os, json

def cleaner(file):
    if os.path.isfile(file):
        os.remove(file)

def write_json_issues(data, source):
    store = []
    count = 0
    for i in range(len(data)):
        if "pull_request" not in data[i]:
            count+=1
            store.append({
                "count": count,
                "url": data[i]["url"],
                "title": data[i]["title"],
                "state": data[i]["state"],
                "issue_number": data[i]["number"],
                "user": data[i]["user"]["login"],
                "user_url": data[i]["user"]["url"],
                "created_at": data[i]["created_at"],
                "updated_at": data[i]["updated_at"],
                "closed_at": data[i]["closed_at"],
                "body": data[i]["body"] if data[i]["body"] else "empty"
            })
            with open("git-orca.json", "w+") as f:
                f.write(str(json.dumps({
                    "requested": "issues",
                    "source": source,
                    "total": len(store),
                    "data": store,
                    "watermark": "Generated by git-orca"
                }, indent=4)))
    print('Check git-orca.json for result')

def write_txt_issues(data, source):
    count = 0
    with open("git-orca.txt", "w+") as f:
        f.write("ISSUES\n")
        f.write(f"Source: {source}\n")
        f.write("\n")
        for i in range(len(data)):
            if "pull_request" not in data[i]:
                count += 1
                f.write(
f"""{count}. {data[i]["title"]}
Url: {data[i]["url"]}
State: {data[i]["state"]}
Issue number: {data[i]["number"]}
User: {data[i]["user"]["login"]}
User url: {data[i]["user"]["url"]}
Created at: {data[i]["created_at"]}
Updated at: {data[i]["updated_at"]}
Closed at: {data[i]["closed_at"]}
Body: {data[i]["body"] if data[i]["body"] else "empty"}

"""
                )
        f.write("\nGenerated with git-orca")
    print('Check git-orca.txt for result')

def write_json_pr(data, source):
    store = []
    count = 0
    for i in range(len(data)):
        if "pull_request" in data[i]:
            count+=1
            store.append({
                "count": count,
                "url": data[i]["url"],
                "title": data[i]["title"],
                "state": data[i]["state"],
                "pull_request": data[i]["pull_request"]["url"],
                "pull_request_number": data[i]["number"],
                "user": data[i]["user"]["login"],
                "user_url": data[i]["user"]["url"],
                "created_at": data[i]["created_at"],
                "updated_at": data[i]["updated_at"],
                "closed_at": data[i]["closed_at"],
                "body": data[i]["body"] if data[i]["body"] else "empty"
            })
            with open("git-orca.json", "w+") as f:
                f.write(str(json.dumps({
                    "requested": "PRs",
                    "source": source,
                    "total": len(store),
                    "data": store,
                    "watermark": "Generated by git-orca"
                }, indent=4)))
    print('Check git-orca.json for result')

def write_txt_pr(data, source):
    count = 0
    with open("git-orca.txt", "w+") as f:
        f.write("PRs\n")
        f.write(f"Source: {source}\n")
        f.write("\n")
        for i in range(len(data)):
            if "pull_request" in data[i]:
                f.write(
f"""
{count}. {data[i]["title"]}
Url: {data[i]["url"]}
State: {data[i]["state"]}
Pull request: {data[i]["pull_request"]["url"]}
Pull request number: {data[i]["number"]}
User: {data[i]["user"]["login"]}
User url: {data[i]["user"]["url"]}
Created at: {data[i]["created_at"]}
Updated at: {data[i]["updated_at"]}
Closed at: {data[i]["closed_at"]}
Body: {data[i]["body"] if data[i]["body"] else "empty"}

"""
                                    )
        f.write("\nGenerated with git-orca")
    print('Check git-orca.txt for result')
