"""
JSON e Pickle
"""

import json

ret = json.dumps(['produto', {'Playstation 4': {'4TB', 'Novo', '220V', 2340}}])

print(type(ret))
print(ret)