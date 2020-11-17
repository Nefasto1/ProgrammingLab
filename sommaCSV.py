values = []

file = open("shampoo_sales.csv", "r");

value = 0;
for line in file:
    element = line.split(",");
    if element[0] != "Date":
        value += float(element[1]);

print("Somma: {}" .format(value));