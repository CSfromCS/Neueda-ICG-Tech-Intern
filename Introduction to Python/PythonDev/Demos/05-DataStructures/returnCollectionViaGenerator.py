# Return a collection of numbers from user, one at a time.
def getNums():
    while True:
        num = int(input("Number? "))
        if num == -1 :
            break
        yield num

# Client code.
nums = getNums()
for n in nums:
    print("  %d" % n)
    