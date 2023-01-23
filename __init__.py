from mycroft import MycroftSkill, intent_handler, AdaptIntent
from mycroft.skills.context import adds_context, removes_context


class FoodOrderer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('orderer.food.intent')
    def handle_food(self, message):
        self.speak_dialog('orderer.food')

        @intent_handler(AdaptIntent("").require('type'))
        def type(self, message):
            food_type = message.data.get('type')
            self.speak('okay I will order a {}'.format(food_type))



def create_skill():
    return FoodOrderer()

