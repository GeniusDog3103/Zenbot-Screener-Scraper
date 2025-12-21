from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options

def semi_auto_zen_data((url: str, time= 10, tries=3, headless= True, warnings=True):
  """
  Args:
    url: (str) url to zenbot scanner; check repo documentation for how to set up your own scanner
    time: (int) time in sec to wait for scanner to load; default: 10
    tries: (int) number of tries for website to load before quitting; default: 3
    headless: (bool) True to keep browser from popping up on your screen; default: True
    warnings: (bool) whether you want print messages for updates once loaded website, copied tickers, etc.; default: True
  Output:
    tickers: (list) list of tickers found
  """
    # enable browser logging
    


    #****************************************************************************************
    #MAKE SURE THAT WHEN YOU FIRST LOAD IT YOU PRESS ALLOW TO COPY CLIPBOARD SO THAT THE NEXT LOAD WILL WORK AUTOMATICALLY
    #****************************************************************************************



    options = Options()
    if headless == True:
        chrome_options.add_argument("--headless=new")
    options.add_argument(r"--user-data-dir=C:\Users\Intel\AppData\Local\Google\Chrome\User Data\Default")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=options)
    
    table_loaded_bool = False
    table = 0
    wait = WebDriverWait(driver, time) #takes some time for the thing too load
    while tries>0 and table_loaded_bool == False:
        try:
            driver.get(url)
            table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-grid-full')))
            if type(table) == webdriver.remote.webelement.WebElement:
                table_loaded_bool = True
                if warnings == True:
                    print("Loaded website")
        except exceptions.TimeoutException:
            tries-=1
            driver.quit()
            if warnings == True:
                print("Retrying to load website")
    try:
      
        copy_button = driver.find_element(by=By.ID, value="button-copy-tickers")
        if warnings == True:
            print("Found copy tickers button.")
        copy_button.click()

        clipboard_text_from_js = driver.execute_script("return navigator.clipboard.readText()")
        if warnings == True:
            print("Returned clipboard with copied tickers")
        #print("************************************")
        #print(f"TICKERS:{clipboard_text_from_js}")
        #print("************************************")
        tickers_vars = clipboard_text_from_js.split(',')
                
    except Exception as e:
        print(f"Error:{e}")

    finally:
        driver.quit()
        if warnings == True:
            print("Finished scraping; closed webdriver")
    
    return tickers_vars
