#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if value <= 0:
            raise ValueError("width cannot be zero or negative")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
        }
