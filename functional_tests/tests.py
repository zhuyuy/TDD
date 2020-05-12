from django.test import LiveServerTestCase
from selenium import webdriver#(1)
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTesst(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn( row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith has heard about a cool new online to-do app She goes to chceck out its homepage
        self.browser.get(self.live_server_url)

        #She noticecs the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #she is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feahters')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feahters')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        #there is still a tet box inviting her to add another item. She enters"use peacock feathers to make a fly'(Edith is very methodical)
        self.fail('finish the test!')


#if __name__=='__main__':


browser = webdriver.Firefox()#(2)

#Edith has heard about a cool new online to-do  app. She goes
# to check out its homepage
browser.get("http://localhost:8000")#(3)

# She noticecs the page title and header mention to-do lists
assert 'To-Do' in browser.title, "Brower title was" + browser.title

# She is invited to enter a to-do item straight away

#She typing "Buy  peacock feathers " into a text box (Edith's hobby
# is tying fly-fishing lures)

#when she hits enter, the page updates, and now the apge lists
#"1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item. She
#enters "Use peacock feathers to make a flu" (Edith is vey methodical)

#The page updates again, and now shows both item on her list

#The page updates again, and no shos both item on her list

#Edith wonders whether the site will remenber her list Then she sees 
#that the site has gearated a unique URL for her -- there is some
#explanatory text to that effect

#she visits that URL - her to-do list is still there

#Satistied , she goes back  to sleep

browser.quit() 