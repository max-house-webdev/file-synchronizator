import os

from .FileObserverABC import FileObserverABC


class FileObserver(FileObserverABC):
    """File observer implementation
    """

    def observe_local_files_storage(self):
        self.local_files_storage.clear()

        file_list = os.listdir(self.local_dir)

        for filename in file_list:
            file_abs_path = os.path.join(self.local_dir, filename)

            self.local_files_storage |= {
                filename: os.path.getmtime(file_abs_path)}
