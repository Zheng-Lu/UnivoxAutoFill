from selenium import webdriver
import random
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path="D:\ChromeDriver")
driver.get('https://surveys.sample-cube.com/survey')


def isExists(css_selector):
    try:
        driver.find_element_by_css_selector(css_selector)
    except NoSuchElementException:
        return False
    return True


def click_choice():
    multiple_choices = "input[name='mat-radio-group-3']"
    if isExists(multiple_choices):
        random.choice(driver.find_elements_by_css_selector(multiple_choices)).click()


if __name__ == "__main__":
    count = 0  # count the pages start from zero
    while True:
        click_choice()
        next_button = f"button#next_{count}[type='button']"
        driver.find_element_by_css_selector(next_button).click()
        count += 1
