#Program 3 With a single integer as the input, generate the following until a = x
def generate_series(a):
    if a % 2 == 0:
        a -= 1
    series = [2 * i - 1 for i in range(1, a + 1)]
    return ", ".join(map(str, series))

a = int(input("Enter a positive integer: "))
print(f"Output: {generate_series(a)}")
