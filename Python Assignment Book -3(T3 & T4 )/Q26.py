'''What is the output of the following codes:
(i) def foo():
try:
return 1
finally:
return 2
k = foo()
print(k)
(ii) def a():
try:
f(x, 4)
finally:
print('after f')
print('after f?')
a()'''
def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)

def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')

a()

#Output
'''"C:\Program Files\Python311\python.exe" "C:\Users\yogit\Desktop\consultadd_python_training\Python\Python Assignment Book -3\Q26.py" 
2
after f
after f?
Traceback (most recent call last):
  File "C:\Users\yogit\Desktop\consultadd_python_training\Python\Python Assignment Book -3\Q26.py", line 32, in <module>
    a()
  File "C:\Users\yogit\Desktop\consultadd_python_training\Python\Python Assignment Book -3\Q26.py", line 27, in a
    f(x, 4)
    ^
NameError: name 'f' is not defined

Process finished with exit code 1'''
