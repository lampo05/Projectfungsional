random_list = [105, 3.1, "Hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

def a_int(value):
    return isinstance(value, int)

def b_float(value):
    return isinstance(value, float)
def c_string(value):
    return isinstance(value, str)

int_values = {
    value: (value // 100, (value // 10) % 10, value % 10)
    for value in filter(a_int, random_list)
}

float_values = tuple(filter(b_float, random_list))

string_values = list(filter(c_string, random_list))

print("Int (dictionary):")
print(int_values)
print("\nFloat (tuple):")
print(float_values)
print("\nString (list):")
print(string_values)
