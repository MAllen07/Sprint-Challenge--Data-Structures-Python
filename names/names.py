import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\100")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\100")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\100\100{', '.join(duplicates)}\100\100")
print (f"runtime: {end_time - start_time} seconds")

#First test-  runtime: 10.456552982330322 seconds
#Second test - runtime: 0.0015401840209960938 seconds 
