
# input
n=int(input('n : '))
# # 3.1
# for i in range(1,n+1):
#     print('*'*i)
# # 3.2
# for i in range(1,n+1):
#     print('{}{}'.format(' '*(n-i),'*'*i))
#
# #3.3
#     j=1
# for i in range(1,n+1):
#     if i==1:
#         print('{}*{}'.format(' '*(n-1),' '*(n-1)))
#     else:
#         print('{}*{}*{}'.format(' '*(n-i),' '*(j),' '*(n-i)))
#         j = j + 2
#
# #3.4
# k=n-2
# for i in range(1,n+1):
#     if n%2!=0:
#         if i<int(n/2)+1:
#             print('{}*{}*{}'.format(' ' * (i-1), ' ' * (k), ' ' * (i-1)))
#             k = k - 2
#         elif i==int(n/2)+1:
#             print('{}*{}'.format(' '*int((n-1)/2),' '*int((n-1)/2)))
#         elif i>int(n/2)+1:
#             k=abs(k)
#             print('{}*{}*{}'.format(' ' * (n - i), ' ' * (k), ' ' * (n - i)))
#             k=k+2
#     if n%2==0:
#         if i<=n/2:
#             print('{}*{}*{}'.format(' ' * (i-1), ' ' * (k), ' ' * (i-1)))
#             k = k - 2
#         elif i>n/2:
#             k = k + 2
#             print('{}*{}*{}'.format(' ' * (n - i), ' ' * (k), ' ' * (n - i)))

# # 3.5
# k=0
# j=1
# for i in range(1,n+1):
#     # n is odd
#     if n % 2 != 0:
#         if i==1 or i==n:
#             space=int(n/2)
#             print('{}*{}'.format(' '*space,' '*space))
#         elif i==int(n/2)+1:
#             print('*'*n)
#         elif i<int(n/2)+1 :
#             star=i+i-1
#             space=int((n-star)/2)
#             print('{}{}{}'.format(' '*space,'*'*star,' '*space))
#         elif i>int(n/2)+1 :
#             k=k+2
#             star=n-k
#             space=int((n-star)/2)
#             print('{}{}{}'.format(' '*space,'*'*star,' '*space))
#     # n is even
#     if n % 2 == 0:
#         if i==1 or i==n:
#             space=int((n-1)/2)
#             print('{}*{}'.format(' '*space,' '*space))
#         elif i<=n/2 :
#             star=i+i-1
#             space=int((n-star)/2)
#             print('{}{}{}'.format(' '*space,'*'*star,' '*space))
#         elif i>n/2 :
#             star=n-j
#             space=int((n-star)/2)
#             print('{}{}{}'.format(' '*space,'*'*star,' '*space))
#             j=j+2
# str='A+B+E+C+D'
# for i in range(0,n+1):
#     if n==1:
#         print('+')
#     else:
#         j=i+3
#         a=str[i:j]
#         i=j
#         print(a)