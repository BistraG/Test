from time import sleep
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys

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

#Click on "Support"
btn_support = driver.find_element_by_xpath('//*[@id="pane2"]/div[2]/div[3]/div[1]/a')
btn_support.click()
sleep(4)
title_support = driver.find_element_by_xpath('//*[@id="pane3"]/div/div[2]/div[2]/div')
assert title_support.text == "Support"

#Click on the button with dashed line  "Add members"
btn_add_members = driver.find_element_by_xpath('//*[@id="team-members"]/a')
btn_add_members.click()
sleep(5)
users_list = driver.find_elements_by_xpath('//*[@id="ms-team_user_ids"]/div[1]/ul')
countUsers = len(users_list)
assert countUsers > 0

#from the selection list, choose Employee 1
if driver.find_element_by_xpath('//*[@id="1605-selection"]/span'):
    print("Employee 1 already choosen")
    driver.quit()
else:
 btn_employee1 = driver.find_element_by_xpath('//*[@id="1605-selectable"]/span')
 btn_employee1.click()
 sleep(5)

 #info for added Employee appears
 added_member = driver.find_element_by_xpath('//*[@id="team-members"]/div/div/div[1]/div[2]/a[1]')
 assert added_member.text == "Employee 1"

 #click on button "Save"
 btn_save = driver.find_element_by_xpath('//*[@id="edit_team_4"]/div[3]/div[2]/input')
 btn_save.click()
 sleep(3)

 #close the browser
 driver.quit()


#button = driver.find_element_by_xpath('//div[@id="abc"][@class="xyz"]')
#button.click()
#  get the search textbox
#search_field = driver.find_element_by_id("lst-ib")
# search_field.clear()
#  enter search keyword and submit search_field.send_keys("Selenium WebDriver Interview questions") search_field.submit() # get the list of elements which are displayed after the search # currently on result page using find_elements_by_class_name method lists= driver.find_elements_by_class_name("_Rm") # get the number of elements found print (“Found “ + str(len(lists)) + “searches:”) # iterate through each element and print the text that is # name of the search i=0 for listitem in lists: print (listitem) i=i+1 if(i>10): break # close the browser window driver.quit()
#products = self.driver.find_elements_by_xpath("//h2[@class=‘product-name’]/a")
