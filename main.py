from store import Checkout
from store.references import FilePath

rules = FilePath.RULES_PATH.value

co = Checkout(rules)
co.scan('nsh')
co.scan('nsh')
co.scan('nsh')
co.scan('mch')
co.scan('cac')

co.scan('stv')
co.scan('stv')
co.scan('stv')
co.scan('stv')
co.scan('stv')

co.total()