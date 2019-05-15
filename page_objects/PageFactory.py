"""
PageFactory uses the factory design pattern. 
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Tutorial main page
2. Tutorial redirect page
3. Contact Page
4. Bitcoin main page
5. Bitcoin price page
"""

from page_objects.top_wear_page import Top_Wear_Page

class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url='https://madstreetden.myshopify.com/',trailing_slash_flag=True):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name == "top wear":
            test_obj = Top_Wear_Page(base_url=base_url,trailing_slash_flag=trailing_slash_flag)
        return test_obj

    get_page_object = staticmethod(get_page_object)