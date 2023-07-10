import os
import json
import shutil
from datetime import datetime as dt
from pathlib import Path


class DirectoryCleaner:
    get_time = lambda _: dt.now().strftime('%I-%M-%S%p %m:%d:%Y')
    time = get_time(1)
    def __init__(self, src_path, dest_path, move_date):
        self.src_path = Path(src_path)
        self.dest_path = Path(dest_path)
        self.move_date = dt.strptime(move_date, '%Y-%m-%d')
        self.make_dir()
    
    def make_dir(self):
        os.makedirs(Path(self.dest_path) / self.time, exist_ok=True)
    
    def move_files(self, file):
        shutil.move(self.src_path / file, self.dest_path / self.time / file)
    
    def clean(self):
        files = list(filter(lambda i: self.move_files(i) if dt.fromtimestamp(os.path.getmtime(self.src_path / i))<=self.move_date else False,os.listdir(self.src_path)))



def main():
    conf = json.load(open(Path(__file__).parent.absolute() / 'config.json'))
    src_path = conf['src_dir']
    dest_path = conf['dest_dir']
    move_date = conf['move_before_date']
    cleaner = DirectoryCleaner(src_path, dest_path, move_date).clean()

if __name__ == '__main__':
    main()