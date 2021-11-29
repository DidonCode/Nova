from selenium import webdriver

class music():
	def __init__(self):
		self.driver = webdriver.Chrome(executable_path='C:/Users/Richard/.wdm/drivers/chromedriver/win32/89.0.4389.23/chromedriver.exe')

	def play(self, query):
		self.query = query
		self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
		cookie = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a')
		cookie.click()
		video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
		video.click()

	def pause(self):
		print("oui")
		videoPause = self.driver.find_element_by_xpath('//*[@id="movie_player"]/div[1]/video')
		videoPause.click()

	def close(self):
		self.driver.quit()