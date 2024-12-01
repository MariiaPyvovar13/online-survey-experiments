from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player
from survey_example_appfolder.HelperFunctions import detect_screenout, detect_quota

#This is the pages.py file. Here we structure how our pages and pagesequence function.
#Each page has its own class where you always specify form_model = Player as we have players for each page
#and we have the form_fields in a list which indicate the variables we have on that page. There will be
#more functionality added here but this is a good start.



class Welcome(Page):
    form_model = Player
    form_fields = ["entry_question"]

class DemoPage(Page):
    form_model = Player
    form_fields = ["gender", "age_question", "study_field", "rating"]

    def before_next_page(self):
        # here we are increasing the counter for each player that goes past the Welcome Page
        self.group.counter += 1

        # we want to detect all the screenouts and the quota reached right away
        detect_screenout(self)
        detect_quota(self)

    def vars_for_template(self):
        return {"participant_label": safe_json(self.participant.label),
                "screenout": safe_json(self.player.screenout),
                "quota": safe_json(self.player.quota),
        }

    # def is_displayed(self):
    #     # Example quota logic: stop showing if Male count reaches 50
    #     male_count = self.subsession.player_set.filter(gender="Male").count()
    #     return male_count < 50

class ImagePage(Page):
    form_model = Player
    form_fields = ["popout_reason", "popout_question"]



class PopoutPage(Page):
    form_model = Player
    form_fields = ["popout_reason",
                   "popout_response",
                   "popout_question",
                   "popout_question",
                   "more_experience",
                   "consider_visited"]

class ScreenSizePage(Page):
    form_model = Player
    form_fields = []  # No fields for direct user input

    def js_vars(player: Player):
        return {}


class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player


class RedirectPage(Page):
    def vars_for_template(self):
        return {"participant_label": safe_json(self.participant.label)}

    # style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player

#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                ImagePage,
                PopoutPage,
                EndPage,
                RedirectPage]