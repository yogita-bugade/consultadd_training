'''What is the output of the following code examples?
x=123
i = 0
count = 0
for i in x:
print(i)
while i < 5:
print(i)
i += 1
if i == 3:
break
else:
print(“error”)
while True:
print(count)
count += 1
if count >= 5:
Break'''

#Code 1
x = 123
for i in str(x):
    print(i)

#Output
# 1
# 2
# 3

#Code 2
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

#Output
#0
#1
#2

#Code 3
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
#Output
#0
#1
#2
#3
#4
