from store import Checkout
from store.references import FilePath

rules = FilePath.RULES_PATH.value

co = Checkout(rules)
# items = ['nsh', 'nsh', 'nsh', 'mch']
# items = ['nsh', 'stv', 'stv', 'nsh', 'stv', 'stv', 'stv']
items = ['cac', 'mch', 'stv']
for i in items:
    co.scan(i)

print(co.total())
print(co.bill)