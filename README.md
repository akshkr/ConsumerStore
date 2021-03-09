# ConsumerStore
Consumer store is the interface to process bills and checkout items.

There are two main files:
 - `/items/store_items.csv`: item_id, name and price
 - `/rules/store_rules.csv`: Offer rules can contain free items, x at price of y items<br>
    new price and discount if a minimum quantity is purchased

### Importing Checkout class
`from store import Checkout`

### Feeding store rules
Store rules can be a remote file or the file in the repo

```
from store.references import FilePath
rules = FilePath.RULES_PATH.value
```

### Billing
```
co = Checkout(rules)
items = ['cac', 'mch', 'stv']
for i in items:
    co.scan(i)

```

### Output
```
print(co.total())
print(co.bill)
```