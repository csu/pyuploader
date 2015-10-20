from abc import ABCMeta, abstractmethod

class Uploader:
    __metaclass__ = ABCMeta

    @abstractmethod
    def upload(self, filepath, title=None, parent=None): pass