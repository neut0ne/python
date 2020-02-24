#! /usr/bin/env python3

import sys
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

print(" ")
print("Welcome to Watcher! 👀")
print(" ")
print("This program will log any changes in the")
print("current directory. If any changes occur,")
print("a log output will be printed here.")
print("To quit, press ctrl + c.")
print(" ")
print("To quit, press ctrl + c.")
print(" ")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    except KeyboardInterrupt:
            observer.stop()
            os.remove("watcher.py")
    observer.join()            
