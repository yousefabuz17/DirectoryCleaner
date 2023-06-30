# DirectoryCleaner Project

## Introduction
The DirectoryCleaner project is designed to clean up and organize specific directories on your computer, with a focus on the Desktop and Downloads folders. It automatically identifies files based on their creation or modification date and moves them into a new folder, which is named after the date it was created. This project aims to provide a more organized and clutter-free environment by effectively managing files in designated directories.

## Features
- Automatic cleaning of the Desktop and Downloads folders
- Identification of files based on creation/modification date
- Creation of new folders named after the date the files are moved
- Moving files into the corresponding date-named folders

## Usage
Upon running the 'directory_cleaner.py' script, the program will scan the Desktop and Downloads folders for files. It will evaluate the creation or modification dates of the files and create a new folder for each unique date encountered. The files will then be moved into the respective date-named folders.

# Future Enhancements
- Allow customization of target directories for cleaning
- Implement file type filtering to selectively clean specific file types
- Add support for scheduling automatic cleanups
- Provide a user-friendly graphical interface for configuration and execution