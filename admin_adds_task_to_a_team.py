from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from time import sleep
# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to Fluxday demo page
driver.get("http://demo.fluxday.io/users/sign_in")
assert "Fluxday" in driver.title

#Login with valid admin credentials
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


#In the menu click on "Team"
btn_team=driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[4]/a')
btn_team.click()
sleep(4)
list_teams = driver.find_elements_by_xpath('//*[@id="pane2"]')
countTeams = len(list_teams)
assert countTeams > 0

#From Testing,click on the button "Add task"
btn_add_task = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/div[4]/div[3]/a[2]')
btn_add_task.click()
sleep(4)
form_task = driver.find_element_by_xpath('//*[@id="new_task"]/div[3]/div[1]')
assert form_task.text == "Task"

#Fill the form
field_title = driver.find_element_by_xpath('//*[@id="task_name"]')
field_title.send_keys("Project 123456")

field_description = driver.find_element_by_xpath('//*[@id="task_description"]')
field_description.send_keys("Maintenance")

calendar = driver.find_element_by_xpath('/html/body/div[3]')

start_date = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]')
sleep(3)
#start_date.click()

field_end_date =driver.find_element_by_id("task_end_date")
field_end_date.click()
end_date = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/table/tbody/tr[4]/td[3]')
#end_date.click()
sleep(3)

field_priority = driver.find_element_by_xpath('//*[@id="new_task"]/div[2]/div[6]/div/div[1]/label')
field_priority.click()
sleep(3)
field_priority.find_element_by_xpath('//*[@id="task_priority"]/option[2]').click()
sleep(3)

#Click on the button "Create Task"
btn_create_task = driver.find_element_by_xpath('//*[@id="new_task"]/div[3]/div[2]/input')
btn_create_task.click()
sleep(3)

project_name = driver.find_element_by_xpath('//*[@id="pane3"]/div[2]/div/div[1]/div[2]')
assert project_name.text == "Project 123456"

driver.quit()






