
def fact(number, sumi):
    while number != 1:
        sumi = sumi* number
        number -= 1
    return sumi


k = int(input())
p = int(input())
sumi = 1
print(f"{fact(k, sumi) / fact(p, sumi):.2f}")