limit = int(input("Enter the number till which you want the tables: "))
tables_array = []
for i in range(1, limit + 1):
    individual_tables = []
    for j in range (1, 11):
        individual_tables.append((i * j))
    tables_array.append(individual_tables)

for i in range(10):
    for j in range (limit):
        print(f"{j + 1} x {i + 1} = {tables_array[j][i]}".rjust(12), end='\t')
    print("")