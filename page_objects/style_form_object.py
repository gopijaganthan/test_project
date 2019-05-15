"""
This class models the form on the Selenium tutorial page
The form consists of some input fields, a dropdown, a checkbox and a button
"""

from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import locator_objects.top_wear as top_wear_locator
import time


class Style_Form_Object:
    "Page object for the Form"

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def check_style_it_button_present(self, wait_seconds = 15):
        "Check Style it button is rendered properly"
        self.smart_wait(wait_seconds,top_wear_locator.style_me_img)
        result_flag = self.check_element_present(top_wear_locator.style_me_img)
        self.conditional_write(result_flag,
            positive='Verified Style Element is present in the top wear page',
            negative='Style Element is NOT present in the top wear page',
            level='debug')
        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_style_it_button(self, wait_seconds = 5):
        "click Style it button"
        self.smart_wait(wait_seconds,top_wear_locator.style_me_img)
        time.sleep(wait_seconds)
        result_flag = self.click_element(top_wear_locator.style_me_img)
        self.conditional_write(result_flag,
            positive='Clicked on Style Element in top wear page',
            negative='Unable to click on Style Element in top wear page',
            level='debug')
        return result_flag
    
    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_product_id(self, index_no, wait_seconds = 5):
        "click on product based on the index value in top wear page"
        self.smart_wait(wait_seconds,top_wear_locator.product_card%(index_no))
        result_flag = self.click_element(top_wear_locator.product_card%(index_no))
        self.conditional_write(result_flag,
            positive='Clicked on product id in top wear page',
            negative='Unable to click on product id in top wear page',
            level='debug')
        return result_flag

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_product_id(self, index_no = 1, wait_seconds = 5):
        "gets the product id based on the index value in top wear page"
        self.smart_wait(wait_seconds,top_wear_locator.style_me_img)
        href = self.get_attribute(top_wear_locator.product_card%(index_no),"href")
        self.conditional_write(href,
            positive='got product id on Style Element in top wear page',
            negative='Unable to get product id on Style Element in top wear page',
            level='debug')
        return href.rsplit('/',1)[1]

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_client_id(self, index_no = 1, wait_seconds = 5):
        "gets the client id based on the index value in top wear page"
        self.smart_wait(wait_seconds,top_wear_locator.client_id)
        client_id = self.get_attribute(top_wear_locator.client_id,"data-msd-client-id")
        self.conditional_write(client_id,
            positive='Found client id in top wear page',
            negative='Unable to find client id in top wear page',
            level='debug')
        return client_id

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_recommended_names(self, index_no = 1, wait_seconds = 5):
        "gets the recommended names from the carousel"
        self.smart_wait(wait_seconds,top_wear_locator.recommended_links)
        recommended_names = self.get_texts(top_wear_locator.recommended_names)
        self.conditional_write(recommended_names,
            positive='Found recommended names in top wear page - carousel',
            negative='Unable to find recommended names in top wear page - carousel',
            level='debug')
        return recommended_names

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_recommended_prices(self, index_no = 1, wait_seconds = 5):
        "gets the recommended prices from the carousel"
        self.smart_wait(wait_seconds,top_wear_locator.recommended_links)
        recommended_prices = self.get_texts(top_wear_locator.recommended_prices)
        self.conditional_write(recommended_prices,
            positive='Found recommended prices in top wear page - carousel',
            negative='Unable to find recommended prices in top wear page - carousel',
            level='debug')
        return recommended_prices

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_recommended_link(self, index_no = 1, wait_seconds = 5):
        "gets the recommended link from the carousel based on the index value"
        self.smart_wait(wait_seconds,top_wear_locator.recommended_links)
        recommended_links = self.get_attribute(top_wear_locator.recommended_links,"href")
        self.conditional_write(recommended_links,
            positive='Found links in top wear page - carousel',
            negative='Unable to find links in top wear page - carousel',
            level='debug')
        return recommended_links

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def click_recommended_product_link(self, product_id, wait_seconds = 5):
        "click the recommended link from the carousel based on product id"
        self.smart_wait(wait_seconds,top_wear_locator.recommended_product_link % product_id)
        click_product_link = self.click_element(top_wear_locator.recommended_product_link % product_id)
        self.conditional_write(click_product_link,
            positive='Clicked on productlinks in top wear page - carousel',
            negative='Unable to click on product link in top wear page - carousel %s' % product_id,
            level='debug')
        return click_product_link


    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def navigate_to_next_recommendations(self, wait_seconds = 5):
        "click the next button on the recommended view"
        self.smart_wait(wait_seconds,top_wear_locator.next_nav)
        next_nav = self.click_element(top_wear_locator.next_nav)
        self.smart_wait(wait_seconds,top_wear_locator.previous_nav)
        self.conditional_write(next_nav,
            positive='Found links in top wear page - carousel',
            negative='Unable to find links in top wear page - carousel',
            level='debug')
        return next_nav

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def navigate_to_previous_recommendations(self, index_no = 1, wait_seconds = 5):
        "click the previous button on the recommended view"
        self.wait(wait_seconds)
        self.smart_wait(wait_seconds,top_wear_locator.previous_nav)
        previous_nav = self.click_element(top_wear_locator.previous_nav)
        self.smart_wait(wait_seconds,top_wear_locator.next_nav)
        self.conditional_write(previous_nav,
            positive='Found links in top wear page - carousel',
            negative='Unable to find links in top wear page - carousel',
            level='debug')
        return previous_nav

    @Wrapit._screenshot
    @Wrapit._exceptionHandler
    def get_requests_made(self, path_to_filter_requests):
        req  = ''
        "get the requests made"
        req  = self.get_driver_requests_made()
        filtered_requests = [d for d in req if d.path == path_to_filter_requests]
        self.conditional_write(filtered_requests,
            positive='Found request that matches the condition',
            negative='Unable to find request that matches the condition',
            level='debug')
        return filtered_requests




