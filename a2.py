# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        '''(Rat, str, int, int) -> NoneType
        >>> rat1 = Rat('P', 1, 4)
        >>> str(rat1)
        'P at (1, 4) ate 0 sprouts.'
        '''
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        '''(Rat, int, int) -> NoneType
        >>> rat1 = Rat('P', 1, 4)
        >>> rat1.set_location(2, 5)
        >>> str(rat1)
        'P at (2, 5) ate 0 sprouts.'
        '''
        self.row = row
        self.col = col

    def eat_sprout(self):
        '''(Rat) -> NoneType
        >>> rat1 = Rat('P', 1, 4)
        >>> rat1.eat_sprout()
        >>> str(rat1)
        'P at (1, 4) ate 1 sprouts.'
        '''

        self.num_sprouts_eaten += 1

    def __str__(self):
        '''(Rat) -> str
        >>> rat1 = Rat('J', 4, 3)
        >>> str(rat1)
        'J at (4, 3) ate 0 sprouts.'
        '''

        return '{0} at ({1}, {2}) ate {3} sprouts.'\
        .format(self.symbol,self.row,self.col,self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        ''' (Maze, list of list of str, Rat, Rat)-> NoneType '''
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = self.number_sprouts_start()

    def number_sprouts_start(self):
        cont = 0
        for row in self.maze:
            for val in row:
                if val == SPROUT:
                    cont += 1
        return cont

    def is_wall(self, row, column):
        ''' (Maze, int, int) -> bool'''
        return self.maze[row][column] == WALL

    def update_maze(self):
        '''(Maze) -> Nonetype
        Update the rats position in the maze'''

        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

    def get_character(self, row, column):
        ''' (Maze, int, int) -> str'''
        self.update_maze()
        return self.maze[row][column]

    def move(self, rat ,vertical ,horizontal):
        ''''(Maze, Rat, int, int) -> bool '''
        if self.is_wall(rat.row + vertical, rat.col +horizontal) == False:
            self.maze[rat.row][rat.col] = HALL
            rat.set_location(rat.row + vertical, rat.col +horizontal)
            if self.maze[rat.row][rat.col] == SPROUT:
                rat.num_sprouts_eaten += 1
                self.maze[rat.row][rat.col] = HALL
                self.num_sprouts_left -= 1
            return False
        else:
            return True

    def __str__(self):
        '''(Maze) -> str'''
        self.update_maze()

        result = ''
        for line in self.maze:
            for value in line:
                result += value
            result += '\n'

        result = result + str(self.rat_1) + '\n'
        result = result + str(self.rat_2) + '\n'

        return result