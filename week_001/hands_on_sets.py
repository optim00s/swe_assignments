U = set(range(2, 101))
A = set(x for x in U if x % 2 == 0)
B = set(x for x in U if x % 3 == 0)
C = set(x for x in U if x % 5 == 0 or x % 7 == 0)

answer_a = A & B
print(f"The set of multiples of 2 and 3 - len: {len(answer_a)}\n collection: {sorted(answer_a)}")
answer_b = A | C
print(f"The set of multiples of 2 or 5 or 7 - len: {len(answer_b)}\n collection: {sorted(answer_b)}")
answer_c = B - C
print(f"The set of multiples of 3 that arent multiples of 5 or 7 - len: {len(answer_c)}\n collection: {sorted(answer_c)}")
answer_d = A ^ B
print(f"The set of either multiple of 2 or multiple of 3, not multiple of both - len: {len(answer_d)}\n collection: {sorted(answer_d)}")
answer_e = U - (A | B | C)
print(f"The complement of multiples of 2 or 3 or 5 or 7 - len: {len(answer_e)}\n collection: {sorted(answer_e)}")
