"""
This suite will is to verify  below usecases.

1) Navigate to https://madstreetden.myshopify.com/collections/top-wear 
2) Check if the 'Style it' buttons are rendered. 
3) Click on one of 'Style it' button
4) Check the requests that are sent.
5) Check the recommendations popup is correctly rendered.
6) Check if the products coming in the request are correctly populated in the carousel.
7) Click on Next (the right arrow) to see another set of products and check if they are rendered correctly.
8) Click on one of the recommended products and check if the product display page opens in a new tab.
"""
import os,sys,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
from endpoints.Madstreetden_API_Endpoints import Madstreetden_API_Endpoints
from endpoints.Eu_Speedy_Madstreetden_API_Endpoints import Eu_Speedy_Madstreetden_API_Endpoints
import conf.testrail_caseid_conf as testrail_file
from conf import top_wear_conf as conf
import json

def ui_top_wear_page(base_url,browser,browser_version,os_version,os_name,remote_flag,testrail_flag,tesults_flag,test_run_id,remote_project_name,remote_build_name):

    "Run the test"
    try:
        #1. Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #2. Create required objects to run test
        top_wear_obj = PageFactory.get_page_object("top wear",base_url=base_url)
        madstreetden_API = Madstreetden_API_Endpoints()
        eu_speedy_API = Eu_Speedy_Madstreetden_API_Endpoints()
        madstreetden_API.append_base_url()

        #3. Setup TestRail reporting
        if testrail_flag.lower()=='y':
            if test_run_id is None:
                top_wear_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                testrail_flag = 'N'   
            if test_run_id is not None:
                top_wear_obj.register_testrail()

        if tesults_flag.lower()=='y':
            top_wear_obj.register_tesults()

        #(Test step - 1): Navigate to https://madstreetden.myshopify.com/collections/top-wear
        #4. Setup and register a driver and navigate to base url
        start_time = int(time.time())   #Set start_time with current time
        top_wear_obj.register_driver(remote_flag,os_name,os_version,browser,browser_version,remote_project_name,remote_build_name)
        
        #(Test step - 2): Check if the 'Style it' buttons are rendered. 
        result_flag = top_wear_obj.check_style_it_button_present()
        top_wear_obj.log_result(result_flag,
                            positive="Verified Style Element is present in the top wear page",
                            negative="Failed - Style Element is NOT present in the top wear page \nOn url: %s\n"%(top_wear_obj.get_current_url()))

        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        case_id = testrail_file.test_example_check_style_it
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("check style element", "Verify Style Element is present in the top wear page", "test_example_check_style_it", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])
        
        
        #(Test step - 3): Click on one of 'Style it' button
        result_flag = top_wear_obj.click_style_it_button()
        top_wear_obj.log_result(result_flag,
                            positive="Clicked on Style Element in top wear page",
                            negative="Failed - Unable to click on Style Element in top wear page, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #5. Update test case results into configured test_rails
        case_id = testrail_file.test_example_click_style_it
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("Click style element", "Verify Style Element is present in the top wear page", "test_example_click_style_it", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])

        
        # (Test step - 4): Check the requests that are sent. 
        #6. Gets the API requests are being made, while clicking 'sytle it' button.
        filtered_requests = top_wear_obj.get_requests_made('https://demo-vuestyle.madstreetden.com/get_product_meta')
        result_flag = filtered_requests
        top_wear_obj.log_result(len(result_flag)==1,
                            positive="find the request made to the get_product_meta",
                            negative="Failed - request NOT made to get product meta data while click on click style it button, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
     
        top_wear_obj.log_result(result_flag[0].method=='POST',
                            positive="find the request method made to the get_product_meta",
                            negative="Failed - request NOT made to get product meta data while click on click style it button, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        top_wear_obj.log_result(result_flag[0].headers['Host'] =='demo-vuestyle.madstreetden.com',
                            positive="find the request hdeader host to the get_product_meta",
                            negative="Failed - request NOT made to get product meta data while click on click style it button, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        case_id = testrail_file.test_example_check_request_made
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("Check Request Made", "Verify request sent after click Style button in the top wear page", "test_example_check_request_made", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])


        #7. Get product id from the page
        product_id = top_wear_obj.get_product_id().upper()
        #8. Get client id from the page
        client_id = top_wear_obj.get_client_id()

        #9. Get API Key using 'client_id' redender in base url
        data= {"client": client_id}
        header =  {"Content-Type": "application/json","Origin":base_url,"Referer": base_url+"/collections/top-wear"}
        configuration_data = eu_speedy_API.get_config(data,header)
        api_key = configuration_data['response']['api_key']

        #10. Constructing JSON object request recommended product's meta data
        data = {}
        data["api_key"] = api_key
        data["widget_list"] = [0]
        data["mad_uuid"] = client_id
        data["product_id"] = product_id
        data["num_results"] = conf.num_results
        data["occasions"] = conf.occasions
        data["fields"] = conf.fields
        data["filters"]  = conf.filters
        json_data = json.loads(json.dumps(data))

        #(Test step - 5): Check the recommendations popup is correctly rendered.
        #11. To verify rendered product's infromation, Get product's meta data using the mad stree API
        recommended_product_name = madstreetden_API.get_recommended_product(json_data,header)
        recommended_product_price = madstreetden_API.get_recommended_product(json_data,header,'price')
        recommended_product_id = madstreetden_API.get_recommended_product(json_data,header,'product_id')

        #12. Verify recommended names are shown in the carousel
        result_flag = top_wear_obj.get_recommended_names() == recommended_product_name[0:4]
        top_wear_obj.log_result(result_flag,
                            positive="Verified the products names coming in the request are correctly populated in the carousel",
                            negative="Failed - the products names coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #13. Verify recommended prices are shown in the carousel
        result_flag = top_wear_obj.get_recommended_prices() == ['$'+str(int(x)) for x in recommended_product_price[0:4]]
        top_wear_obj.log_result(result_flag,
                            positive="Verified the products prices coming in the request are correctly populated in the carousel",
                            negative="Failed - the products prices coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #14. Verify recommended product link is correctly linked
        result_flag = top_wear_obj.get_recommended_link().endswith(recommended_product_id[0])
        top_wear_obj.log_result(result_flag,
                            positive="Verified the products links coming in the request are correctly populated in the carousel",
                            negative="Failed - the products links coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        case_id = testrail_file.test_product_recommended_carousel
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("Click next rendered correctly", "Verify after Clicking on Next (the right arrow) to see another set of products are rendered correctly in the top wear page", "test_product_recommended_carousel", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])

        #(Test step - 7): Click on Next (the right arrow) to see another set of products and check if they are rendered correctly.
        top_wear_obj.navigate_to_next_recommendations()

        #15. After clicking Next button, To verify rendered product's infromation, Get product's meta data using the mad stree API
        recommended_product_name = madstreetden_API.get_recommended_product(json_data,header)
        recommended_product_price = madstreetden_API.get_recommended_product(json_data,header,'price')
        recommended_product_id = madstreetden_API.get_recommended_product(json_data,header,'product_id')

        #(Test step - 6): Check if the products coming in the request are correctly populated in the carousel.
        result_flag = top_wear_obj.get_recommended_names() == recommended_product_name[4:8]
        top_wear_obj.log_result(result_flag,
                            positive="Verified the products Names coming in the request are correctly populated in the carousel",
                            negative="Failed - the products Names coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #16. After clicking Next button, Verify recommended prices are shown in the carousel
        result_flag = top_wear_obj.get_recommended_prices() == ['$'+str(int(x)) for x in recommended_product_price[4:8]]
        top_wear_obj.log_result(result_flag,
                            positive="Verified the products prices coming in the request are correctly populated in the carousel",
                            negative="Failed - the products prices coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #17. After clicking Next button, Verify recommended product link is correctly linked
        result_flag = top_wear_obj.get_recommended_link().endswith(recommended_product_id[4])
        top_wear_obj.log_result(result_flag,
                            positive="Verified the product\'s link coming in the request are correctly populated in the carousel",
                            negative="Failed - the product\'s link coming in the request are NOT correctly populated in the carousel, On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        case_id = testrail_file.test_click_next_rendered_products
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("Click next rendered correctly", "Verify after Clicking on Next (the right arrow) to see another set of products are rendered correctly in the top wear page", "test_click_next_rendered_products", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])

        #(Test step - 8): Click on one of the recommended products and check if the product display page opens in a new tab.
        top_wear_obj.click_recommended_product_link(recommended_product_id[4])
        top_wear_obj.switch_window()
        result_flag = top_wear_obj.get_current_url().find(recommended_product_id[4]) != -1
        top_wear_obj.log_result(result_flag,
                            positive="Verified after clicking on the recommended product populated in the carousel",
                            negative="Failed - Aftr clicking on the recommended product page Not rendered Properly in a new tab., On url: %s\n"%(top_wear_obj.get_current_url()))
        top_wear_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
        case_id = testrail_file.test_click_recommended_product
        top_wear_obj.report_to_testrail(case_id,test_run_id,result_flag)
        top_wear_obj.add_tesults_case("Click next rendered correctly", "Verify after Verified after clicking on the recommended product populated in the carousel it navigated to new tab", "test_click_recommended_product", result_flag, "", [top_wear_obj.log_obj.log_file_dir + os.sep + top_wear_obj.log_obj.log_file_name])

        #18. Print out the results
        top_wear_obj.write_test_summary()
        
        top_wear_obj.wait(3)
        expected_pass = top_wear_obj.result_counter
        actual_pass = top_wear_obj.pass_counter
        top_wear_obj.teardown()
        
    except Exception as e:
        print("Exception when trying to run test:%s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
       
    
#---START OF SCRIPT   
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()
                
    #Run the test only if the options provided are valid
    if options_obj.check_options(options): 
        ui_top_wear_page(base_url=options.url,
                        browser=options.browser,
                        browser_version=options.browser_version,
                        os_version=options.os_version,
                        os_name=options.os_name,
                        remote_flag=options.remote_flag,
                        testrail_flag=options.testrail_flag,
                        tesults_flag=options.tesults_flag,
                        test_run_id=options.test_run_id,
                        remote_project_name=options.remote_project_name,
                        remote_build_name=options.remote_build_name) 
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
