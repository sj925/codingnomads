# Adapt your Generator expression from the previous exercise:
# Add a floor division by 1111 on it.
# What numbers do you get?


nums = range(1, 1000000)
gen = ((num, num // 1111) for num in nums if num % 1111 == 0)
print(gen)
print(list(gen))