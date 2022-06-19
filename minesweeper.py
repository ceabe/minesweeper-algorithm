import numpy as np
import random


class GameBoard:
	def __init__(self, lines, columns):
		self.lines = lines
		self.columns = columns
		self.board = [[]]

	def generate_board(self):
		# fill numpy 2d array with "."
		self.board = np.array(np.full((self.lines, self.columns), "."))
		# set mine count based on averaged lines + columns
		count = (self.lines + self.columns) / 2
		# count down through mines
		while count > 0:
			rand_x = random.randint(0, self.lines - 1)
			rand_y = random.randint(0, self.columns - 1)
			self.board[rand_x][rand_y] = "*"
			count -= 1

	def prettify(self, spacing):
		# god forbid I know whats going on here. Thanks StackOverflow!
		return '\n'.join([''.join([('{:' + str(spacing) + '}').format(item) for item in row]) for row in self.board])

		# vanilla python way of doing this
		# game_board = [["." for x in range(lines)] for y in range(columns)]


# stores 2 values from single line of input then typecasts to int
user_lines, user_columns = map(int, input().split())

game_board = GameBoard(user_lines, user_columns)
game_board.generate_board()
print(game_board.prettify(spacing=0))
