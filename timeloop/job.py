from threading import Thread, Event
from datetime import datetime


class Job(Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        Thread.__init__(self)
        self.stopped = Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        stopped = self.stopped
        task = self.execute

        while not stopped.is_set():
            next_run = datetime.now() + self.interval
            task(*self.args, **self.kwargs)
            timeout_left = (next_run - datetime.now()).total_seconds()
            if timeout_left > 0:
                stopped.wait(timeout_left)
