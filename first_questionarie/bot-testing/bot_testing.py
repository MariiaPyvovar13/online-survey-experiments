from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string

# this is the session wide link
link = "http://localhost:8000/join/havorure"

def build_driver():
    # Set up the driver
    return webdriver.Chrome() #(ChromeDriverManager().install())

def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return 1
    except NoSuchElementException:
        return 0

def welcome_page(driver):
    # Give input to the entry question - find the element by its id
    entry_question_id = "id_entry_question"
    entry_question_input = "Test Name"
    driver.find_element(By.ID, entry_question_id).send_keys(entry_question_input)
    # next button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()

def demo_page(driver):
    # gender
    # gender = driver.find_elements(By.NAME, "gender")
    # rand_selection = random.randint(0, len(gender) - 1)
    # gender[rand_selection].click()
    if check_exists_by_xpath(driver, '//*[@name="gender"]'):
        gender = driver.find_elements(By.NAME, "gender")
        if len(gender) > 0:
            rand_selection = random.randint(0, len(gender) - 1)
            gender[rand_selection].click()

    # age
    xpath = '//*[@id="id_age_question"]'
    age = random.randint(18,40)
    driver.find_element(By.XPATH, xpath).send_keys(str(age))

    # study
    study_field_dropdown = driver.find_element(By.NAME, "study_field")
    select_study_field = Select(study_field_dropdown)
    options = select_study_field.options
    random_option = random.choice(options)  # Randomly choose one option from the dropdown
    select_study_field.select_by_visible_text(random_option.text)

    # rating
    rating_dropdown = driver.find_element(By.NAME, "rating")
    select_rating = Select(rating_dropdown)
    options = select_rating.options
    random_option = random.choice(options)  # Randomly choose one option from the dropdown
    select_rating.select_by_visible_text(random_option.text)

    # agreement question
    agreement = driver.find_elements(By.NAME, "agreemen_quest")
    rand_selection = random.randint(0, len(agreement) - 1)
    agreement[rand_selection].click()

    # next
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()
    return rand_selection

def image_page_img1(driver):
    """
    Handles the logic for img1.png where `popout_reason` is present.
    """
    popout_reason = driver.find_element_by_id("id_popout_reason")
    if popout_reason:
        popout_reason.send_keys("Reason")  # Example input for popout reason

    popout_response = driver.find_element_by_id("popout_response")
    if popout_response:
        popout_response.send_keys("Additional details about the reason")

    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/button').click()


def image_page_img2(driver):
    """
    Handles the logic for img2.png where `popout_question` is present.
    """
    popout_question = driver.find_element_by_id("id_popout_question")
    if popout_question:
        popout_question.send_keys("Yes")  # Example: Answering "Yes" to the question

    # Handle conditional display logic
    if popout_question.get_attribute("value") == "Yes":
        more_experience = driver.find_element_by_id("more_experience")
        if more_experience:
            more_experience.send_keys("Some experience")  # Example response
    elif popout_question.get_attribute("value") == "No":
        consider_visited = driver.find_element_by_id("consider_visited")
        if consider_visited:
            consider_visited.send_keys("No plans to visit")  # Example response

    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/button').click()

def onlyOneGroup(driver):
    # Find the element by its tag
    driver.find_element(By.TAG_NAME, 'button').click()

def popout_page(driver):
    # Wait until the page loads (adjust timeout if necessary)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Define the options for the dropdowns
    popout_reason_choices = ["Peace", "Happiness", "Sadness", "Excitement", "Other"]
    popout_question_choices = ["Yes", "No"]

    try:
        selected_image = driver.execute_script("return player.selected_image;")
        print(f"Selected image: {selected_image}")
    except Exception as e:
        print(f"Error fetching selected image: {e}")
        return

    # Checking which image was selected
    selected_image = driver.execute_script("return player.selected_image;")
    print(f"Selected image: {selected_image}")

    if selected_image == "img1.png":
        # Handle the case where img1.png is selected
        try:
            # Interact with the popout_reason field
            popout_reason_xpath = "//*[@id='id_popout_reason']"
            popout_reason_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, popout_reason_xpath))
            )
            # Select a random option for popout_reason
            random_reason = random.choice(popout_reason_choices)
            popout_reason_dropdown.send_keys(random_reason)
            print(f"Selected '{random_reason}' in popout_reason dropdown.")

            # Wait for popout_response to appear and verify it's visible
            popout_response_xpath = "//*[@id='popout_response']"
            popout_response = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, popout_response_xpath))
            )
            assert popout_response.is_displayed(), "Popout response should be visible."

            print("Popout response for img1.png verified successfully.")

        except Exception as e:
            print(f"Error handling img1.png: {e}")


    elif selected_image == "img2.png":
        try:
            # Interact with the popout_question field
            popout_question_xpath = "//*[@id='id_popout_question']"
            popout_question_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, popout_question_xpath))
            )

            # Simulate selecting "Yes"
            random_question = random.choice(popout_question_choices)
            popout_question_dropdown.send_keys(random_question)
            print(f"Selected '{random_question}' in popout_question dropdown.")

            # Verify that more_experience is visible and consider_visited is hidden
            more_experience_xpath = "//*[@id='more_experience']"
            consider_visited_xpath = "//*[@id='consider_visited']"

            if random_question == "Yes":
                # Verify that more_experience is visible
                more_experience = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, more_experience_xpath))
                )
                assert more_experience.is_displayed(), "More experience should be visible."

                # Verify that consider_visited is hidden
                consider_visited = driver.find_element(By.XPATH, consider_visited_xpath)
                assert not consider_visited.is_displayed(), "Consider visited should not be visible."

            elif random_question == "No":
                # Verify that consider_visited is visible
                consider_visited = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, consider_visited_xpath))
                )
                assert consider_visited.is_displayed(), "Consider visited should be visible."

                # Verify that more_experience is hidden
                more_experience = driver.find_element(By.XPATH, more_experience_xpath)
                assert not more_experience.is_displayed(), "More experience should not be visible."

            print("Popout question response for img2.png (No) verified successfully.")

        except Exception as e:
            print(f"Error handling img2.png: {e}")

        else:
            print("No valid image selected or selection logic is broken.")

    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()


def end_of_survey(driver):
    # submit button
    driver.find_element(By.XPATH, '//*[@id="form"]/div/button').click()


def run_bots(no_times, link):
    driver = build_driver()  # initialize the driver
    for i in range(no_times):  # go through the survey several times
        driver.get(link)  # open the browser to the url of your survey
        # check if one can do th survey(e.g. if quota is full start page is not shown(in our case 20 participants)
        if check_exists_by_xpath(driver, "//*[@id='id_entry_question']") == 1:
            welcome_page(driver)

        demo_page(driver) # demo-page(gender, age etc)
        # Check if an extra site is shown and process it if present
        if check_exists_by_xpath(driver, '//*[@id="form"]/div/h3') == 1:
            onlyOneGroup(driver)

        if check_exists_by_xpath(driver, "//*[@id='id_popout_reason']"):  # Logic for img1.png
            image_page_img1(driver)
        elif check_exists_by_xpath(driver, "//*[@id='id_popout_question']"):  # Logic for img2.png
            image_page_img2(driver)

        popout_page(driver)

      # check if extra site is shown to you shown
        if check_exists_by_xpath(driver, '//*[@id="form"]/div/h3') == 1:
            onlyOneGroup(driver)
        end_of_survey(driver)
    print("Success!")

run_bots(no_times=20, link=link)
