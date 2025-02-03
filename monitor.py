import os
import time
import logging

from watchdog.observers import Observer
from image_handler import ImageHandler

class Monitor:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        self.watch_directory = os.path.join(self.base_dir, "images")
        self.output_directory = os.path.join(self.base_dir, "faces")

        os.makedirs(self.watch_directory, exist_ok=True)
        os.makedirs(self.output_directory, exist_ok=True)

        self.event_handler = ImageHandler(self.watch_directory, self.output_directory)

    def start_monitoring(self):
        observer = Observer()
        observer.schedule(self.event_handler, self.watch_directory, recursive=False)
        observer.start()

        logging.info(f"Started monitoring {self.watch_directory}")
        logging.info(f"Extracted faces will be saved to {self.output_directory}")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            logging.info("Stopping monitoring...")

        observer.join()
