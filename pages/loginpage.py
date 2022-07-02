

class LoginPage():

# All the locators of Login page
    def __init__(self, driver):
        self.driver = driver

        self.username_id = "user-name"
        self.password_id = "password"
        self.login_button_id = "login-button"

    def enter_username(self, username):
        self.driver.find_element("id", self.username_id).clear()
        self.driver.find_element("id", self.username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("id", self.password_id).clear()
        self.driver.find_element("id", self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element("id", self.login_button_id).click()