total_evens = 0

for i in range(1,101):
    test_even = i % 2
    if test_even == 0:
        total_evens += i

print(total_evens)
