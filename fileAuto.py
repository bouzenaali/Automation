import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# the source and the destinations directories
src_dir = "C:\\Users\pc\Downloads"
vid_dir = "C:\\Users\pc\Videos\videos"
img_dir = "C:\\Users\pc\Pictures\pic downloads"
doc_dir = "C:\\Users\pc\Documents\Downloaded_docs"
exe_dir = "C:\\Users\pc\Downloads\executables"
zip_dir = 'C:\\Users\pc\Downloads\zipped'
other_dir = 'C:\\Users\pc\Downloads\other'

# the extensions and the directories they will be moved to
ext_dir_map = {
    '.mp4': vid_dir,
    '.avi': vid_dir,
    '.mkv': vid_dir,
    '.jpg': img_dir,
    '.jpeg': img_dir,
    '.png': img_dir,
    '.pdf': doc_dir,
    '.doc': doc_dir,
    '.docx': doc_dir,
    '.exe': exe_dir,
    '.zip': zip_dir
}

# 
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(src_dir):
            src_path = os.path.join(src_dir, filename)
            if os.path.isfile(src_path):
                ext = os.path.splitext(filename)[1].lower()
                if ext in ext_dir_map:
                    dest_dir = ext_dir_map[ext]
                else:
                    dest_dir = other_dir
                dest_path = os.path.join(dest_dir, filename)
                shutil.move(src_path, dest_path)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, src_dir)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    