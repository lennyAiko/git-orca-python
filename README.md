# git-orca (python)

This a CLI tool to fetch issues and PRs from any repo

## Packages

To use this tool, the below listed are required

- [Python](https://www.python.org/downloads/)
- Github access token. How to get one [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)

## Installation/Setup

1. Clone this repository to your local machine

```bash
git clone https://github.com/lennyAiko/git-orca-python.git
```

2. Navigate to the repository directory

```bash
cd git-orca-python
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

<!-- change configuring .env file -->

4. Create a `.env` file

```bash
touch .env
```

5. Add your Github access token as a variable to the `.env` file.

```bash
> cat .env
GITHUB_ACCESS_TOKEN=<github_access_token>
```

> **NOTE**
replace `github_access_token` with your github personal access token

## Usage

For a quick start, after installation/setting up the repo just run the below command. This would start an interactive session for you to provide the necessary info about the repository.

1. Install the package

```bash
node index.js
```

Alternatively, you can provide the information about the repo on execution of the script with flags:

- --owner: Specifies the GitHub username of the repository owner.
- --name: Specifies the name of the repository.
- --issue: Indicates that you want to view issues.
- --pr: Indicates that you want to view PRs.
- --open: Indicates that you want to view open issues/PRs.
- --closed: Indicates that you want to view closed issues/PRs.
- --p: Specifies the page number you want to view (e.g., page 1).
- --pp: Specifies the number of items per page (e.g., 10 items per page)

### For issues

```bash
node index.js --owner <github username> --name <repository name> --issue --open --p <page number> --pp <number of items per page>
```

### For pull requests

```bash
node index.js --owner <github username> --name <repository name> --pr --closed --p <page number> --pp <number of items per page>
```

### Example

```bash
node index.js --owner lennyaiko --name git-orca --issue --closed --p 1 --pp 5
```

> **NOTE**
You don't have to specify all the flags