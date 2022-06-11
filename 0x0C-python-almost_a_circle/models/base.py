#!/usr/bin/python3
"""
Class first create
"""
import json


class Base:
    """
    Class Base manages the id attribute in all future classes
    and avoid duplicating the same code
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON representation of list_objs to a file
        """
        if list_objs is None or list_objs == []:
            listo = []
        else:
            listo = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__+".json", "w") as f:
            f.write(cls.to_json_string(listo))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return json.loads("[]")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        """
        try:
            f = open(str(cls.__name__) + ".json")
            f.close()
        except FileNotFoundError:
            return []

        liinst = []
        with open(str(cls.__name__) + ".json", "r") as f:
            liinst = cls.from_json_string(f.read())

        num_ins = len(liinst)
        inst = []
        for y in range(num_ins):
            inst.append(cls.create(**liinst[y]))

        return inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        if list_objs is None or list_objs == []:
            liobj = []
        with open(cls.__name__ + ".csv", "w") as fc:
            list_objs = [i.to_dictionary() for i in list_objs]
            rec = ['id', 'width', 'height', 'x', 'y']
            squ = ['id', 'size', 'x', 'y']
            if cls.__name__ == "Rectangle":
                f_csv = csv.DictWriter(fc, fieldnames=rec)
            else:
                f_csv = csv.DictWriter(fc, fieldnames=squ)
            f_csv.writeheader()
            f_csv.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of instances
        """
        try:
            f = open(str(cls.__name__) + ".csv")
            f.close()
        except FileNotFoundError:
            return []
        squ = ['id', 'size', 'x', 'y']
        rec = ['id', 'width', 'height', 'x', 'y']
        if cls.__name__ == "Rectangle":
            fieldn = rec
        else:
            fieldn = squ

        inst = []
        with open(str(cls.__name__) + ".csv", "r") as fc:
            cr = csv.reader(fc, delimiter=',')
            for i, dictt in enumerate(cr):
                if i > 0:
                    ins = cls(1, 1)
                    for x, y in enumerate(dictt):
                        if y:
                            setattr(ins, fieldn[x], int(y))
                    inst.append(ins)
        return inst
