x = 5
print(x)

x="PYTHON"
print(x)

a="hello" # renzoku
print(3*a)

print("kayama" + "yoki" ) # renketu

name = "kayama"  
print("My name is" + name)


string_price = "1000"
price = 500

total_price = int(string_price) + price # use int
print(total_price)

li =[]
li.append("python")
print(li)
li.append("php")
print(li)


profile = {"name":"yoki","email":"yoki@gmail.com"}
print(profile["name"])

profile["gender"] = "male"
print(profile)

for i in range(10):
    if i%2==0:
        print("{} is even.".format(i))
    else:
        print("{} is odd.".format(i))


score = 80
if score > 78:
    print("ok")
else:
    print("bad")

score = 100
if score == 100:
    print("full")
elif score > 85:
    print("ok")
else:
    print("bad")



for i in ["apple", "banana", "lemon"]:
    print(i)


for i in range(10):
    print(i)


data = [20,40,60,80]
for d in data:
    print(d)


sum_d = 0
for d in data:
    sum_d += d
print(sum_d)


sum_d = 0

for d in data:
    sum_d += d
else:
    print(sum_d)


for i in range(10):
    if i == 3:
        continue
    print(i)


for i in range(10):
    if i == 3:
       break
    print(i)


print(list(range(101)))