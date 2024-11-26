from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start. 

class Welcome(Page):
    form_model = Player
    form_fields = ["entry_question"]

class DemoPage(Page):
    form_model = Player
    form_fields = ["age_question", "study_field", "rating", "agreemen_quest"]


class ImagePage(Page):
    form_model = Player
    form_fields = ["emotion_choice", "image_response"]


class PopoutPage(Page):
    form_model = Player
    form_fields = ["popout_response", "time_popout"]

    def before_next_page(player: Player, timeout_happened):
        player.time_popout_end = "Recorded when user submits the page"

    def vars_for_template(player: "Player"):
        return {
            "popout_instruction": "Please interact with the popout question before proceeding."
        }

class ScreenSizePage(Page):
    form_model = Player
    form_fields = []  # No fields for direct user input

    def js_vars(player: 'Player'):
        return {}


class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                ImagePage,
                PopoutPage,
                EndPage]