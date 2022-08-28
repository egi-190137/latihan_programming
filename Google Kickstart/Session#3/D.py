def find_number_of_gbuses_per_city(gbus_list, cities):
    bus_count_lst = [0]*len(cities)
    for i in range(len(cities)):
        for gbus in gbus_list:
            if cities[i] in range(gbus[0], gbus[1]+1):
                bus_count_lst[i] += 1
    return bus_count_lst


def main():
    # Get number of test cases
    test_cases = int(input())

    for test_case in range(1, test_cases + 1):
        # Get gbuses
        num_gbuses = int(input())
        # Put gbus cities into a list of tuples of [start, end]
        gbus_list = input().split()
        gbus_list = [(int(gbus_list[i]), int(gbus_list[i + 1]))
                            for i in range(len(gbus_list))
                            if i % 2 == 0]
        # Get cities
        num_cities_to_return = int(input())
        cities_list = []
        for i in range(num_cities_to_return):
            cities_list.append(int(input()))

        ans = find_number_of_gbuses_per_city(gbus_list, cities_list)
        print("Case #%d:" % (test_case), end=" ")
        for i in range(len(ans)):
            print("%d" % ans[i], end=" ")
        print("") # print new line after each case.

        # blank line between test cases
        if test_case != test_cases:
            _ = input()



if __name__ == "__main__":
    main()
