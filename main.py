#!/usr/bin/env python3

import os, sys
from dotenv import load_dotenv
load_dotenv()

from helpers.commands import CLI

def main(TOKEN):
    try:
        CLI(TOKEN)
    except KeyboardInterrupt:
        print("\n\nThanks for using git-orca, see you next time Champ!")
        sys.exit()

if __name__ == "__main__":
    main(os.getenv("TOKEN"))