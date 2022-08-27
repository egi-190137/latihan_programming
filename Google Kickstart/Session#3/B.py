def number_of_record_breaking_days(number_of_days, vistors):
    record_breaking_days = 0
    last_breaking_days = 0
    for i in range(number_of_days):
        if i == 0:
            if vistors[i] > vistors[i+1]:
                record_breaking_days += 1
                last_breaking_days = vistors[i]
        elif i == number_of_days - 1:
            if vistors[i] > last_breaking_days and vistors[i] > vistors[i-1]:
                record_breaking_days += 1
                last_breaking_days = vistors[i]
        elif vistors[i] > last_breaking_days and vistors[i] > vistors[i-1] and vistors[i] > vistors[i+1]:
            record_breaking_days += 1
            last_breaking_days = vistors[i]
    return record_breaking_days

def main():
    test_cases = int(input())
    for test_case in range(1, test_cases + 1, 1):
        number_of_days = int(input())
        vistors = list(map(int, input().split()))

        ans = number_of_record_breaking_days(number_of_days, vistors)

        print("Case #{}: {}".format(test_case, ans))

if __name__ == "__main__":
    main()
