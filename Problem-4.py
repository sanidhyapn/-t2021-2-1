#Program-4 Get the total count of number listed in the dictionary which is multiple of [1,2,3,4,5,6,7,8,9]
def count_multiples(input_list):
    result = {i: 0 for i in range(1, 10)} 
    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1  
    return result


input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))


print(count_multiples(input_list))