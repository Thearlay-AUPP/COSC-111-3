print("*"*37)
print("Welcome to chunking list application:")
print("*"*37)
chunking_by = []
while True:
    data = input("Enter here the data of your list:")
    chunking_by.append(data)

    more = input("Input here y if you want to add more or n if you want to stop:")
    if more.upper() == "N":
        print(chunking_by)
        break

chunk_size = eval(input("Please input here the chunk size:"))
start = 0
end = len(chunking_by)
print("*"*37)
print(f"Here is your list after chunking by {chunk_size}:    ")
print("*"*37)
for i in range(start, end, chunk_size):
    print(chunking_by[i: i+chunk_size])




