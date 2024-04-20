import os
from folders import folder

with open(os.path.join(folder, './all_text/Edition_logs/Edition_logs.txt'), 'r') as f:
    Edition_logs: str = f.read()

with open(os.path.join(folder, './all_text/command_table/command_table.txt'), 'r') as f:
    Command_table: str = f.read()