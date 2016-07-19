import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
	#Load Installed Extension, Always the partcular extension will be Enabled
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('load-extension=/home/ethiraj.k/.config/google-chrome/Default/Extensions/ihbiedpeaicgipncdnnkikeehnjiddck/1.1_0')
	#Load Installed Extension, Always the partcular extension will be Enabled
	'''chrome_options = Options()
	chrome_options.add_extension('/home/ethiraj.k/.config/google-chrome/Default/Extensions/ihbiedpeaicgipncdnnkikeehnjiddck/1.1_0/')
	chrome_options.add_argument('/opt/google/chrome/default_apps/gmail.crx')
	chrome_options.add_extension('C:\Users\<Your_User_Name>\AppData\Local\Google\Chrome\User Data\Default\Extensions')'''
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def test_1_twitter(self):
        driver = self.driver
        driver.get("https://twitter.com/")
        loginButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]")
	loginButton.send_keys(Keys.RETURN)
	userName = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/div[1]/input")
	userName.send_keys("ethirajit")
	password = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/div[2]/input")
	password.send_keys("mangammal")
        loginButton = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/input[1]")
	loginButton.send_keys(Keys.RETURN)
	assert "Ethiraj" in driver.page_source
	print "Twitter - Pass"

    def test_2_google(self):
        driver = self.driver
        driver.get("https://twitter.com/")
        loginButton = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]")
	loginButton.send_keys(Keys.RETURN)
	userName = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/div[1]/input")
	userName.send_keys("ethirajit")
	password = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/div[2]/input")
	password.send_keys("mangammal")
        loginButton = driver.find_element_by_xpath("/html/body/div[21]/div[2]/div[2]/div[2]/div[2]/form/input[1]")
	loginButton.send_keys(Keys.RETURN)
	assert "Ethiraj" in driver.page_source
	print "Google - Pass"

    def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()
