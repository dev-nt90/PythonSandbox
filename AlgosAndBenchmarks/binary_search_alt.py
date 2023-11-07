def binary_search(data, followers):
    low = 0
    high = len(data) - 1

    while(low <= high):
        median = (low+high) // 2
        
        if(data[median]["followers"] < followers):
            low = median + 1
        else:
            high = median - 1

        if(low != len(data) and data[low]["followers"] == followers):
            return data[low]["name"]

    return None


def test(data, followers):
    name = binary_search(data, followers)
    print(f"Searching for: {followers}")
    print(f"Found: {name}")
    print("====================================")


def main():
    test_data = [
        {"name": "John", "followers": 5},
        {"name": "Jane", "followers": 10},
        {"name": "James", "followers": 15},
        {"name": "Judy", "followers": 20},
        {"name": "Jenny", "followers": 25},
        {"name": "Jasper", "followers": 30},
        {"name": "Jack", "followers": 35},
        {"name": "Jill", "followers": 40},
        {"name": "Bob", "followers": 45},
        {"name": "Borice", "followers": 50},
        {"name": "Boris", "followers": 55},
        {"name": "Donald", "followers": 60},
        {"name": "Doris", "followers": 65},
        {"name": "Derek", "followers": 70},
        {"name": "Diana", "followers": 75},
        {"name": "Dennis", "followers": 80},
        {"name": "Daisy", "followers": 85},
        {"name": "Duke", "followers": 90},
        {"name": "Duke", "followers": 95},
        {"name": "Duke", "followers": 100},
    ]
    to_search = [50, 40, 30, 20, 5000]
    for v in to_search:
        test(test_data, v)


main()
