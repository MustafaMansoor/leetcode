from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to your chromedriver.exe using Service
service = Service("C:\\Users\\Mustafa\\Desktop\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

page_urls = [
    'https://perkinknives.com/collections/folding-pocket-knives',
    'https://perkinknives.com/collections/folding-pocket-knives?page=2',
    'https://perkinknives.com/collections/folding-pocket-knives?page=3',
    'https://perkinknives.com/collections/folding-pocket-knives?page=4',
    'https://perkinknives.com/collections/chef-knives',
    'https://perkinknives.com/collections/chef-knives?page=2',
    'https://perkinknives.com/collections/chef-knives?page=3'
]

with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Description', 'Regular price', 'Categories', 'Images'])
    
    for page_url in page_urls:
        driver.get(page_url)
        time.sleep(6)
        
        # Handle potential overlay (e.g., age verification)
        try:
            wait = WebDriverWait(driver, 10)
            overlay = wait.until(EC.visibility_of_element_located((By.ID, "age-verification")))
            close_button = overlay.find_element(By.CLASS_NAME, "close-button")  # Adjust as needed
            close_button.click()
            time.sleep(2)
        except:
            pass

        # Handle cookie consent banner
        try:
            cookie_banner = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "cc-window"))
            )
            accept_button = cookie_banner.find_element(By.CLASS_NAME, "cc-btn")
            accept_button.click()
            time.sleep(2)
        except:
            pass

        parent = driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[2]/div/div[1]/div/div[5]")
        child_elements = parent.find_elements(By.XPATH, ".//*")  # All descendants

        for i in range(len(child_elements)):
            # Re-locate the parent and child elements to avoid stale references
            parent = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[4]/div[2]/div/div[1]/div/div[5]"))
            )
            parent = driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[2]/div/div[1]/div/div[5]")
            parent = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[4]/div[2]/div/div[1]/div/div[5]"))
            )
            updated_child = parent.find_elements(By.XPATH, ".//*")[i]
            
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product_item")))
            child_div = updated_child.find_element(By.CLASS_NAME, "product_item")  # Adjust as needed
            subchild_div = child_div.find_element(By.CLASS_NAME, "product_info")  # Adjust as needed
            againsubchild_div = subchild_div.find_element(By.CLASS_NAME, "product_name")  # Adjust as needed

            lastsubchild_div = againsubchild_div.find_element(By.TAG_NAME, "a")  # Adjust as needed

            # Ensure no overlay is blocking the click
            try:
                wait.until(EC.element_to_be_clickable((By.TAG_NAME, "a")))
                lastsubchild_div.click()
                time.sleep(10)  # Wait for the new page to load
            except Exception as e:
                print(f"Error clicking on product link: {e}")
                continue
            
            # Scrape data on the new page
            try:
                title = driver.find_element(By.CLASS_NAME, "single_product__title").text
                description = driver.find_element(By.CLASS_NAME, "product_description rte").text
                price = driver.find_element(By.CLASS_NAME, "single_product__price").text  # Adjust as needed
                print(f"Name: {title}")
                print(f"Description: {description}")
                print(f"Regular price: {price}")
            except Exception as e:
                print(f"Error scraping data: {e}")
            
            # Navigate back to the original page
            driver.back()
            time.sleep(2)  # Wait to ensure the original page is fully loaded 

driver.quit()
print("Scraping completed. Data saved to products.csv.")