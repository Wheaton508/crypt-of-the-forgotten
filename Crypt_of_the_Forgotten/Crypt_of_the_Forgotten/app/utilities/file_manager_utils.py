import os
import pathlib
from app.constants import APP_NAME, APP_AUTHOR
from app.utilities.file_manager import FileManager
import app.utilities.platformdirs as appdirs

def get_app_data_fman() -> FileManager:
    '''Get the file manager for the app data directory'''
    appdata_dir = pathlib.Path(appdirs.user_log_dir(APP_NAME, APP_AUTHOR))
    if not os.path.isdir(appdata_dir):
        os.makedirs(appdata_dir)
    return FileManager(appdata_dir)