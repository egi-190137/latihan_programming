import unittest


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited_points = set([ tuple([0, 0]) ])
        current_position = [0, 0]

        for direction in path:
            if direction == "N":
                current_position[1] += 1
            elif direction == "S":
                current_position[1] -= 1
            elif direction == "E":
                current_position[0] += 1
            elif direction == "W":
                current_position[0] -= 1
            
            print(current_position)
            print(visited_points)
            if tuple(current_position) in visited_points:
                return True
            

            visited_points.add(tuple(current_position))

        return False


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertFalse(self.solution.isPathCrossing("NES"))

    def test_example_2(self):
        self.assertTrue(self.solution.isPathCrossing("NESWW"))

    def test_example_3(self):
        self.assertFalse(self.solution.isPathCrossing("W"))


if __name__ == '__main__':
    unittest.main()        