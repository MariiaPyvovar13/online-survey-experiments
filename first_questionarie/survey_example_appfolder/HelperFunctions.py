import random

def random_number(x, y):
    '''
    method for random integers
    '''  
    rng = random.Random()
    number = rng.randint(x, y)
    return number



'''
we also want to implement some functions to help with the quota checking and 
to have an overwview (counting) who is taking part in our survey.

Generally when it comes to redirecting we distinguish between people who: 
1. took part in the whole survey (and get redirected as success to the provider)
2. people who get screened-out (meaning they did not fulfill a characteristic one agreed upon previously)
3. people who get redirected because the quota is already full

We encode those three different event in three different variables (booleans) to use for redirecting

'''

def detect_screenout(self):
    '''this function will check for characteristics a participant needs to 
    take part in the survey, (f.e. a certain age or being eligible to vote)'''

    if self.player.agreemen_quest == 2: # screen out anybody that disagreed to the terms
        self.player.screenout = 1

def detect_quota(self):
    # Gender quotas
    male_quota = 1
    female_quota = 1

    # Update group counters based on gender
    if self.player.gender == 1:  # Male
        if self.group.male_count >= male_quota:
            self.player.quota = 1  # Quota reached for males
        else:
            self.group.male_count += 1  # Increment male count
    elif self.player.gender == 2:  # Female
        if self.group.female_count >= female_quota:
            self.player.quota = 1  # Quota reached for females
        else:
            self.group.female_count += 1  # Increment female count

# def participant_count(self):
#     '''if we want to count different things we might also implement a function here.
#     For now we are just using the counter we implemented before'''
#     return None