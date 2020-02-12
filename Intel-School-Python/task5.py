""" Отборочное задание на школу Intel N5 """

# ЕСТЬ 5 ЗАКРЫТЫХ ЯЩИКОВ, РАСПОЛОЖЕННЫХ В РЯД.
# В ОДНОМ ИЗ ЯЩИКОВ ЛЕЖИТ МЯЧИК. КАЖДУЮ ПОПЫТКУ МОЖНО ОТКРЫТЬ ОДИН ЯЩИК.
# ПОСЛЕ КАЖДОЙ ПОПЫТКИ ВСЕ ЯЩИКИ СНОВА ЗАКРЫВАЮТСЯ И МЯЧИК
# ПЕРЕМЕЩАЕТСЯ В СОСЕДНИЙ ЯЩИК. КАК НАЙТИ МЯЧИК?
# КАК ВЫ БУДЕТЕ ДЕЙСТВОВАТЬ?

# Реализация условий задачи на Python 3.8 для проверки моих решений

from random import randint
ITERATIONS = 100000  # сколько раз протестировать заданный алгоритм со случайными условиями
BOXES = 5  # а если мы захотим обобщить задачу на N ящиков?


def list_inp(list_size):
    """Allows to enter a list and prints the result"""
    l_in = list()
    for i in range(1, list_size+1):
        print("Enter box to open on {} step".format(i))
        l_in.append(int(input()))
    return l_in


class Boxes:
    """Model of 5 boxes and  moving ball"""
    def __init__(self):
        """Constructor"""
        self.position = randint(1, BOXES)
        self.step = 0
        self.last_opened = 0
        self.found = False

    def reboot(self):
        """Sets the task to new start values"""
        self.position = randint(1, BOXES)
        self.step = 0
        self.last_opened = 0
        self.found = False
        print("reboot successful \n")

    def start(self):
        """Method gives all information about the attempt"""
        print("Iteration {} started.".format(i))
        print("Task created: ball in {} \n".format(self.position))

    def inc_step(self):
        """Method increases number of currently opened boxes"""
        self.step += 1

    def open(self, box_id):
        """Method handles all the consequences of opening box number <id>"""
        self.last_opened = box_id
        self.inc_step()
        if self.position == box_id:
            self.found = True
        else:
            self.ball_change()

    def open_custom(self):
        """Method gets a box to open from console"""
        print("Enter box to open:")
        box_id = int(input())
        self.open(box_id)

    def open_from_list(self, list_boxes):
        """Method handles opening a sequence of boxes from list <list_boxes>"""
        for i in list_boxes:
            print("Box to open:", i)
            print("Ball is in:", self.position)
            self.open(i)
            if self.end_attempt():
                self.reboot()
                return True
        self.reboot()
        return False

    def ball_change(self):
        """Method realizes motion of the ball after opening a box"""
        if self.position == BOXES:
            self.position = BOXES-1
        elif self.position == 1:
            self.position = 2
        else:
            direction = randint(1, 2)
            if direction == 1:
                self.position += 1
            else:
                self.position -= 1
        print("ball moves to {}".format(self.position))

    def end_attempt(self):
        """Method gives results of each opening attempt"""
        if self.found:
            print("Ball found in {} box on {} attempts \n".format(self.position, self.step))
        else:
            print("Ball not found on {} attempt \n".format(self.step))
        return self.found


boxes = Boxes()
print("Enter number of steps in your solution:")
N = int(input())
to_open = list_inp(N)

failed = 0
for i in range(1, ITERATIONS):
    boxes.start()
    if not boxes.open_from_list(to_open):
        failed += 1
        print("ITERATION {} FAILED".format(i))
        print("--------------------------------")

print("{} out of {} successfully".format(ITERATIONS-failed, ITERATIONS))
