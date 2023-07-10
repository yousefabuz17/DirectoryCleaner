import os
import json
import shutil
from datetime import datetime as dt
from pathlib import Path

class DirectoryCleaner:
    def __init__(self, src_path, dest_path, move_date, ignored_files):
        self.src_path = Path(src_path)
        self.dest_path = Path(dest_path)
        self.move_date = dt.strptime(move_date, '%Y-%m-%d')
        self.ignored_files = ignored_files
        self.make_dir()

    make_dir = lambda self: os.makedirs(self.dest_path / self.time, exist_ok=True)
    move_files = lambda self, file: shutil.move(self.src_path / file, self.dest_path / self.time / file)
    is_ignored = lambda self, file: any(entry in file for entry in self.ignored_files)
    clean = lambda self: [self.move_files(file) for file in os.listdir(self.src_path) if dt.fromtimestamp(os.path.getmtime(self.src_path / file)) <= self.move_date and not self.is_ignored(file) and not os.path.splitext(file)[1]=='']

    time = dt.now().strftime('%I-%M-%S%p %m:%d:%Y')

def main():
    conf = json.load(open(Path(__file__).parent.absolute() / 'config.json'))
    directories = conf.get('directories', [])
    ignored_files = [entry.lower() for entry in conf.get('.ignore', [])]
    for directory in directories:
        DirectoryCleaner(directory['src_dir'], directory['dest_dir'], directory['move_before_date'], ignored_files).clean()

if __name__ == '__main__':
    if dt.now().day == 1:
        try:
            main()
        except FileNotFoundError as e:
            print(f'FileNotFoundError: Change move_date on config.json to a date before {dt.fromtimestamp(os.path.getmtime(Path(__file__).parent.absolute() / "config.json"))}')
        except ValueError as e:
            print(f'ValueError: {str(e)}')
    else:exit()