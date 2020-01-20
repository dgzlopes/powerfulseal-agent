import abc, six


@six.add_metaclass(abc.ABCMeta)
class AbstractAttack:
    @abc.abstractmethod
    def run(self):
        pass  # pragma: no cover

    @abc.abstractmethod
    def remove(self):
        pass  # pragma: no cover
