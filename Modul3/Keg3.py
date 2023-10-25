random_list = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
    3.1,
    2.7,
    5.5,
    107,
    41,
    12,
    "Hello",
    "Python",
    "world",
    "AI"
]

# Filter untuk memisahkan nilai float, int, dan string
filtered_float = list(filter(lambda x: isinstance(x, float), random_list))
filtered_int = list(filter(lambda x: isinstance(x, int), random_list))
filtered_str = list(filter(lambda x: isinstance(x, str), random_list))


# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int(x):
    x = str(x)
    if len(x) == 1:
        return {'ratusan': 0, 'puluhan': 0, 'satuan': int(x)}
    elif len(x) == 2:
        return {'ratusan': 0, 'puluhan': int(x[0]), 'satuan': int(x[1])}
    else:
        return {'ratusan': int(x[0]), 'puluhan': int(x[1]), 'satuan': int(x[2])}


mapped_int = list(map(map_int, filtered_int))

# Output
print("Data Float :", filtered_float)
print("Data Int :")
for item in mapped_int:
    print(item)
print("Data String :", filtered_str)
