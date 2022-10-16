def perfNum(n):
    s = 0
    for p in range(1, n):
        if n%p == 0:
            s += p
    if s == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

numb = int(input())
perfNum(numb)