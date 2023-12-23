import unittest


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisine_to_food = {}
        self.food_to_rating = {}
        for i in range(len(foods)):
            self.cuisine_to_food[cuisines[i]] = self.cuisine_to_food.get(cuisines[i], []) + [ foods[i] ]
            self.food_to_rating[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return max(self.cuisine_to_food, key=lambda x: self.cuisine_to_food[x])

# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
    
def test_helper(commands, params):
    test_result = [ None ]
    foodRatings = FoodRatings(*params[0])
    print(foodRatings)
    for i in range(1, len(commands)):
        print(commands[i])
        print(params[i])
        if commands[i] == "highestRated":
            test_result.append(foodRatings.highestRated(*params[i]))
        elif commands[i] == "changeRating":
            test_result.append(foodRatings.changeRating(*params[i]))
            print(foodRatings)
        print(test_result)
        print("\n\n")
    
    return test_result 


class MyTest(unittest.TestCase):

    def test_example_1(self):
        commands = [
            "FoodRatings", 
            "highestRated", 
            "highestRated", 
            "changeRating", 
            "highestRated", 
            "changeRating", 
            "highestRated"
        ]
        params = [
            [
                ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
                ["korean", "japanese", "japanese", "greek", "japanese", "korean"], 
                [9, 12, 8, 15, 14, 7]
            ], 
            ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]
        ]
        self.assertEqual(test_helper(commands=commands, params=params), [ None, "kimchi", "ramen", None, "sushi", None, "ramen" ])

    def test_example_2(self):
        commands = [
            "FoodRatings",
            "changeRating",
            "highestRated",
            "changeRating",
            "changeRating",
            "changeRating",
            "highestRated",
            "highestRated"
        ]
        params = [
            [
                ["emgqdbo","jmvfxjohq","qnvseohnoe","yhptazyko","ocqmvmwjq"],
                ["snaxol","snaxol","snaxol","fajbervsj","fajbervsj"],
                [2,6,18,6,5]
            ],
            ["qnvseohnoe",11],
            ["fajbervsj"],
            ["emgqdbo",3],
            ["jmvfxjohq",9],
            ["emgqdbo",14],
            ["fajbervsj"],
            ["snaxol"]
        ]

        self.assertEqual(test_helper(commands=commands, params=params), [None,None,"yhptazyko",None,None,None,"yhptazyko","emgqdbo"])


if __name__ == '__main__':
    unittest.main()        