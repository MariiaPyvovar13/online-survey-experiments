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
import random

author = 'your names and team objective go here'
doc = 'Your app description goes here'

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        img_and_question = [
            {"image": "img1.png", "question": "What emotions does this sunset evoke in you?", "choices": ["Peace", "Happiness", "Sadness", "Excitement", "Other"]},
            {"image": "img2.png", "question": "Have you ever seen this place?", "choices": ["Yes", "No"]}
        ]
        for p in self.get_players():
            # Randomly assign one image and its question to each player
            selected = random.choice(img_and_question) # Randomly assign one image
            p.selected_image = selected["image"] # Assign the selected image to the player
            p.image_question = selected["question"]  # Assign the corresponding question
            p.choices = selected["choices"]  # Assign the choices for the popout question

class Group(BaseGroup):
    counter = models.IntegerField(initial = 0)
    male_count = models.IntegerField(initial=0)  # Tracks males
    female_count = models.IntegerField(initial=0)  # Tracks females
    male_quota = models.IntegerField(initial=1)  # Limit for males
    female_quota = models.IntegerField(initial=1)  # Limit for females


class Player(BasePlayer):
    #this is the most important feature of this file. We can collect all the variables used on the html pages here
    
#The Variables are structured on the base of pages
    entry_question = models.StringField(label="Your full name", required=True)
    # age_question = models.IntegerField(label="Full age", required=True)
    gender = models.IntegerField()
    age_question = models.IntegerField(label="What is your age?")
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

    agreemen_quest = models.IntegerField()

    # Selecting image
    selected_image = models.StringField()
    image_question = models.StringField()

    popout_reason = models.StringField(
        label="What emotion does this image evoke in you?",
        choices=["Peace", "Happiness", "Sadness", "Excitement", "Other"],
        blank = True
    )

    popout_response = models.StringField(
        label="Why?",
        blank=True
    )

    popout_question = models.StringField(
        label="Have you ever seen this place?",
        choices=["Yes", "No"],
        blank=True
    )

    more_experience = models.StringField(
        label="Great! Can you tell us more about your experience?",
        blank=True
    )

    consider_visited = models.StringField(
        label="It’s beautiful, isn’t it? Have you considered visiting?",
        blank=True
    )

    gender = models.IntegerField()

    screenout = models.BooleanField(initial=0)
    quota = models.BooleanField(initial=0)

    # Popout question
    time_popout = models.StringField(initial="")
    time_popout_end = models.StringField()

    # Screen size
    screen_width = models.IntegerField(initial=-999, label="Screen width")
    screen_height = models.IntegerField(initial=-999, label="Screen height")
