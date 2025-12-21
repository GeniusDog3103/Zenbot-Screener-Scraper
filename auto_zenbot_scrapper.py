from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options

def auto_zen_data(url: str, time= 10, tries=3, headless= True, warnings=True):
    """
    Args:
      url: (str) url to screener
      time: (int) time in sec to wait for scanner to load; default: 10
      tries: (int) number of tries for website to load before quitting; default: 3
      headless: (bool) True to keep browser from popping up on your screen; default: True
      warnings: (bool) whether you want print messages for updates once loaded website, copied tickers, etc.; default: True
    Output:
      tickers: (list) list of tickers found
    """
    chrome_options = Options()
    if headless == True:
      chrome_options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(options=chrome_options)
      
      
    table_loaded_bool = False
    table = 0
    wait = WebDriverWait(driver, time) #takes some time for the website to load
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
       symbols = driver.find_elements(by=By.CSS_SELECTOR, value='div.grid-cell.age-column-container')
        
        if warnings == True:
            print("Found tickers table")
            
       stocks_df = []
       for element in symbols:
           stocks_df.append(element.text)
            
    except Exception as e:
        print(f"Error:{e}")

    finally:
        driver.quit()
        if warnings == True:
            print("Closed website, finished scrapping.")
    
    return stocks_df
