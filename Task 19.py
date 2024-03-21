from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class LoginSauce:
   """
   This class is used to login into the https://www.saucedemo.com/ webpage using the username and password

   url = https://www.saucedemo.com/
   username = standard_user
   password = secret_sauce
   """

   def __init__(self, url="https://www.saucedemo.com/", username="standard_user", password="secret_sauce"):
       self.url = url
       self.username = username
       self.password = password
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       """
       This method is to open up the chrome browser with the URL and makes the browser to go fullscreen.
       """
       self.driver.get(self.url)
       sleep(3)
       self.driver.maximize_window()


   def quit(self):
       """
       This method is used to close the webbrowser
       """
       self.driver.quit()

   def login(self):
       self.boot()

       """
       To fill the username and password
       """
       self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
       sleep(3)
       self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
       sleep(3)
       self.driver.find_element(by=By.ID, value="login-button").click()
       sleep(3)

   def get_title(self):
       """
       This method fetches the title of the  webpage.
       """
       try:
           title = self.driver.title
           print("Page Title:", title)
           return title
       except Exception as e:
           print("Failed to fetch page title", e)

   def get_current_url(self):
       """
       This method fetches the current URL of the webpage.
       """
       try:
           current_url = self.driver.current_url
           print("Current URL:", current_url)
           return current_url
       except Exception as e:
           print("Failed to fetch current URL", e)

   def save_page_contents(self, filename="Webpage_task_11.txt"):
        """
        This method extracts the entire contents of the webpage and saves it into a text file.
        """
        try:
            page_contents = self.driver.page_source
            with open(filename, "w", encoding="utf-8") as file:
                file.write(page_contents)
            print(f"Webpage contents saved to '{filename}'")
        except Exception as e:
            print("Failed to save webpage contents", e)



obj = LoginSauce()
obj.login()
obj.get_title()
obj.get_current_url()
obj.save_page_contents()
obj.quit()

"""
Output- 
Page Title: Swag Labs
Current URL: https://www.saucedemo.com/inventory.html
Webpage contents saved to 'Webpage_task_11.txt'
"""