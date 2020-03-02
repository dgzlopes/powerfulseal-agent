from base import AbstractAttack
import uuid


class NetworkAttack(AbstractAttack):
    def __init__(self, type, args):
        self.id = uuid.uuid1()
        self.type = type
        self.args = args
        it = iter(self.args)
        self.duration = 60
        for elem in it:
            # General
            if elem in ("-d", "--duration"):
                self.duration = int(next(it))
            # Latency
            elif elem in ("-m", "--ms"):
                self.ms = int(next(it))

    def run(self):
        if self.type == "latency":
            pass
        return self.id

    def remove(self):
        return self.id
