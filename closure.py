def closer(num):
    def actual(x):
        return num**x

    return actual


a = closer(4)
print(a(4))


# Lets understand how closer work:


# You make a function called power that takes an argument num.
def power(num):
    def value(val):
        return (
            val**num
        )  # Inside you create another function called value that takes another argument val and it does val to the power of num

    # so when you call power(num) it gives you a new function value that remembers num
    return value


a = power(4)  # Now a remembers 4 as num
print(a(3))