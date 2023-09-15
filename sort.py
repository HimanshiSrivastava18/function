# a=[9,7,3,1,8,4,12,6]
# n=len(a)
# for i in range(n):
#     for j in range(n-i-1):
#         if (a[j]>a[j+1]):
#             a[j],a[j+1]=a[j+1],a[j]
# print(a)

# a=[9,7,3,1,8,4,12,6]
# n=len(a)
# for i in range(n-1):
#     min_index=i
#     for j in range(i+1,n):
#         if (a[j]<a[min_index]):
#             min_index=j
#         a[i],a[min_index]=a[min_index],a[i]
# print(a)
