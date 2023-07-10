import os
import json
import shutil
from datetime import datetime as dt
from pathlib import Path

class DirectoryCleaner:
    def __init__(self, src_path, dest_path, move_date):
        self.src_path = Path(src_path)
        self.dest_path = Path(dest_path)
        self.move_date = dt.strptime(move_date, '%Y-%m-%d')
        self.make_dir()

    make_dir = lambda self: os.makedirs(self.dest_path / self.time, exist_ok=True)
    move_files = lambda self, file: shutil.move(self.src_path / file, self.dest_path / self.time / file)
    clean = lambda self: [self.move_files(file) for file in os.listdir(self.src_path) if dt.fromtimestamp(os.path.getmtime(self.src_path / file)) <= self.move_date]

    time = dt.now().strftime('%I-%M-%S%p %m:%d:%Y')

def main():
    conf = json.load(open(Path(__file__).parent.absolute() / 'config.json'))
    DirectoryCleaner(conf['src_dir'], conf['dest_dir'], conf['move_before_date']).clean()

if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError as e:
        print(f'FileNotFoundError: Check the config.json file {str(e)}')
