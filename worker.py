import logging
from models import Task
from time import sleep
from threading import Thread
from services.task_processor import TaskProcessor


class Worker(Thread):
    def run(self):
        while True:
            try:
                logging.info("Processing...")
                self.process()
                logging.info("Done.")
            except Exception as e:
                logging.warning(str(e))

            sleep(10)

    def get_task_available(self) -> Task:
        return Task.select().where(Task.status == "waiting").limit(1).get()

    def process(self):
        task = self.get_task_available()

        if task is None:
            return

        task.set_as_processing()
        task_processor = TaskProcessor(task)

        try:
            caption_ref_id = task_processor.execute()
            task.set_as_finished(caption_ref_id)
        except Exception as e:
            logging.warning(str(e))
            task.set_as_failed()
