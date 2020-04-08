#leap year
year=int(input('Enter year : '))
if year%400==0 or (year%400!=0 and year%100!=0 and year%4==0):
    print(year,'-> true')
else:
    print(year, '-> flase')