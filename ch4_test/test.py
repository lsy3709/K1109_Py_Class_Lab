# a = [1,2,3]
# print(a)
# print(type(a))
# # 리스트 <--> 튜플

# b = tuple(a)
# print("###############")
# print(type(b))
# print(b)

tt = ((1,2,3),(4,5,6),(7,8,9))
print(tt)
print(tt[0][0])
for i in range(0,3):
  for k in range(0,3):
    print (tt[i][k], end=" ")
  print()