import sys
import os
import json
import shutil
import daemon
from datetime import datetime as dt
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QCheckBox

class DirectoryCleanerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Directory Cleaner")
        
        self.src_label = QLabel("Source Directory:")
        self.src_line_edit = QLineEdit()
        self.src_browse_button = QPushButton("Browse...")
        self.src_browse_button.clicked.connect(self.browse_source_directory)

        self.dest_label = QLabel("Destination Directory:")
        self.dest_line_edit = QLineEdit()
        self.dest_browse_button = QPushButton("Browse...")
        self.dest_browse_button.clicked.connect(self.browse_destination_directory)

        self.date_label = QLabel("Move Before Date (YYYY-MM-DD):")
        self.date_line_edit = QLineEdit()
        
        self.daemon_checkbox = QCheckBox("Automatic Daemon")
        self.daemon_checkbox.setChecked(False)

        self.run_button = QPushButton("Run Directory Cleaner")
        self.run_button.clicked.connect(self.run_directory_cleaner)

        layout = QVBoxLayout()
        layout.addWidget(self.src_label)
        layout.addWidget(self.src_line_edit)
        layout.addWidget(self.src_browse_button)
        layout.addWidget(self.dest_label)
        layout.addWidget(self.dest_line_edit)
        layout.addWidget(self.dest_browse_button)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_line_edit)
        layout.addWidget(self.daemon_checkbox)
        layout.addWidget(self.run_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def browse_source_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        self.src_line_edit.setText(directory)

    def browse_destination_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Destination Directory")
        self.dest_line_edit.setText(directory)

    def run_directory_cleaner(self):
        src_path = self.src_line_edit.text()
        dest_path = self.dest_line_edit.text()
        move_date = self.date_line_edit.text()
        ignore_files = json.load(open(Path(__file__).parent.absolute() / 'config.json'))['.ignore']
        run_as_daemon = self.daemon_checkbox.isChecked()

        if run_as_daemon:
            with daemon.DaemonContext():
                cleaner = DirectoryCleaner(src_path, dest_path, move_date, ignore_files)
                cleaner.clean()
        else:
            cleaner = DirectoryCleaner(src_path, dest_path, move_date, ignore_files)
            cleaner.clean()


class DirectoryCleaner:
    def __init__(self, src_path, dest_path, move_date, ignored_files, dir_name=None):
        self.src_path = Path(src_path)
        self.dest_path = Path(dest_path)
        self.move_date = dt.strptime(move_date, '%Y-%m-%d')
        self.ignored_files = ignored_files
        self.dir_name = dir_name
        self.make_dir()

    make_dir = lambda self, name=None: os.makedirs(self.dest_path / self.time, exist_ok=True) if self.dir_name is None else os.makedirs(self.dest_path / self.dir_name, exist_ok=True)
    move_files = lambda self, file: shutil.move(self.src_path / file, self.dest_path / self.time / file)
    is_ignored = lambda self, file: any(entry in file for entry in self.ignored_files)
    clean = lambda self: [self.move_files(file) for file in os.listdir(self.src_path) if dt.fromtimestamp(os.path.getmtime(self.src_path / file)) <= self.move_date and not self.is_ignored(file) and not os.path.splitext(file)[1]=='']

    time = dt.now().strftime('%I-%M-%S%p %m:%d:%Y')

def main():
    app = QApplication(sys.argv)
    window = DirectoryCleanerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
