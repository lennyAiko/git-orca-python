# let's create git-orca!

import requests, os, json
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

def default_value(var, value):
    if not var:
        var = value
        print(var)
    return var

print("\n<==> git-orca <==>\n")

owner = input("\nWho is the owner of the repo? ")
owner = default_value(var=owner, value="lennyaiko")

repo = input("\nWhat is the name of the repo? ")
repo = default_value(var=repo, value="git-orca")

selection = input("\nDo you want to view issues or PR? ")
selection = default_value(var=selection, value="issues")

state = input("\nDo you want open or closed? ")
state = default_value(var=state, value="closed")

page = input("\nWhat page do you want to view? ")
page = default_value(var=page, value="1")

per_page = input("\nHow many per page? ")
per_page = default_value(var=per_page, value="30")

file_format = input("\nSelect a file format" )
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

store = []
count = 0

if len(r) < 1:
    print(f"Found no {selection}'s here")
else:
    match(selection):
        case "issues":
            
                    match(file_format):
                        case "json":
                            for i in range(len(r)):
                                if "pull_request" not in r[i]:
                                    count+=1
                                    store.append({
                                        "count": count,
                                        "url": r[i]["url"],
                                        "title": r[i]["title"],
                                        "state": r[i]["state"],
                                        "issue_number": r[i]["number"],
                                        "user": r[i]["user"]["login"],
                                        "user_url": r[i]["user"]["url"],
                                        "created_at": r[i]["created_at"],
                                        "updated_at": r[i]["updated_at"],
                                        "closed_at": r[i]["closed_at"],
                                        "body": r[i]["body"] if r[i]["body"] else "empty"
                                    })
                                    with open("git-orca.json", "w+") as f:
                                        f.write(str(json.dumps({
                                            "total": len(store),
                                            "data": store,
                                            "watermark": "Generated by git-orca"
                                        }, indent=4)))
                
                        case "txt":
                            with open("git-orca.txt", "w+") as f:
                                for i in range(len(r)):
                                    if "pull_request" not in r[i]:
                                        count += 1
                                        f.write(
f"""{count}. {r[i]["title"]}
Url: {r[i]["url"]}
State: {r[i]["state"]}
Issue number: {r[i]["number"]}
User: {r[i]["user"]["login"]}
User url: {r[i]["user"]["url"]}
Created at: {r[i]["created_at"]}
Updated at: {r[i]["updated_at"]}
Closed at: {r[i]["closed_at"]}
Body: {r[i]["body"] if r[i]["body"] else "empty"}

"""
                                )
                                f.write("\nGenerated with git-orca")

        case "pr":
            for i in range(len(r)):
                if "pull_request" in r[i]:
                    match (file_format):
                        case "json":
                            count+=1
                            store.append({
                                "count": count,
                                "url": r[i]["url"],
                                "title": r[i]["title"],
                                "state": r[i]["state"],
                                "pull_request": r[i]["pull_request"]["url"],
                                "pull_request_number": r[i]["number"],
                                "user": r[i]["user"]["login"],
                                "user_url": r[i]["user"]["url"],
                                "created_at": r[i]["created_at"],
                                "updated_at": r[i]["updated_at"],
                                "closed_at": r[i]["closed_at"],
                                "body": r[i]["body"] if r[i]["body"] else "empty"
                            })
                            with open("git-orca.json", "w+") as f:
                                f.write(str(json.dumps({
                                    "total": len(store),
                                    "data": store,
                                    "watermark": "Generated by git-orca"
                                }, indent=4)))

                        case "pr":
                            with open("git-orca.txt", "w+") as f:
                                f.write(
f"""
{count}. {r[i]["title"]}
Url: {r[i]["url"]}
State: {r[i]["state"]}
Pull request: {r[i]["pull_request"]["url"]}
Pull request number: {r[i]["number"]}
User: {r[i]["user"]["login"]}
User url: {r[i]["user"]["url"]}
Created at: {r[i]["created_at"]}
Updated at: {r[i]["updated_at"]}
Closed at: {r[i]["closed_at"]}
Body: {r[i]["body"] if r[i]["body"] else "empty"}

"""
                                )
                                f.write("\nGenerated with git-orca")
                
        case _:
            print(f"Found no {selection}'s here")
           