import unittest
from Main import Snake, Apple
class TestSnake(unittest.TestCase):
    def test_grow(self):
        #skapar en orm och ger den riktning
        snake=Snake(10,10)
        snake.change_direction((1,0))
        snake.move()
        length_before=len(snake.body)
        snake.grow() # markerar att ormen ska växa
        snake.move() # ormen rör sig och bör vara ett segment längre
        self.assertEqual(len(snake.body),length_before+1) # Kontrollerar att kroppen faktiskt blev längre

    def test_collison(self):
        #sätter ormens huvud och kropp till samma koordinat för att simulera kollsion med sig själv
        snake=Snake(10,10)
        snake.body=[[10,10],[11,10],[10,10]]
        self.assertTrue(snake.check_colision()) # Huvudet finns i kroppen vilket ska returnera true

    def test_direction_reverse(self):
        # kontrollerar att ormen inte kan vända 180 grader
        snake=Snake(10,10)
        snake.change_direction((1,0)) # rör sig åt höger
        snake.change_direction((-1,0)) # rör sig åt vänster
        self.assertTrue(snake.direction,(1,0)) # riktningen ska fortfarande vara åt höger

if __name__ == "__main__":
    unittest.main()