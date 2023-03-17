from abc import ABC
from abc import abstractmethod


class BaseBuilder:
    def __init__(self, text):
        self.text = text

    def load_data(self):
        return self.text

    @abstractmethod
    def transform_data(self):
        pass

    @staticmethod
    def output_data(text):
        return text

    def process_string(self):
        self.load_data()

        transformed_data = self.transform_data()

        return self.output_data(transformed_data)
