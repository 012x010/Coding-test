a, b, c = map(int, open(0).read().split())

if a + b + c != 180:
    print("Error")
elif a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif a == b or b == c or c == a:
    print("Isosceles")
else:
    print("Scalene")