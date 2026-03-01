
import sys
import builtins

with open('worklife', 'w+') as f:
    f.write('he is speaking right now')
    print(f.seek(0))
    f.seek(0)
    print(f.read)






