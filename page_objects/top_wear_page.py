"""
This class models the main Selenium tutorial page.
URL: selenium-tutorial-main
The page consists of a header, footer, form and table objects
"""
from .Base_Page import Base_Page
from .style_form_object import Style_Form_Object
from utils.Wrapit import Wrapit
import time
class Top_Wear_Page(Base_Page,Style_Form_Object):
    "Page Object for the Top wear page"

    def start(self):
        url = 'collections/top-wear'
        self.open(url)