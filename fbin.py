### chap07/fbin.py
'''Convert a decimal fraction into a binary string'''
import sys

# Grab input values
n = float(input("Decimal fraction to convert: "))
bits = int(input("Size of significand in bits: "))

# Error checking
if n < 0.0 or n >= 1.0:
    sys.exit("ValueError: target must be in the range [0.0, 1.0)")

# Initialize our bounds and our current best estimate
upper = 1.0
lower = 0.0
best = lower  # with 0 bits used, our best estimate is 0
encoding = ''

for i in range(1, bits+1):
    # Our new estimate always adds a least-significant one bit to
    # the end of our current lower bound, i.e., move up the value
    # below the target number.
    new_guess = lower + (2.0 ** -i)

    # Update the correct bound, depending upon whether the new
    # estimate overshot the target or not.
    if new_guess <= n:
        lower = new_guess
        encoding += '1'
    else:
        upper = new_guess
        encoding += '0'

    # And now update which of these is our current best estimate
    if n - lower < upper - n:
        best = lower
    else:
        best = upper

    if best == n:
        break

    # Print how we've done so far
    units = 'bit' if i == 1 else 'bits'
    print(f'With {i} {units}, {n} is between {lower} and {upper}')

print(f"\nWith maximum {bits} bits of encoding for n = {n},")
if best == n:
    print(f"  the EXACT encoding is '0b0.{encoding}'")
else:
    print(f"  the closest encoding is '0b0.{encoding}'")
print(f"  which has a decimal value of {best}")