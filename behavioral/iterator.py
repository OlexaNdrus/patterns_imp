"""Implementation of Iterator pattern on Storage example.
Storage places boxes and stuff. WE can iterate through stuff(personal) and through each separate box"""

class Storage:
    def __init__(self, boxes, personal):
        if not personal:
            personal = []
        if not boxes:
            boxes = []
        self.personal = sorted(personal, key=lambda person: person._name)
        self.boxes = boxes

    def __iter__(self):
        return Personal_iterator(self.personal)

    def get_personal(self):
        return self.personal

    def get_boxes(self):
        return self.boxes

    def add_stuff_member(self, member):
        self.personal.append(member)

    def add_box_element(self, el):
        self.boxes.append(el)

class Box:
    def __init__(self, *boxes):
        if not boxes:
            boxes = []
        self.boxes = boxes

    def __iter__(self):
        return Box_iterator(self.boxes)

    def __repr__(self):
        return f'This box consist {len(self.boxes)} boxes inside'

    def add_box(self, *args):
        for el in args:
            self.boxes.append(el)


class Box_iterator:
    def __init__(self, boxes):
        self.position = 0
        self._boxes = boxes
        self.quantity = len(self._boxes)

    def __next__(self):
        el = self._boxes[self.position]
        self.position += 1
        if self.position > self.quantity:
            raise StopIteration
        return el

class Person:
    def __init__(self, name, position):
        full_name = name.split()
        self._name = full_name[0]
        self._second_name = full_name[1]
        self._position = position

    def __repr__(self):
        return f'{self._name}  works on position {self._position}'

    def get_name(self):
        return self._name

class Personal_iterator:
    def __init__(self, personal):
        self.counter = 0
        self.personal = personal
        self. quantity = len(self.personal)

    def __next__(self):
        if self.counter == self.quantity:
            raise StopIteration
        person = self.personal[self.counter]
        self.counter += 1
        return person

if __name__ == '__main__':
    big_box = Box()
    huge_box = Box()
    average_box = Box()
    small_box = Box()
    tiny_box = Box()

    big_box.add_box(average_box)
    huge_box.add_box(tiny_box, small_box)
    print(big_box, huge_box)

    first_person = Person('Lawrence Fishborn', 'Adutant')
    second_person = Person('Garhy Bomstruck', 'Manager')
    third_person = Person('Lila Morrel', 'Director')
    print(first_person, second_person, third_person)

    main_storage = Storage(boxes=[huge_box, big_box], personal=[first_person, second_person, third_person])
    for thing in main_storage:
        print(thing)

    for box in main_storage.get_boxes():
        print(box)

    print(main_storage.get_personal())