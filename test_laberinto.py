import unittest
from laberinto import Game

class TestLaberinto(unittest.TestCase):

    def test_make2RoomsMaze(self):
        game = Game()
        maze = game.make2RoomsMaze()
        
        self.assertEqual(len(maze.rooms), 2)
        
        room1 = maze.rooms[0]
        room2 = maze.rooms[1]
        
        self.assertIsInstance(room1, Room)
        self.assertIsInstance(room2, Room)
        
        self.assertIsNotNone(room1.south)
        self.assertIsNotNone(room2.north)
        
        door = room1.south
        self.assertEqual(door, room2.north)
        
if __name__ == '__main__':
    unittest.main()
