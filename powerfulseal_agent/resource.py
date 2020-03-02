from base import AbstractAttack
from utils import kill_proc
import uuid
import subprocess


class ResourceAttack(AbstractAttack):
    def __init__(self, type, args):
        self.id = uuid.uuid1()
        self.type = type
        self.args = args
        it = iter(self.args)
        self.duration = 60
        self.cores = 2
        self.workers = 2
        for elem in it:
            # General
            if elem in ("-d", "--duration"):
                self.duration = int(next(it))
            # CPU
            elif elem in ("-c", "--cores"):
                self.cores = int(next(it))
            # Memory
            elif elem in ("-w", "--workers"):
                self.workers = int(next(it))

    def run(self):
        if self.type == "cpu":
            p = subprocess.Popen(["stress", "-c", str(self.cores)])
            self.process = p.pid
            pass
        elif self.type == "memory":
            p = subprocess.Popen(["stress", "-m", str(self.workers)])
            self.process = p.pid
            pass
        return self.id

    def remove(self):
        kill_proc(self.process)
        return self.id
