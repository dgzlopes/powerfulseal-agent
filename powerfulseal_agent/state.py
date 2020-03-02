from base import AbstractAttack
import uuid
import os


class StateAttack(AbstractAttack):
    def __init__(self, type, args):
        self.id = uuid.uuid1()
        self.type = type
        self.args = args
        it = iter(self.args)
        for elem in it:
            if elem in ("-w", "--wait"):
                self.wait = int(next(it))

    def run(self):
        if self.type == "shutdown":
            os.system("echo o > /sysrq")
        elif self.type == "restart":
            os.system("echo b > /sysrq")
        return self.id

    def remove(self):
        return self.id
