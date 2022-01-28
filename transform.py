import re
import numpy as np
from pyrsistent import b

nf = 'a<=>b'

match = re.search(r"[^<=>^]*", nf)
print(match)
