# list datastrucure

my_list = ["toyota", "bmw", "subaru", "range", "nissan"]
my_list.append("mazda")
print(my_list)
print(my_list[0])
my_list[1] = "mercedes"
# mutable
print(f"{my_list[1]} is manufactured in Germany")
print(type(my_list))

# tuple datastructure
my_tuple = ("Banana", "apple", "orange", "mangoes", "apples")
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[-3:-1])
# my_tuple(1)="pineapples"
print(f"I like eating {my_tuple[1]}")
print(len(my_tuple))
my_tuple.count(2)

# set datastructure
my_set = {"python", "java", "c", "ruby", "javascript"}
print(my_set)

# dictionary datastructure
my_dict = {"name": "Yegon", "Age": 30, "Gender": "Male"}
car_info = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2022,
    "color": "Blue",
    "mileage": 15000
}
print(my_dict)
print(my_dict["Age"])
print(my_dict["Gender"])
print(car_info)
print(car_info["mileage"])