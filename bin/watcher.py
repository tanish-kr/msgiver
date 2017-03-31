# -*- coding: utf-8 -*-

import os
import sys
import time
import re
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class CIHandler(FileSystemEventHandler):

    def __init__(self, context):
        super(FileSystemEventHandler, self).__init__()
        self.context = context

    def on_created(self, event):
        test(event)

    def on_modified(self, event):
        test(event)


def test(context):
    try:
        if not context.is_directory and re.compile(".py$").search(context.src_path):
            logging.info("Static code analysis with pep8 :%s", context.src_path)
            subprocess.call(["pep8", context.src_path])
            prefix = "" if re.compile("^test_").search(context.src_path.split("/")[-1]) else "test_"
            test_file_name = prefix + context.src_path.split("/")[-1]
            test_file_path = os.path.join(current_path(), "tests", test_file_name)
            logging.info("Unit test :%s", test_file_path)
            if os.path.exists(test_file_path):
                subprocess.call(["python", "-m", "unittest", test_file_path])
            else:
                logging.warn("No such file %s", test_file_path)

    except Exception as err:
        logging.exception("Error dosomething: %s", err)
        pass


def current_path():
    return os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
                )
            )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d%H:%M:%S')
    path = current_path() + "/msgiver"
    test_path = current_path() + "/tests"
    event_handler = CIHandler(path)
    test_event_handler = CIHandler(test_path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(test_event_handler, test_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join
