import os
import readline

HISTORY_FILE = os.path.expanduser('~/myhistory')
if os.path.exists(HISTORY_FILE):
    readline.read_history_file(HISTORY_FILE)
readline.add_history('command2')
readline.write_history_file(HISTORY_FILE)
