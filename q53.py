import random

lst = "Ana,Carlos,Pedro,Beatriz,Maria".split(",")
RNG = random.randint(0,len(lst)-1)

print(f"O lider e: {lst[RNG]}")