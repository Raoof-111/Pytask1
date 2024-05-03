




# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]
# nums = []
# for i in range(5):
#     num = int(input(f"Zəhmət olmasa {i+1}-ci ədədi daxil edin: "))
#     nums.append(num)
# nums.sort()
# print("Sıralanmış ədədlər:", nums)








# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin.
# Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 
 
# col = input("Zəhmət olmasa bir cümlə daxil edin: ")
# le = [i for i in col if i.isalpha()]
# le.sort()
# print( ''.join(le))









#3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13

# tebrikler . 4 cehdde 13 reqemeni tapdiz

# n = 15
# cehd = 0

# while True:
#     num = int(input("Ədədi daxil edin: "))
#     cehd += 1
#     if num == n:
#         print(f"{cehd} cəhddə tapdınız.")
#         break







# 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)

# for num in range(1, 100):
#     if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#         print(num, end=" ")