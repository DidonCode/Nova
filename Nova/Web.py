from selenium import webdriver

import Voice

class infow():
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='C:/Users/Richard/.wdm/drivers/chromedriver/win32/89.0.4389.23/chromedriver.exe')

	def get_info(self, query):
		self.query = query
		self.driver.get(url="https://www.wikipedia.org")
		search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
		search.click()
		search.send_keys(query)
		enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
		enter.click()

	def read(self):
		textPage = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p')
		textPage2 = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]')
		if textPage.text != "":
			Voice.Speak(textPage.text)
		elif textPage2.text != "":
			Voice.Speak(textPage2.text)

	def close(self):
		self.driver.quit()