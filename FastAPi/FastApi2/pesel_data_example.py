# import datetime
# pesel = "122311678901"

# year = int(pesel[2:4])
# if year in range(81,92): year = 1800
# elif year in range(1,12): year = 1900
# elif year in range(21,32): year = 2000
# elif year in range(41,52): year = 2100
# elif year in range(61,72): year = 2200

# date_t = datetime.date(int(pesel[0:2])+year, int(pesel[2:4]), int(pesel[4:6]))
# print(date_t)


# import datetime
# pesel = "00290536128"
# year_num = int(pesel[2:4])

# a = 1
# b = 12
# year = 1900
    
# for i in range(4) :
#     if year_num in range(a,b): year 
#     else:
#         a += 20
#         b += 20 
#         year += 100

# if year_num > 12: year_num = year_num % 20

# date_t = datetime.date(int(pesel[0:2]) + year, year_num, int(pesel[4:6]))
# print(date_t)
