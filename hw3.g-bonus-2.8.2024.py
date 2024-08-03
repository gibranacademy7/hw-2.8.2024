import random;

random_numbers = [random.randint(-50, 50) for _ in range(20)];
print("Random list:", random_numbers);

absolute_numbers = list(map(lambda x: abs(x), random_numbers));
print("Absolute values list:", absolute_numbers);
#or:
for item in map(lambda x: abs(x), random_numbers):
    print(item);
