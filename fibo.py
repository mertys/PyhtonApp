# fibo sayıları = 0, 1, 1, 2, 3, 5, 8, 13 her sayı kendinden önce gelen sayının toplanması ile elde edilir.
def fibo(n):
    fibosay = [0 , 1 , 1]
    fib1 = 0
    fib2 = 1
    fib3 = 1

    while fib3 < n:
        fibosay.append(fib3)
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2

    return fibosay

fib_say = 0 

for sayı in fibo(50):
    if sayı % 2 ==0:
        fib_say += sayı

print(fib_say)

###############################################################

prev=1
num=1
toplam=0
while num<50:
    new_num=num+prev
    if new_num%2==0:
        toplam+=new_num
    prev=num
    num=new_num
print(toplam)