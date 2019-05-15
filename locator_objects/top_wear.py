############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Locators for the sytle it page

style_me_img = "xpath,//div[@data-msd-module-id]/img"
product_card = "xpath,//li[%d]//div[contains(@class,'product-card')]/a"
client_id = "xpath,//script[@data-msd-client-id]"
recommended_names = "xpath,//div[@class='vue-item-wrapper vue-slider-item-wrapper']//div[@class='vue-carousel-slide-item-text']"
recommended_prices = "xpath,//div[@class='vue-item-wrapper vue-slider-item-wrapper']//div[contains(@class,'vue-product-price')]"
recommended_links = "xpath,//div[@class='vue-item-wrapper vue-slider-item-wrapper']//div[@class='vue-carousel-slide-item-image-wrapper']//a"
recommended_product_link = "xpath,//div[@class='vue-item-wrapper vue-slider-item-wrapper']//div[@class='vue-carousel-slide-item-image-wrapper']//a[contains(@href,'%s')]"
next_nav = "xpath,//a[@class='vue-next-nav-wrapper']"
previous_nav = "xpath,//a[@class='vue-prev-nav-wrapper']"
#----
