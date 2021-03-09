from store.utils.reader import read_rules, read_items
from store.references import FilePath

items = read_items(FilePath.ITEM_PATH.value)


class Checkout:
    def __init__(self, rules):
        self._rules = read_rules(rules)
        self._item_list = list()
        self.bill = None

    def scan(self, item_id):
        self._item_list.append(item_id)

    def total(self):
        from store.core.bill import BillProcessor
        processor = BillProcessor(items, self._rules)
        processor.process(self._item_list)


