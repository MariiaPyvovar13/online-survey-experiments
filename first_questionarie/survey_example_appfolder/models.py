from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    #we will only come to the group class when we look at advanced methods
    pass


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    entry_question = models.StringField(label="Your full name", required=True)
    age_question = models.IntegerField(label="Full age", required=True)                          
    study_field = models.StringField(label="What is your field of study?",
                                     choices=["Economics",
                                              "Politics and Administration",
                                              "SEDS",
                                              "Computer Science",
                                              "Linguistics",
                                              "Other"], 
                                              required=True)
    rating = models.StringField(label="How satisfied are you with your study program? (1 - very unsatisfied, 5 - very satisfied)",
                                choices=["1",
                                         "2",
                                         "3",
                                         "4",
                                         "5"],
                                         required=True)
    agreemen_quest = models.BooleanField(label="Do you agree that your answers will be used in future research?",
                                         choices=[(True, "Yes"), (False, "No")],
                                         required=True)

