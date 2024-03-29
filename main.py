# Made by Kavin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#set the chrome WebDriver
driver = webdriver.Chrome()

# Go to Perplexity AI website
print("Type \'end\' to end the story")
driver.get("https://www.perplexity.ai")
prompt1 = "Write the first part of a choose your own story game from the perspective of someone affected by this article. This story should include the main ideas of this article, include important information and must always stay relevent. DO NOT MENTION AN ARTICLE OR ANY MEDIA WHERE THE INFORMATION IS FROM. avoid putting headings or any formatting in the response. Make the story interesting so that it has suspense, thrill, adventure and strongly maintains the user's attention so they want to find out what happens next at all times; while doing this, dont make it too repetitive or generic. Do not include an introduction or anything of the sort except the actual story in the response. At the end present the user with a couple open-ended options to continue the story so they can explore into a specific area of the article: "


#the parameter is the root article
def start(article):
    #Wait for the textarea element to be present
    textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder='Ask anything...']"))
    )
    #Enter text into the textarea
    textarea.send_keys(prompt1+article)
    button = driver.find_elements(By.CSS_SELECTOR, "button[class='md:hover:bg-offsetPlus text-textOff dark:text-textOffDark md:hover:text-textMain dark:md:hover:bg-offsetPlusDark  dark:md:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-in-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-point active:scale-95 origin-center whitespace-nowrap inline-flex text-sm aspect-square h-8']")
    for i in button:
        i.click()

def initiate():
    #close a popup
    while True:
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button[class='md:hover:bg-offsetPlus text-textOff dark:text-textOffDark md:hover:text-textMain dark:md:hover:bg-offsetPlusDark  dark:md:hover:text-textMainDark font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-in-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-point active:scale-95 origin-center whitespace-nowrap inline-flex text-sm aspect-square h-8']")
            button.click()
            break
        except:
            pass
    #initiate conversation with first button click
    while True:
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button[class='bg-super dark:bg-superDark dark:text-backgroundDark text-white hover:opacity-80 font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-in-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-point active:scale-95 origin-center whitespace-nowrap inline-flex text-sm aspect-square h-8']")
            button.click()
            break
        except:
            pass

def grabAnswer():
    while True:
        try:
            sleep(20)
            main = driver.find_elements(By.CSS_SELECTOR, "div[class='prose dark:prose-invert inline leading-normal break-words min-w-0 [word-break:break-word]']")
            sub_elements = main[-1].find_elements(By.XPATH, ".//*")
            # Print the text from each sub-element
            text = ""
            for sub_element in sub_elements:
                if sub_element.text in text:
                    continue
                text.join(sub_element.text)
                print(sub_element.text)
            break
        except:
            pass

#Enter text into input box (x is the choice the user gives)
def inputChoice(x):
    #enter prompt of user choice
    while True:
        try:
            prompt = f"This is the user's response. Continue the story and make sure to present more options at the end. These options should explore specific thing that the article was about. It should be technical but in the same time, integrate it into the story. When refering to studies include the actual specifics, facts and figures. Also make sure one of the options allows the user to connect this topic to a different topic. Remember to ALWAYS MAINTAIN THE NARRATIVE and keep it as a story. do not stray away from the fact that you are just a narrator of the users experiences: {x}"
            textarea = driver.find_element(By.CSS_SELECTOR, "textarea[placeholder='Ask follow-up']")
            textarea.send_keys(prompt)
            break
        except:
            pass

    #click button
    while True:
        try:
            button = driver.find_element(By.CSS_SELECTOR, "button[class='bg-super dark:bg-superDark dark:text-backgroundDark text-white hover:opacity-80 font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-in-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-point active:scale-95 origin-center whitespace-nowrap inline-flex text-sm aspect-square h-8']")
            button.click()
            break
        except:
            pass


try:
    start("https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1227279/full")
    initiate()
    grabAnswer()
    while True:
        x = input("Choice: ")
        if x.lower() == "end":
            break
        inputChoice(x)
        grabAnswer()


except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
