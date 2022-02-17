from abc import ABCMeta, abstractmethod

class Prototype(metaclass=ABCMeta):
    
    @abstractmethod
    def clone():
        pass

#what is a metaclass