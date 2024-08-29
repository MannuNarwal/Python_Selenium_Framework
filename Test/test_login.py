# Import dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.login_page import *
from Paths.config_tests import *


#1 User verify to launch on browser
def test_open_website():
  driver = getUrlDriver(main_url)

#2 User click on login button on Home page
def test_click_login():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 

#Sign In
#3 User click on SIGN In button without filling email and password
def test_Signin_button():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH,Sign_up_button) 

#4 User click on Email Text Field 
def test_Email_Text_Field():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH,Email_Text_Field) 
  
#5 User enter text in Email Text Field 
def test_Enter_Email():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH,Email_Text_Field) 
  enter_text(driver, By.XPATH, Email_Text_Field, valid_email)
  
#6 User click on Password Text Field 
def test_Password_Text_Field(): 
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH, Password_Text_Field)   
 
#7 User enter text in Password Text Field
def test_Enter_Password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH, Password_Text_Field) 
  enter_text(driver, By.XPATH, Password_Text_Field, valid_Password)
   
  
#8 User Login with valid email and Valid password
def test_valid_email_and_valid_password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH,Email_Text_Field)
  enter_text(driver, By.XPATH, Email_Text_Field, valid_email)
  click_button(driver, By.XPATH, Password_Text_Field)   
  enter_text(driver, By.XPATH, Password_Text_Field, valid_Password) 
  click_button(driver, By.XPATH,Sign_up_button)    
  
  
#9 User Login with invalid email and invalid password
def test_invalid_email_and_invalid_password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH,Email_Text_Field)
  enter_text(driver, By.XPATH, Email_Text_Field, invalid_email)
  click_button(driver, By.XPATH, Password_Text_Field)   
  enter_text(driver, By.XPATH, Password_Text_Field, invalid_password) 
  click_button(driver, By.XPATH,Sign_up_button)   
  
#10 User Login with valid email and invalid password
def test_valid_email_and_invalid_password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH,Email_Text_Field)
  enter_text(driver, By.XPATH, Email_Text_Field, valid_email)
  click_button(driver, By.XPATH, Password_Text_Field)   
  enter_text(driver, By.XPATH, Password_Text_Field, invalid_password) 
  click_button(driver, By.XPATH,Sign_up_button) 
  
  
#11 User Login with invalid email and valid password
def test_invalid_email_and_valid_password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH,Email_Text_Field)
  enter_text(driver, By.XPATH, Email_Text_Field, invalid_email)
  click_button(driver, By.XPATH, Password_Text_Field)   
  enter_text(driver, By.XPATH, Password_Text_Field, valid_Password) 
  click_button(driver, By.XPATH,Sign_up_button)  
  
#forget_button
#12 User click on Forget your Password    
def test_click_forget_password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)

 
#13 User click Submit Button after clicking on forget password button 
def test_Recover_Password_submit_button():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)
  click_button(driver, By.XPATH,Recover_Password_submit_button)
  
  
#14 User click e-mail text box field after clicking forget password button 
def test_Recover_Password_email():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)


#15 User enter e-mail text box field after clicking forget password button 
def test_Recover_Password_email():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)
  
   
#16 user redirected to Recover password page  
def test_Recover_Password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)
  driver = getUrlDriver(recover_password_url)
  
#17 User click Cancel Button after clicking forget password button 
def test_Recover_Password_Cancel_button():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Forget_Password)
  click_button(driver, By.XPATH,Recover_Password_Cancel_button)
  

#Create Account 
#18 User click on Create Account 
def test_Create_Account_button():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)  
  
#19 User click on Sign Up Button on Create account page    
def test_Create_Account_button():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)  
  click_button(driver, By.XPATH, Create_Account_Sign_In_button)
  
#20 User Click on First Name text field after clicking on create account
def test_click_create_Account_First_Name():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_First_name) 
  
#21 User Click on Last Name text field after clicking on create account
def test_click_create_Account_Last_Name():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_Last_name)  
  
#22 User Click on Email text field after clicking on create account
def test_click_create_Account_Email():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_Email) 
  
#23 User Click on Password text field after clicking on create account
def test_click_create_Account_Password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in)
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_password) 
  

#24 User enter on First Name text field after clicking on create account
def test_enter_Create_Account_First_Name():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_First_name)  
  enter_text(driver, By.XPATH, Create_Account_First_name, valid_F_name_1) 
 
#25 User enter on Last Name text field after clicking on create account
def test_enter_create_Account_Last_Name():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_Last_name)  
  enter_text(driver, By.XPATH, Create_Account_Last_name, valid_L_name_1)
  
#26 User enter on Email text field after clicking on create account
def test_enter_create_Account_email():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_Email) 
  enter_text(driver, By.XPATH, Create_Account_Email, valid_email_2)
  
#27 User enter on Password text field after clicking on create account
def test_enter_create_Account_Password():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_Email) 
  click_button(driver, By.XPATH, Create_Account_password) 
  enter_text(driver, By.XPATH,Create_Account_password , valid_Password_2)
  
#28 User created account with valid name, email and password
def test_click_create_New_Account():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_First_name)
  enter_text(driver, By.XPATH, Create_Account_First_name, valid_F_name_1) 
  click_button(driver, By.XPATH, Create_Account_Last_name)  
  enter_text(driver, By.XPATH, Create_Account_Last_name, valid_L_name_1)
  click_button(driver, By.XPATH, Create_Account_Email) 
  enter_text(driver, By.XPATH, Create_Account_Email, valid_email_2)
  click_button(driver, By.XPATH, Create_Account_password) 
  enter_text(driver, By.XPATH,Create_Account_password , valid_Password_2)
  click_button(driver, By.XPATH, Create_Account_Sign_In_button)
  
#30 User created account with invalid name, email and password
def test_click_create_New_Account():
  driver = getUrlDriver(main_url)
  click_button(driver, By.XPATH,log_in) 
  click_button(driver, By.XPATH, Create_Account_button)
  click_button(driver, By.XPATH, Create_Account_First_name)
  enter_text(driver, By.XPATH, Create_Account_First_name, invalid_F_name_1) 
  click_button(driver, By.XPATH, Create_Account_Last_name)  
  enter_text(driver, By.XPATH, Create_Account_Last_name, invalid_L_name_1)
  click_button(driver, By.XPATH, Create_Account_Email) 
  enter_text(driver, By.XPATH, Create_Account_Email, invalid_email_2)
  click_button(driver, By.XPATH, Create_Account_password) 
  enter_text(driver, By.XPATH,Create_Account_password , invalid_Password_2)
  click_button(driver, By.XPATH, Create_Account_Sign_In_button)
  
#NEWSLETTER SUBSCRIPTION 
#31 User click for Newsletter Subscripition button
def test_click_Newsletter_Subscripition_button():
   driver = getUrlDriver(main_url)
   click_button(driver, By.XPATH,log_in) 
   click_button(driver, By.XPATH,Newsletter_Subscripition_button)  
   
#32 User click contact email text box for newsletter subscription  
def test_click_Newsletter_Subscripition_email():
   driver = getUrlDriver(main_url)
   click_button(driver, By.XPATH, log_in) 
   click_button(driver, By.XPATH, Newsletter_Subscripition_Email_button)
   

#33 User enter contact email text box for newsletter subscription  
def test_Newsletter_Subscripition_enter_email():
   driver = getUrlDriver(main_url)
   click_button(driver, By.XPATH, log_in) 
   click_button(driver, By.XPATH, Newsletter_Subscripition_Email_button)   
   enter_text(driver, By.XPATH, Newsletter_Subscripition_Email_button, valid_email_2)
 
#34 User subscribed with invalid contact email text box for newsletter subscription  
def test_Newsletter_Subscripition_invalid_email():
   driver = getUrlDriver(main_url)
   click_button(driver, By.XPATH, log_in) 
   click_button(driver, By.XPATH, Newsletter_Subscripition_Email_button)   
   enter_text(driver, By.XPATH, Newsletter_Subscripition_Email_button, invalid_email_2) 
     
#35 User Subscribed with valid contact email text box for newsletter subscription  
def test_Newsletter_Subscripition_valid_email():
   driver = getUrlDriver(main_url)
   click_button(driver, By.XPATH, log_in) 
   click_button(driver, By.XPATH, Newsletter_Subscripition_button)
   enter_text(driver, By.XPATH, Newsletter_Subscripition_Email_button, valid_email_2)  
   click_button(driver, By.XPATH, Newsletter_Subscripition_Email_button)
   
   