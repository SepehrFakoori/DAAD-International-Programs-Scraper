from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Create a driver
driver = webdriver.Chrome()


# This is the link of the International program for just PHD, Master and Bachelor
driver.get(
    'https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=&degree%5B%5D=1&'
    'degree%5B%5D=2&degree%5B%5D=3&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&'
    'langExamSC=&langDeAvailable=&langEnAvailable=&lang%5B%5D=&modStd%5B%5D=&cit%5B%5D=&tyi%5B%5D=&ins%5B%5D=&'
    'fee=&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=&limit=100&'
    'offset=&display=list')


# Wait for the cookie banner to appear and then close it
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button'))).click()
sleep(1)


# i = 1 --> Page 1
i = 1

items = []


# there are 20 pages for all international program in my time.
# you can check for number of the pages and change it
while i <= 20:

    # Get the link of each program and append it to the items list
    items.append([item.get_attribute("href") for item in
                  WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(
                      (By.CSS_SELECTOR, ".list-inline-item.mr-0.js-course-detail-link")))])
    
    sleep(5)

    try:

        # select next page button and if there were no next page button it exits from this
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.js-result-pagination-next"))).click()
        
    except Exception as e:

        print(f"Error: \n{e}")

    sleep(5)
    i += 1

# Print "Done" if complete scraping international programs
print("Done")

j = 0

# create a file path to save the links into the a txt file
file_path = "links.txt"

# Open the file in write mode
with open(file_path, "w") as file:

    # n is for writing number of the links besides them
    n = 1

    # x is for pages 1 to 20
    for x in range(0, 20):

        for item in items[x]:

            # Example: 1) https://links-of-the-first-program.com/
            # 2) https://links-of-the-second-program.com/

            file.write(f"{n}) " + item + "\n")
            n += 1


# Write this message when complete writing links in links.txt file
print("Links written to links.txt")