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

#In the menu click on "OKR"
btn_okr = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul[2]/li[6]/a')
btn_okr.click()
sleep(2)
#Information for OKR is loaded
info_okr = driver.find_element_by_xpath('//*[@id="pane2"]/div[1]/div[1]/div')
assert info_okr.text  == "OKR"
sleep(2)
#From dropdown menu titled "Admin User" choose "Team Lead"
btn_admin_user = driver.find_element_by_xpath('//*[@id="s2id_okr_user_id"]/a/span[1]')
btn_admin_user.click()
sleep(2)
btn_team_lead = driver.find_element_by_xpath('//*[@id="okr_user_id"]/option[2]')
btn_team_lead.click()
sleep(2)
#Information for the OKRs of Team Lead is shown
info_team_lead = driver.find_element_by_xpath('//*[@id="s2id_okr_user_id"]/a/span[1]')
assert (info_team_lead.text == "Team Lead")

#Click on button "New OKR"
btn_new_okr = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/a[1]')
btn_new_okr.click()
sleep(2)
#Filling form titled "Set OKR for Team Lead" appears
info_team_lead_form = driver.find_element_by_xpath('//*[@id="new_okr"]/div[3]/div[1]')
assert info_team_lead_form.text == "Set OKR for Team Lead"

#Fill the form
name = driver.find_element_by_xpath('//*[@id="okr_name"]')
name.send_keys("Person X")
start_date = driver.find_element_by_xpath('//*[@id="okr_start_date"]')
start_date.click()
sleep(2)
end_date = driver.find_element_by_xpath('//*[@id="new_okr"]/div[2]/div[3]/div[1]/label')
end_date.click()
sleep(2)
objective = driver.find_element_by_xpath('//*[@id="okr_objectives_attributes_0_name"]')
objective.send_keys("To prepare the team for the new Project XZDFG")
key_results1 = driver.find_element_by_xpath('//*[@id="okr_objectives_attributes_0_key_results_attributes_0_name"]')
key_results1.send_keys("All the machines and people ready for Project XZDFG")
key_results2 = driver.find_element_by_xpath('//*[@id="okr_objectives_attributes_0_key_results_attributes_1_name"]')
key_results2.send_keys("f,dasmf,smdfsm")
sleep(3)
#Filled Form

#Click on the button "Save"
btn_save = driver.find_element_by_xpath('//*[@id="new_okr"]/div[3]/div[2]/input')
btn_save.click()

#The information of the added OKR for Team Lead appears on the page
info_added_okr = driver.find_element_by_xpath('//*[@id="pane3"]/div/ol/li')
assert info_added_okr.text == "To prepare the team for the new Project XZDFG"

driver.quit()