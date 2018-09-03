from pathlib import Path
import subprocess

backup_sources = [
    ,
]

backup_dest = Path()
logfile = Path()

for path in map(Path, backup_sources):
    subprocess.run(["rsync", "-aihW", "--progress", "--log-file", logfile, path, backup_dest])
