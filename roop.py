name = "Ted"
for character in name:
    print(character)



people = {
    "G.Bluth II": "A.Development",
    "Barney": "HIMYM",
    "Dennis": "Always Sunny",
}
for character in people:
    print(character)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

for i in range(1,6):
    if i == 3:
        continue
    print(i)


for i in range(1,3):
    print(i)
    for letter in ["a","b","c"]
        print(letter)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)

print(added)

while input('y or n?') != n:
    for i in range(1,6):
        print(i)
