import random
from typing import List, Union

class UnopenedCell():
	def __init__(self) -> None:
		pass

class OpenedCell():
	def __init__(self) -> None:
		pass

class FlaggedCell():
	def __init__(self) -> None:
		pass


class Bomb():
	BOMB = "*"
	def __init__(self) -> None:
		pass
	def __repr__(self) -> str:
		return self.BOMB

class Empty():
	def __init__(self) -> None:
		self.num = 0
	def __repr__(self) -> str:
		return str(self.num)

class Cell():
	def __init__(self) -> None:
		self.state: Union[UnopenedCell, OpenedCell, FlaggedCell] = UnopenedCell()
		self.contain: Union[Empty, Bomb] = Empty()
	def __repr__(self) -> str:
		return str(self.contain)

class Board():
	'''Generate board for minesweeper,
	bombs parameter sets max limit, not exact amount
	'''
	def __init__(self, x: int, y: int, bombs: int) -> None:
		self.x = x
		self.y = y
		self.bombs = bombs
	
	def generate(self) -> List[List[Cell]]:
		'''Generates new board.'''
		self.board: List[List[Cell]] = list()
		self.__generate_matrix()
		self.__add_bombs()
		self.__add_nums()
		return self.board
	
	def __generate_matrix(self):
		'''Creating matrix, and adding Empty cells'''
		for y in range(self.y):
			row_arr = list()
			for x in range(self.x):
				row_arr.append(Cell())
			self.board.append(row_arr)

	def __add_bombs(self):
		'''Adding bombs to board'''
		for i in range(self.bombs):
			self.board[random.randint(0, self.y-1)][random.randint(0, self.x-1)].contain = Bomb()

	def __add_nums(self):
		'''Numerating empty cells'''
		region = list()
		for row in range(len(self.board)):
			for cell in range(len(self.board[row])):
				if isinstance(self.board[row][cell].contain, Bomb):
					if cell < self.x-1:
						region.append(self.board[row][cell+1])
					if cell > 0:
						region.append(self.board[row][cell-1])
					if row > 0:
						region.append(self.board[row-1][cell])
						if cell < self.x-1:
							region.append(self.board[row-1][cell+1])
						if cell > 0:
							region.append(self.board[row-1][cell-1])
					if row < self.y-1:
						region.append(self.board[row+1][cell])
						if cell < self.x-1:
							region.append(self.board[row+1][cell+1])
						if cell > 0:
							region.append(self.board[row+1][cell-1])

		for cell in region:
			if isinstance(cell.contain, Empty):
				cell.contain.num += 1