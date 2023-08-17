from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import os
import re
import shutil
from unidecode import unidecode

################################################
# Modify these values according to your needs
################################################

# Page number on which to start the extractions
new_value = 1

# Replace these with your actual login credentials
username = "{USERNAME}"
password = "{PASSWORD}"

# Path to the Edge WebDriver executable
webdriver_path = r"C:\Users\{USER}\Downloads\edgedriver_win32\msedgedriver.exe"

# Portal URL to Login
login_url = "https://{WEBSITE_URL}"

# Base URL for the user list
base_url = "https://{WEBSITE_URL}/Web/Users/"

################################################
################################################


# Function to sanitize a filename for saving files
def sanitize_filename(filename):
    # Transliterate Unicode characters into plain ASCII characters
    filename = unidecode(filename)
    # Replace any remaining non-ASCII characters with underscores
    filename = re.sub(r'[^\x00-\x7F]', '_', filename)
    # Replace characters not allowed in file names with underscores
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Remove trailing spaces from the filename
    filename = filename.strip()
    return filename

# Initialize the WebDriver
driver = webdriver.Edge(executable_path=webdriver_path)

# Perform login
driver.get(login_url)
username_input = driver.find_element_by_id("LoginInput")
password_input = driver.find_element_by_id("PasswordInput")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = driver.find_element_by_id("AuthButton")
login_button.click()
time.sleep(3)

# Navigate to the user list
driver.get(base_url)

# Execute a JavaScript script to initiate the search query
button_script = "window.ctl00_PageContentHolder_userListGrid.launchSearchQuery();"
driver.execute_script(button_script)
time.sleep(3)

while True:
    time.sleep(3)

    # Find user links on the page
    user_links = driver.find_elements_by_xpath("//a[contains(@href, '/Web/Users/UserFolder?')]")
    unique_user_links = set()

    # Loop through user links to process user folders
    for user_link in user_links[:-1]:
        user_link_url = user_link.get_attribute('href')
        if user_link_url not in unique_user_links:
            unique_user_links.add(user_link_url)

            # Open user link in a new tab
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(user_link_url)
            time.sleep(2)

            # Extract user's name from the folder page
            user_name_element = driver.find_element_by_class_name("info.user-name")
            user_name = user_name_element.text.strip()
            user_name = sanitize_filename(user_name)

            # Find download links in the user folder
            download_links = driver.find_elements_by_xpath("//a[contains(@href, '/Web/downloadCertificate?')]")
            i = 0

            # Loop through download links to download files
            for download_link in download_links:
                download_directory = rf"C:\Users\L3x_\Downloads\{user_name}"
                if not os.path.exists(download_directory):
                    os.makedirs(download_directory)

                driver.execute_script("window.open(arguments[0], '_blank');", download_link.get_attribute('href'))
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(5)

                source_folder = r"C:\Users\L3x_\Downloads"
                destination_folder = rf"C:\Users\L3x_\Downloads\{user_name}"
                time.sleep(0.5)
                get_last_created_file(source_folders, destination_folder)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    time.sleep(3)

    # Move to the next page of user listings
    element = driver.find_element_by_class_name("k-textbox")
    new_value += 1
    print(new_value)
    element.clear()
    element.send_keys(new_value)
    element.send_keys(Keys.ENTER)

# Close the WebDriver when finished
driver.quit()