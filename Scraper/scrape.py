from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = Chrome()
driver.get("https://web.housing.illinois.edu/diningmenus")
dining_dd = driver.find_element(By.ID, "dineop")
dining_options = dining_dd.find_elements(By.TAG_NAME, "option") 

date = driver.find_element(By.ID, "mealdate")
date.clear()
date.send_keys("02/26/2024")

with open("scraped_content.txt", "w", encoding="utf-8") as file:
    for option in dining_options:
        option.click(); 
        button = driver.find_element(By.CSS_SELECTOR, 'input.il-button.view[type="button"][value="View"]')
        button.click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menuData")))
        
        menu_data = driver.find_element(By.ID, "menuData")
        soup = BeautifulSoup(menu_data.get_attribute('innerHTML'), "html.parser")
    
                    
                


driver.quit()
