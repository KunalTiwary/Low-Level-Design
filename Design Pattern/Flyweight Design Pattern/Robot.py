from abc import ABC, abstractmethod


class Robot(ABC):
    @abstractmethod
    def display(self, x, y):
        pass

