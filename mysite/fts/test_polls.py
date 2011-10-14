from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys

class TestPolls(FunctionalTest):
    def _setup_polls_via_admin(self):
        # Gertrude logs into the admin site
        self.browser.get(ROOT + '/admin/')
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')
        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

        # She follows the link to the Polls app, and adds a new Poll
        self.browser.find_elements_by_link_text('Polls')[1].click()
        self.browser.find_element_by_link_text('Add poll').click()

        # She enters its name, and uses the 'today' and 'now' buttons to set
        # the publish date
        question_field = self.browser.find_element_by_name('question')
        question_field.send_keys("How awesome is Test-Driven Development?")
        self.browser.find_element_by_link_text('Today').click()
        self.browser.find_element_by_link_text('Now').click()

        # She sees she can enter choices for the Poll.  She adds three
        choice_1 = self.browser.find_element_by_name('choice_0')
        choice_1.send_keys('Very awesome')
        choice_2 = self.browser.find_element_by_name('choice_1')
        choice_2.send_keys('Quite awesome')
        choice_3 = self.browser.find_element_by_name('choice_2')
        choice_3.send_keys('Moderately awesome')

        # She saves her new poll
        self.browser.find_element_by_link_text('Save').click()


    def test_voting_on_a_new_poll(self):
        # First, Gertrude the administrator logs into the admin site and
        # creates a couple of new Polls, and their response choices
        self._setup_polls_via_admin()

        # Now, Herbert the regular user goes to the homepage of the site. He
        # sees a list of polls.

        # He clicks on the link to the first Poll, which is called
        # 'How awesome is test-driven development?'

        # He is taken to a poll 'results' page, which says
        # "no-one has voted on this poll yet"

        # He also sees a form, which offers him several choices.
        # He decided to select "very awesome"

        # Herbert clicks 'submit'

        # The page refreshes, and he sees that his choice
        # has updated the results.  they now say
        # "100 %: very awesome".

        # The page also says "1 votes"

        # Satisfied, he goes back to sleep

