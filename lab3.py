# # Lab 3 Ex. 1

# A_set = frozenset([100, 200, 300])
# B_set = frozenset([300, 400, 500])
# C_set = frozenset([500, 600, 700])

# one = A_set.intersection(B_set)
# print(one)

# two = A_set.difference(B_set)
# print(two)

# three = A_set.isdisjoint(B_set)
# print(three)

# four = A_set.union(B_set)
# print (four)

# five = B_set.symmetric_difference(C_set)

# # Ex. 2

# letters_1 = {'D', 'E', 'F', 'G'}
# letters_2 = {'H', 'I'}

# letters_3 = letters_1.copy()
# print(letters_1)

# letters_1.update(letters_2)
# print (letters_1)

# differance = letters_1.difference(letters_2)
# print(differance)

# letters_1.remove('I')
# print(letters_1)

# print(len(letters_1))

# letters_1.discard('I')
# letters_1.discard('E')
# print(letters_1)

# # Ex. 3
# import collections

# months_Dq = collections.deque(['Mar', 'April', 'May'])

# # A - adds to the end
# months_Dq.extend(['June', 'July', 'August'])
# print(months_Dq)

# # B - adds from the left starting feb jan dec mar
# months_Dq.appendleft(['Dec', 'Jan', 'Feb'])
# print(months_Dq)

# # C - removes last item from left "Feb"
# months_Dq.popleft()
# print(months_Dq)

# # D - Removes last item from the right side "August"
# months_Dq.pop()
# print(months_Dq)

# #E - removes the occurance of the string
# months_Dq.remove('June')
# print(months_Dq)

# Ex. 4

# #creating a set
# carolina = set([92, 87, 93, 88])
# raquel = set([88, 92, 81, 97])

# # symmetric.difference returns values that are in either set but not both
# diff = carolina.symmetric_difference(raquel)
# print(diff)

# # display same quiz score using .intersection() returns values that are common to both sets
# common = carolina.intersection(raquel)

# # min(set_name) removes lowest number
# # .remove(name) deletes item from set

# carolina.remove(min(carolina))
# raquel.remove(min(raquel))

# print(carolina)
# print(raquel)

#Ex. 5 
st_A = {'c', 'o', 'm', 'p', 'u', 't', 'e', 'r'}
st_B = {'m', 'u', 't', 'e'}


