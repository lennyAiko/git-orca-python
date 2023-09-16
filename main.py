#!/usr/bin/env python3

import os
from dotenv import load_dotenv
load_dotenv()

from helpers.commands import CLI

TOKEN = os.getenv("TOKEN")

CLI(TOKEN)
