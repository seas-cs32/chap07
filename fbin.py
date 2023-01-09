### chap07/fbin.py
# Convert a decimal fraction into a binary string.  The script expects
# you to input a number between 0 (inclusive) and 1 (exclusive).

import sys

# Grab the target number and max number of encoding bits to use from
# the command line.  The default number of bits to use is 23, which
# corresponds to the fraction part of a single-precisions FP number.
if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.exit("Usage: python3 fbin.py target [encoding-bits]")
elif len(sys.argv) == 3:
    bits = int(sys.argv[2])
else:
    bits = 23
n = float(sys.argv[1])

# Error checking
if n < 0. or n >= 1.:
    sys.exit("ValueError: target must be in the range [0., 1.)")

# Initialize our bounds and our current best estimate
upper = 1.
lower = 0.
best = lower  # with 0 bits used, our best estimate is 0
encoding = ''

for i in range(1, bits+1):
    # Our new estimate always adds a least-significant one bit to the end
    # of our current lower bound, i.e., move up the value below the
    # target number.
    new_guess = lower + (2. ** -i)

    # Update the correct bound, depending upon whether the new estimate
    # overshot the target or not.
    if new_guess < n:
        lower = new_guess
    else:
        upper = new_guess

    # And now update which of these is our current best estimate
    if n - lower < upper - n:
        best = lower
        encoding += '0'
    else:
        best = upper
        encoding += '1'

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