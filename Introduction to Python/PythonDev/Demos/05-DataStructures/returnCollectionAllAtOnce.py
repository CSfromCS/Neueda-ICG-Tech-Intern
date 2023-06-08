# Return a collection of numbers from user.
def getNums():
    nums = []
    while True:
        num = int(input("Number? "))
        if num == -1 :
            break
        nums.append(num)
    return nums

# Client code.
nums = getNums()
for n in nums:
    print("  %d" % n)
    