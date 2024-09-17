from selenium import webdriver


class Base_Positioning:

    driver = webdriver.Chrome()

    def open_url_add(self,url):
        self.driver.get(url)

    def xpath_elements(self, elements, code, *args):
        if code == 1:
            self.driver.find_element_by_xpath(elements).send_keys(args)
        elif code == 2:
            self.driver.find_element_by_xpath(elements).clear()
        elif code == 3:
            return self.driver.find_element_by_xpath(elements).text
