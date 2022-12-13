from models import Task
from time import sleep
from threading import Thread
from services.task_processor import TaskProcessor


class Worker(Thread):
    def run(self):
        while True:
            try:
                self.process()
            except:
                pass

            sleep(10)

    def get_task_available(self) -> Task:
        return Task.select().where(Task.status == "waiting").limit(1).get()

    def process(self):
        task = self.get_task_available()
        task.set_as_processing()
        task_processor = TaskProcessor(task)

        try:
            caption_ref_id = task_processor.execute()
            task.set_as_finished(caption_ref_id)
        except:
            task.set_as_failed()
