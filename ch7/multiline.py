#multiline.p
'''
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
'''

import re
p = re.compile("^python\s\w+",re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
