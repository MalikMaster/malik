try:
   import requests

except:
   os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]
if bit == '64bit':
    from malik import reg
    reg()
elif bit == '32bit':
    from malik import reg
    reg()
