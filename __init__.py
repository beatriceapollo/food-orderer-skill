from mycroft import MycroftSkill, intent_file_handler


class FoodOrderer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('orderer.food.intent')
    def handle_orderer_food(self, message):
        self.speak_dialog('orderer.food')


def create_skill():
    return FoodOrderer()

