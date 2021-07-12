import csv
from pathlib import path


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:

    def __init__(self, filepath):
        self.data = []
        relative = path(filepath)
        absolute = relative.absolute()
        with open(absolute) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def get_data(self):
        return self.data

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects