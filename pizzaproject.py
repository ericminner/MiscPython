meal_str = []
salad_str = []


def select_meal():
    meal = input("Hello, would you like a pizza or salad? Say 'done' when finished: ")
    meal = meal.lower()

    if meal == 'done':
        if meal_str == None:
            print("Your order is a {} salad with {} dressing".format(salad(), dressing()))
            another_order = input("Would you like to place another order?: ")
            if another_order == 'yes':
                select_meal()
            if another_order == 'no':
                print("Your order has been processed. Goodbye.")

        elif salad_str == None:
            print("Your order is a {} pizza with {}".format(select_meal(), toppings()))
            another_order = input("Would you like to place another order?: ")
            if another_order == 'yes':
                select_meal()
            if another_order == 'no':
                print("Your order has been processed. Goodbye.")

        elif meal_str and salad_str != None:
            print("Your order is a {} pizza with {} and a {} salad with {} dressing".format(select_meal(), toppings(),
                                                                                            salad(), dressing()))
            another_order = input("Would you like to place another order?: ")
            if another_order == 'yes':
                select_meal()
            if another_order == 'no':
                print("Your order has been processed. Goodbye.")

    while meal != 'done':
        if meal == "pizza":
            meal_str.append(meal)
            pizza()
        elif meal == "salad":
            salad_str.append(meal)
            salad()
        else:
            print("Invalid input")
            select_meal()

    return meal_str, salad_str


def pizza():
    size = input("Small, medium, or large?: ")
    size = size.lower()
    size_str = []
    if size == "small" or "medium" or "large":
        size_str.append(size)
        toppings()
    else:
        print("Invalid input")
        pizza()
    return size_str


def toppings():
    tops = input("What toppings would you like? Select up to two from pepperoni, sausage, or mushrooms: ")
    tops = tops.lower()
    tops_str = []
    toppings_list = ["pepperoni", "sausage", "mushrooms"]

    while tops != 'done':
        if tops in toppings_list:
            tops = input("What toppings would you like? Select up to two from pepperoni, sausage, or mushrooms: ")
            tops = tops.lower()
            tops_str.append(tops + ' and ')
        else:
            print("Invalid input")
            toppings()

    if tops == 'done':
        select_meal()

    return tops_str


def salad():
    sal = input("Would you like a garden or greek salad?: ")
    sal = sal.lower()
    sal_str = []
    if sal != 'garden' or 'salad':
        print("Invalid input.")
        salad()
    else:
        sal_str.append(sal)
        dressing()
    return sal_str


def dressing():
    dress = input("Would you like ranch or blue cheese dressing?: ")
    dress = dress.lower()
    dress_str = []
    dress_choice = ['ranch', 'blue cheese']

    if dress not in dress_choice:
        print("Invalid input.")
        dressing()

    else:
        dress_str.append(dress)
        select_meal()

    return dress_str


select_meal()