from selenium import webdriver#(1)
import unittest

class NewVisitorTesst(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_is_later(self):
        #Edith has heard about a cool new online to-do app She goes to chceck out its homepage
        self.browser.get('http://localhost:8000')

        #She noticecs the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')


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