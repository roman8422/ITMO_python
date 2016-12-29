from random import randrange

class Saper:
    def __init__(self, field_size, number_of_mines):
        self.field_size = field_size
        self.number_of_mines = number_of_mines
        self.field = []
        self.exploded = False
        self.cells_left = True
        self.generate_field()
        self.place_mines()

    def generate_field(self):
        for line in range(self.field_size):
            self.field.append([[0, 'closed'] for row in range(self.field_size)])

    def place_mines(self):
        for mine in range(self.number_of_mines):
            while True:
                x = randrange(self.field_size)
                y = randrange(self.field_size)
                if self.field[x][y][0] == 0:
                    self.field[x][y][0] = 'M'
                    break

        for x in range(self.field_size):
            for y in range(self.field_size):
                if self.field[x][y][0] != "M":
                    num_of_mines_around = 0

                    # Check mines on left and right
                    if x - 1 >= 0:
                        if self.field[x - 1][y][0] == 'M':
                            num_of_mines_around += 1
                    if x + 1 < self.field_size:
                        if self.field[x + 1][y][0] == 'M':
                            num_of_mines_around += 1
                    if y - 1 >= 0:
                        if self.field[x][y - 1][0] == 'M':
                            num_of_mines_around += 1
                    if y + 1 < self.field_size:
                        if self.field[x][y + 1][0] == 'M':
                            num_of_mines_around += 1

                    # Check mines on diagonales
                    # # Top left corner
                    if x - 1 >= 0 and y - 1 >= 0:
                        if self.field[x - 1][y - 1][0] == "M":
                            num_of_mines_around += 1
                    # # Bottom left corner
                    if x + 1 < self.field_size and y - 1 >= 0:
                        if self.field[x + 1][y - 1][0] == "M":
                            num_of_mines_around += 1
                    # Top right corner
                    if x - 1 >= 0 and y + 1 < self.field_size:
                        if self.field[x - 1][y + 1][0] == "M":
                            num_of_mines_around += 1
                    # # Bottom right corner
                    if x + 1 < self.field_size and y + 1 < self.field_size:
                        if self.field[x + 1][y + 1][0] == "M":
                            num_of_mines_around += 1

                    self.field[x][y][0] = num_of_mines_around

    def draw_field(self, open_field = False):
        print()
        count = 0
        for x in range(self.field_size):
            line = ""
            for y in range(self.field_size):
                line += str(self.field[x][y][0]) if open_field or self.field[x][y][1] == 'open' else 'X'
                line += " "

            print(line)

    def open_cell(self):

        in_field_area = False
        while not in_field_area:

            good_coordinates = False
            while not good_coordinates:
                try:
                    (x, s, y) = input("Enter coordinates of cell you want to open (format 'x y'): \n")
                    x, y = int(x), int(y)
                    good_coordinates = True
                except Exception:
                    print("Wrong coordinates, try again(format 'x y'): \n")

            if x <= self.field_size - 1 and \
                y <= self.field_size - 1:
                in_field_area = True
            else:
                print("Wrong coordinates. Both coordinates should be in range 0 to {} \n".format(self.field_size - 1))

        if self.field[x][y][0] == 'M':
            self.exploded = True

        self.field[x][y][1] = "open"

    def check_field(self):
        self.cells_left = False
        cells_open = 0
        for x in range(self.field_size):
            for y in range(self.field_size):
                if self.field[x][y][1] == 'closed':
                    self.cells_left = True
                    break
                else:
                    cells_open += 1

        if cells_open == self.field_size ** 2 - self.number_of_mines:
            self.cells_left = False


    def start_game(self):
        while True:
            self.draw_field()
            self.open_cell()
            if not self.exploded:
                self.check_field()

                if not self.cells_left:
                    self.draw_field(open_field=True)
                    print("You've won!!!\nCongratz!")
                    break
            else:
                self.draw_field(open_field=True)
                print("You've exploded\n")
                break


a = Saper(2, 0)

a.start_game()
