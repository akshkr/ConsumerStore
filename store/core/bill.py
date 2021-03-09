from ast import literal_eval


class BillProcessor:
    def __init__(self, items, rules):
        self.items = items
        self.rules = rules

        self.checkout_items = dict()
        self.free_items = dict()

    def _count_items(self):
        self.checkout_items = {x: {'qty': self.checkout_items.count(x)} for x in set(self.checkout_items)}

    def _check_total(self, item, qty):
        price = list(self.items.loc[self.items['ITEM_ID'] == item]['PRICE'])[0] * qty

        return price

    def _apply_discount(self, item, item_dict):
        rule = self.rules.loc[self.rules['ITEM_ID'] == item]
        if not rule.empty:
            rule = rule.to_dict(orient='records')[0]

            if item_dict['qty'] < rule['MINIMUM_QTY']:
                return item_dict

            if rule['DISCOUNT_PERCENT'] > 0:
                item_dict['total'] *= ((100-rule['DISCOUNT_PERCENT'])/100)
            elif rule['NEW_PRICE'] > 0:
                item_dict['total'] = rule['NEW_PRICE'] * item_dict['qty']
            elif rule['FREE_ITEM_QTY'] != 0:
                total_free_nos = int(item_dict['qty']/rule['MINIMUM_QTY'])
                price = list(self.items.loc[self.items['ITEM_ID'] == item]['PRICE'])[0]
                item_dict['total'] -= total_free_nos*price

            elif literal_eval(rule['FREE_ITEM_ID']):
                for i in literal_eval(rule['FREE_ITEM_ID']):
                    self.free_items[i] = {'qty': int(item_dict['qty']/rule['MINIMUM_QTY']), 'total': 0}

            return item_dict

        else:
            return item_dict

    def process(self, item_list):
        self.checkout_items = item_list
        self._count_items()
        # print(self.checkout_items)
        # print(self.items)
        # print(self.rules)
        for item, details in self.checkout_items.items():
            self.checkout_items[item].update({'total': self._check_total(item, details['qty'])})
            self.checkout_items[item] = self._apply_discount(item, details)

        print(self.checkout_items)
        print(self.free_items)
        # Target
        # KEY(item) : VALUE {qty: , total}
        # print(self.checkout_items)
