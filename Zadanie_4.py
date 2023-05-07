# def div(a, b):
#     result = []
#     for i in range(a+1, b+1):
#         if i % 2 == 0 and i % 3 != 0:
#             result.append(i)
#     return result
#
#
# result = div(0, 20)
# print(result)

def div(a, b):
    return [i for i in range(a + 1, b + 1) if i % 2 == 0 and i % 3 != 0]


result = div(0, 20)
print(result)
