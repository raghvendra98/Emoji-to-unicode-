from itertools import chain
# import numpy as np
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

ttf = TTFont('db_hindi_mast_4.ttf')

chars = chain.from_iterable([y + (Unicode[y[0]],) for y in x.cmap.items()] for x in ttf["cmap"].tables)
chars1=(list(chars))
for i in range(len(chars1)):
    print(chars1[i])


# Use this for just checking if the font contains the codepoint given as
# second argument:
#char = int(sys.argv[2], 0)
#print(Unicode[char])
#print(char in (x[0] for x in chars))
# array = np.array(chars1)
# print(array)

ttf.close()