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
#assert Login with valid admin credentials
btn_admin = driver.find_element_by_link_text("Admin User")
assert btn_admin.text == "Admin User"

#In the menu click on "Users"
btn_users = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[5]/a')
btn_users.click()
sleep(2)

#list of Users is shown
list_users = driver.find_elements_by_xpath('//*[@id="pane2"]/div[2]')
count_users = len(list_users)
assert count_users > 0

#Click on the button "Add User"
btn_add_user = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/a')
btn_add_user.click()
sleep(2)
#Filling form for new user appears
info_form  = driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div[1]')
assert info_form.text == "Add an employee"

#Fill the form
name = driver.find_element_by_xpath('//*[@id="user_name"]')
name.send_keys("Ivan Petrov")
nickname = driver.find_element_by_xpath('//*[@id="user_nickname"]')
nickname.send_keys("dfsjfsl")
email = driver.find_element_by_xpath('//*[@id="user_email"]')
email.send_keys("ivan@mail.bg")
employee_code= driver.find_element_by_xpath('//*[@id="user_employee_code"]')
employee_code.send_keys("fdksl3")
role = driver.find_element_by_xpath('//*[@id="s2id_user_role"]/a/span[1]')
role.click()
sleep(2)
empl = driver.find_element_by_xpath('//*[@id="user_role"]/option[1]')
empl.click()
sleep(2)
goto_psd_col = driver.find_element_by_xpath('//*[@id="s2id_user_role"]/a/span[1]')
goto_psd_col.click()
sleep(2)
password = driver.find_element_by_xpath('//*[@id="user_password"]')
password.send_keys("12345678")
sleep(2)
confirm_password = driver.find_element_by_xpath('//*[@id="user_password_confirmation"]')
confirm_password.send_keys("12345678")
sleep(2)
managers = driver.find_element_by_xpath('//*[@id="new_user"]/div[2]/div[9]/div[1]/label')
managers.click()
sleep(2)
choose = driver.find_element_by_xpath('//*[@id="select2-drop"]/ul/li[3]/div')
choose.click()
sleep(2)

#Click on the button "Save"
btn_save = driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div[2]/input')
btn_save.click()
sleep(2)

#Appears the added user in the Users list
added_user = driver.find_element_by_xpath('//*[@id="pane3"]/div/div[1]/div[4]/div')
assert added_user.text == "Ivan Petrov"

driver.quit()