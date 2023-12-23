import unittest


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.datas = {}
        for i in range(len(foods)):
            self.datas[cuisines[i]] = self.datas.get(cuisines[i], []) + [[ foods[i], ratings[i] ]]

    def changeRating(self, food: str, newRating: int) -> None:
        for cuisine in self.datas.keys():
            for i in range(len(self.datas[cuisine])):
                if self.datas[cuisine][i][0] == food:
                    self.datas[cuisine][i][1] = newRating
                    return

    def highestRated(self, cuisine: str) -> str:
        highest_idx = 0
        for i in range(1, len(self.datas[cuisine])):
            if self.datas[cuisine][i][1] > self.datas[cuisine][highest_idx][1]:
                highest_idx = i
            elif self.datas[cuisine][i][1] == self.datas[cuisine][highest_idx][1]:
                if self.datas[cuisine][i][0] < self.datas[cuisine][highest_idx][0]:
                    highest_idx = i

        return self.datas[cuisine][highest_idx][0]

    def __str__(self):
        return str(self.datas)
        # return '\n'.join([ f"name: {self.datas[][i]}; cuisine: {self.cuisines[i]}; rating: {self.ratings[i]}" for i in range(len(self.foods)) ])


# Your FoodRatings object will be instantiated and called as such:
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