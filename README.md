# Minesweeper board generator

Usage is simple:
```python
b = Board(8, 6, 5)
b.generate()
```
```
[[*, 3, *, 1, 0, 0, 0, 0],
 [2, *, 2, 1, 0, 0, 0, 0],
 [1, 1, 2, 1, 1, 0, 0, 0],
 [0, 0, 1, *, 1, 1, 1, 1],
 [0, 0, 1, 1, 1, 1, *, 1],
 [0, 0, 0, 0, 0, 1, 1, 1]]
```

Board contains `Cell` objects
```python
print(type(b.generate()[0][0])) # -> <class '__main__.Cell'>
```
`Cell` object has these attributes:
- state (`UnopenedCell`, `OpenedCell`, `FlaggedCell`)
- contain (`Empty`, `Bomb`)

`Empty` object has `num` attribute. (Increments by __add_nums() private function)
