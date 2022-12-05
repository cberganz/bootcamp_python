import sys

if len(sys.argv) == 1:
    print("Usage: python3 exec.py [Arguments list].")
    sys.exit(1)

joinedStr = ' '.join(sys.argv[1:])
print(joinedStr[::-1].swapcase())
