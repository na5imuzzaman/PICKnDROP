
class DeliveryCharge:
    def __init__(self):
        pass

    def cost_counting(self, point, unit):
        distance = {'Khagan': 1, 'Charabag': 1.8, 'Savar': 3, 'Mirpur-1': 3.25, 'Newmarket': 4.5, 'Nilkhet': 4.5, 'Panthopath': 4.75, 'Shahbagh': 5, 'Gulistan': 5.5,
                    'Uttara': 4.30, 'Airport': 4.50, 'Dhanmondi': 4.10, 'Shyamoli': 3.50, 'IDB': 4.0}
        dis = distance[point]
        cost = 15
        if unit <= 1:
            unit = 0
        caculated_cost = dis * cost + (dis * cost * .15 * unit)
        return int(caculated_cost)


# place = input("Enter pickup place:")  # testing purpose
# weight = float(input("\nenter Wight:\n"))  # testing purpose
#
# total_cost = cost_counting(distance[place], weight)  # testing purpose
# print("delivery charge:", total_cost)  # testing purpose
