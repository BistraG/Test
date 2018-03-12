from time import sleep
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to Fluxday demo page
driver.get("http://demo.fluxday.io/users/sign_in")
#assert Fluxday demo page is successfully opened
assert "Fluxday" in driver.title

#assert Login with valid admin credentials
username = driver.find_element_by_id("user_email")
password = driver.find_element_by_id("user_password")
username.send_keys("admin@fluxday.io")
sleep(1)
password.send_keys("password")
sleep(2)
btn_login = driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[3]/button')
btn_login.click()
sleep(2)
btn_admin = driver.find_element_by_link_text("Admin User")
assert btn_admin.text == "Admin User"

#click on Departments
btn_departments = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[3]/a')
btn_departments.click()
sleep(3)
list_departments = driver.find_elements_by_xpath('//*[@id="pane2"]/div[2]')
#assert List of departments is shown
count_departments = len(list_departments)
assert count_departments > 0

#Click on the button "Create Department"
btn_create_department = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/a[1]')
btn_create_department.click()
sleep(3)
form = driver.find_element_by_xpath('//*[@id="new_project"]/div[3]/div[1]')
#assert that filling form appears
assert form.text == "Department"

#Fill the form
title = driver.find_element_by_xpath('//*[@id="project_name"]')
title.send_keys("Chemistry")
code = driver.find_element_by_xpath('//*[@id="project_code"]')
code.send_keys("dasda")
url = driver.find_element_by_xpath('//*[@id="project_website"]')
url.send_keys("http://some.com/")
description = driver.find_element_by_xpath('//*[@id="project_description"]')
description.send_keys("Vdhsjkadhsajk")
manager = driver.find_element_by_xpath('//*[@id="new_project"]/div[2]/div[6]/div[1]/label')
manager.click()
employee1 = driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[3]')
employee1.click()
#assert the form is filled

#click on button "Save"
btn_save = driver.find_element_by_xpath('//*[@id="new_project"]/div[3]/div[2]/input')
btn_save.click()
sleep(3)

#The information of the added Department appear on the page
list_departments = driver.find_elements_by_xpath('//*[@id="pane2"]/div[2]')
#assert "Chemistry" in list_departments
added_department = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/a[2]/div/div[2]/div[1]')
assert added_department.text == "Chemistry"

driver.quit()

