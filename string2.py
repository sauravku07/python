a = "Hello"
b = "Hello123"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123@"
g = "1.234"
h = "hello"

print(a, a.isalnum())
print(c, c.isalnum())
print(f, f.isalnum())

print(a, a.isalpha())
print(b, b.isalpha())

print(a, a.isdecimal())
print(g, g.isdecimal())

print(c, c.isdigit())
print(g, g.isdigit())

print(a, a.isnumeric())
print(c, c.isnumeric())

print(h, h.islower())
print(d, d.islower())

print(h, h.isupper())
print(d, d.isupper())

print(h, h.isspace())
print(e, e.isspace())

print(h, h.istitle())
print(b, b.istitle())