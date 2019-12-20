import os
from httpserver import *
pid = os.fork()
if pid < 0 :
    print(" fail")
elif pid == 0:
    main(1235)
else:
    main(1236)
