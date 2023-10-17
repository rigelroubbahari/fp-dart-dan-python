# tugas 1
# # kode1
# def sequencegenerator(start, stop):
#     x=[]
#     for i in range(start, stop+1):
#         x.append(i)
#     return x
# print(sequencegenerator(1, 10))
# # kode2
# def fizzbuzz(a, b):
#     x=[]
#     for num in range(a, b):
#         if num % 3 == 0 and num % 5 == 0:
#             x.append('FizzBuzz')
#         elif num % 3 == 0:
#             x.append('Fizz')
#         elif num % 5 == 0:
#             x.append('Buzz')
#         else:
#             x.append(num)
#     return x
# # kode 3
# def twoNumber(l):
#     res = []
#     for i in 1:
#         if l.index(i) == len(l)-1:
#             break
#         z = i + l[i+1]
#         res.append(z)
#     return res

def sequencegenerator(start, stop):
    return list(range(start, stop+1))

def fizzbuzz(a, b):
    return ['FizzBuzz' if num % 15 == 0 else 'Fizz' if num % 3 == 0 else 'Buzz' if num % 5 == 0 else num for num in range(a, b)]

def twoNumber(l):
    return [l[i] + l[i+1] for i in range(len(l)-1)]