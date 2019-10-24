
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# selenium packages for waiting.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException

import time

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_experimental_option("prefs", {
    "download.default_directory": r"/Users/eomiso/Workplace/Kagglecompt/MirraeAssetCompt/미래에셋 공모전/data/jooganhaeseol",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


driver = webdriver.Chrome(options = options)
driver.get('https://www.petronet.co.kr/v3/index.jsp')

driver.find_element_by_id("id").send_keys('0428kdh')
driver.find_element_by_id("passwd").send_keys('0428kdh!*')
driver.find_element_by_class_name("btn").click()

# find element
target = driver.find_element_by_id("top-menu-head2") #.move_to_element().perfom()
# create object for Action Chains
actions = ActionChains(driver)
actions.move_to_element(target)
#perform the operation on the element
actions.perform()

# find element (주간해설)
driver.find_element_by_xpath("//ul[@id='top-sub-menu2']/li[@class='first_sub_lnb']/a[1]").click()

# switch frame
driver.switch_to.frame('body')

# document number
start = 2500
end = 2100 #2100번 자료부터 2011년 자료
data_cnt = 0
page_num = 0
error_file = []
nData = start - end

while data_cnt < nData:
    # move to page
    page_num +=1
    print('\nPage:',page_num,end='   ')
    time.sleep(.5)
    try:
        # 텍스트 기반으로 페이지 버튼 찾음.
        driver.find_element_by_link_text(str(page_num)).click()
    except WebDriverException:
        driver.back()
        driver.switch_to.frame('body')
        error_file.append(nData - data_cnt + 1 )
        driver.find_element_by_link_text(str(page_num)).click()

    # table rows where downloadable files are stored
    targets = driver.find_elements_by_xpath('//*[@id="contents"]/form[1]/fieldset/table/tbody/tr')
    time.sleep(.5)
    for row in range(1, len(targets)+1):  #row 1 ~ n
        xPath = f'//*[@id="contents"]/form[1]/fieldset/table/tbody/tr[{row}]/td[5]/a/img'
        data_cnt += 1
        print(nData - data_cnt + 1 , end = ' ')

        try:
            driver.find_element_by_xpath(xPath).click()
        except WebDriverException:
            driver.back()
            driver.switch_to.frame('body')
            error_file.append(nData - data_cnt +2)
            driver.find_element_by_xpath(xPath).click()
    
    #페이지 번호가 10의 배수이면 옆에 화살표를 클릭해서 넘어간다.
    if page_num % 10 == 0 and data_cnt < nData:
        # 첫번째 버튼과 두번째 버튼의 Path가 다르다.
        if page_num == 10: i=3
        else: i=4

        page_arrow_path = f'//*[@id="contents"]/form[1]/fieldset/div/ul/li[{i}]/a/img'
        try:
            page_element_arrow = driver.find_element_by_xpath(page_arrow_path)
            page_element_arrow.click()
        except WebDriverException:
            driver.back()
            driver.switch_to.frame('body')
            error_file.append(nData - data_cnt + 1 )
            page_element_arrow = driver.find_element_by_xpath(page_arrow_path)
            page_element_arrow.click()

print('Error_files: ',error_file)


