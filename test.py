import matplotlib.pyplot as plt

numbers = list(range(50))
squares = [number**2 for number in numbers]

print(numbers)
print(squares)

plt.plot(numbers, squares)
plt.title("x*2 for positive integers 0-9")
plt.show()