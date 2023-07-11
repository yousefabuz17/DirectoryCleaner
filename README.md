# Directory Cleaner

The Directory Cleaner is a Python script that enables efficient organization and cleanup of directories by moving outdated files to a designated destination directory based on a specified date.

## Features

- **Automated Directory Cleanup:** The script automatically identifies files in the source directory that are older than the specified date and moves them to the destination directory.
- **Flexible Configuration:** Users can define multiple directories to clean up, each with its own source and destination paths and a move before date.
- **File Exclusion:** The script allows you to define a list of ignored files, such as system files or specific file types, which will be excluded from the cleanup process.
- **Timestamped Backup:** A new directory is created in the destination directory with a timestamp representing the time the program was run. The outdated files are moved to this timestamped backup directory, preserving their original directory structure.
- **Daemon Mode:** The script can be set up as a daemon, running automatically at specified intervals.

## Getting Started

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine or download the source code.
3. Customize the configuration by editing the `config.json` file. Specify the directories to clean up, the destination directory, the move before date, and any ignored files.
4. (Optional) Configure the script to run as a daemon:
    - **Unix-based Systems (including macOS):** Follow the steps below to create a launchd service.
        - Create a new plist file `com.example.directory_cleaner.plist` in the `/Library/LaunchDaemons` directory.
        - Edit the plist file and provide the correct paths to the Python executable and the `directory_cleaner.py` script.
        - Set the appropriate permissions for the plist file: `sudo chown root:wheel /Library/LaunchDaemons/com.example.directory_cleaner.plist` and `sudo chmod 644 /Library/LaunchDaemons/com.example.directory_cleaner.plist`.
        - Load the plist file to start the daemon: `sudo launchctl load /Library/LaunchDaemons/com.example.directory_cleaner.plist`.
    - **Windows Systems:** Follow the steps below to create a Windows service.
        - Use a third-party tool like `pywin32` to create a Windows service that runs the `directory_cleaner.py` script.
5. Run the script manually or start the daemon service to automatically clean up directories based on the configured settings.


## Configuration

The `config.json` file contains the following settings:

- `directories`: An array of directory objects, each specifying the source directory, destination directory, and move before date.
- `.ignore`: A list of ignored files or file types that should not be moved. Customize this list by adding filenames or extensions.

## Examples

```json
{
  "directories": [
    {
      "src_dir": "/path/to/source/directory",
      "dest_dir": "/path/to/destination/directory",
      "move_before_date": "YYYY-MM-DD"
    },
    {
      "src_dir": "/path/to/another/source/directory",
      "dest_dir": "/path/to/another/destination/directory",
      "move_before_date": "YYYY-MM-DD"
    }
  ],
  ".ignore": [
    ".DS_Store",
    ".localized",
    "Thumbs.db",
    ".hdd",
    ".tmp.drivedownload",
    ".tmp.driveupload"
  ]
}
```

# Future Enhancements

1. **User Interface**: Turn project into a GUI application.
    - ~~**Allow User Input**: Allow users to specify the source and destination directories, move before date, and ignored files.~~
    - ~~**Display Progress**: Display the progress of the cleanup process.~~
    - ~~**Display Errors**: Display any errors that occur during the cleanup process.~~
    - ~~**Display Results**: Display the number of files moved and the total size of the files moved.~~
    - ~~**Daemon Mode**: Allow users to configure the script to run as a daemon.~~


# GUI Application
![Screen Shot 2023-07-10 at 8 12 18 PM](https://github.com/yousefabuz17/DirectoryCleaner/assets/68834704/77385c14-8926-4049-a3fe-fa0ff87119b2)








