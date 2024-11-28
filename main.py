from matplotlib import pyplot as plt

size = int(input("Enter the desired number of plot(s): "))
type = input("Type either PLOT or SCATTER or BAR for the graph type: ")
x = []

for i in range(size):
    x.append(i + 1)

y = [i**2 for i in x]

while True: 
    if type.lower() == "plot":
        plt.plot(x, y)
        break
    elif type.lower() == "scatter":
        plt.scatter(x, y)
        break
    elif type.lower() == "bar":
        plt.bar(x, y)
        break
    else:
        type = input("Type either PLOT or SCATTER or BAR for the graph type: ")

plt.show()