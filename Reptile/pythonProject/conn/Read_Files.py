from conn.Base import Base_Positioning



class Img_get_seva:

    url = 1

    def __init__(self):
        self.driver = Base_Positioning().open_url_add()




    def positioning_elements(self,elements):
        self.driver
        self.driver.find_element_by_xpath(elements).clear()