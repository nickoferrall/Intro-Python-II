# class Item:
#     def __init__(self, item_name, item_description):
#         self.item_name = item_name
#         self.item_description = item_description


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print("That's right!! I've taken it!")

    def on_drop(self):
        print("Yup! I've dropped it!")
