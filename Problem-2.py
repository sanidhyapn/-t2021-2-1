#Program-2 With a single integer as the input, generate the following until a = x 

def generate_odd_numbers(a):
    odd_numbers = []
    for i in range(a):
        odd_numbers.append(2 * i + 1)
    return odd_numbers


a = int(input("Enter a number: "))

result = generate_odd_numbers(a)
print(", ".join(map(str, result)))
