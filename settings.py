import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = "ww!"

# The bot token. Keep this secret!
BOT_TOKEN = "Get this from https://discord.com/developers/applications"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = "on winOS 4.0.0 | " + COMMAND_PREFIX + "commands"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
