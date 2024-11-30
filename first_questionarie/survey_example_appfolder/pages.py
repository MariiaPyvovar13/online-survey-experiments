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

    # def before_next_page(self):
    #     # here we are increasing the counter for each player that goes past the Welcome Page
    #     self.group.counter += 1
    #
    #     # we want to detect all the screenouts and the quota reached right away
    #     detect_screenout(self)
    #     detect_quota(self)

class DemoPage(Page):
    form_model = Player
    form_fields = ["gender", "age_question", "study_field", "rating", "agreemen_quest"]

    # def is_displayed(self):
    #     # Example quota logic: stop showing if Male count reaches 50
    #     male_count = self.subsession.player_set.filter(gender="Male").count()
    #     return male_count < 50

class ImagePage(Page):
    form_model = Player
    form_fields = ["popout_reason", "popout_question"]
# class ImagePage(Page):
#     form_model = Player
#     def get_form_fields(self):
#         if self.player.selected_image == "img1.png":
#             return ["popout_reason"]  # Dropdown for emotions
#         else:
#             return ["popout_question"]  # Yes/No question for img2



class PopoutPage(Page):
    form_model = Player
    form_fields = ["popout_reason",
                   "popout_response",
                   "popout_question",
                   "popout_question",
                   "more_experience",
                   "consider_visited"]

   # def get_form_fields(self):

    #    if self.player.selected_image == "img1.png":
      #      return ["popout_reason", "popout_response"]
     #   elif self.player.selected_image == "img2.png":
       #     # Make sure popout_question is set
        #    if self.player.popout_question == "Have you ever seen this place?":
         #       return ["popout_question"]
          #  if self.player.popout_question == "Yes":
           #     return ["popout_question", "more_experience"]
         #   elif self.player.popout_question == "No":
          #      return ["popout_question", "consider_visited"]
      #  return []

 #   def before_next_page(self):
  #      self.player.time_popout_end = "Recorded when user submits the page"

   # # def vars_for_template(self):
   #      return {
   #          "selected_image": self.player.selected_image,
   #          "popout_instruction": "Please interact with the popout question before proceeding."
   #      }

class ScreenSizePage(Page):
    form_model = Player
    form_fields = []  # No fields for direct user input

    def js_vars(player: Player):
        return {}


class EndPage(Page):
    #style: this is a good example of the style 'CamelCase' that one normally uses for classes
    form_model = Player


class RedirectPage(Page):
    form_model = Player


#Here we define in which ordering we want the pages to be shown. We always start with a Welcome page and end with an End page.
page_sequence = [Welcome,
                DemoPage,
                ImagePage,
                PopoutPage,
                EndPage,
                RedirectPage]