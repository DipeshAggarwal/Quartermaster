init python:

    class Eat(Action):

        def __init__(self, actor, item):
            self.actor = actor
            self.item = item

        def __call__(self):
            self.actor.add_buff(self.item.buff)
            store.inventory.use_item(self.item)
