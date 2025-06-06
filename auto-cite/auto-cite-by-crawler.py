from util import *
from importlib import import_module
from dict_hash import sha256
from datetime import datetime

# config info for input/output files and plugins
config = {}
try:
    config = load_data("../_config.yaml", type_check=False).get("auto-cite")
    if not config:
        raise Exception("Couldn't find auto-cite key in config")
except Exception as e:
    log(e, 3, "red")
    exit(1)

log("Compiling list of sources to cite")

# error exit flag
will_exit = False

# loop through plugins
# exit at end of loop if error occurred
if will_exit:
    log("One or more input files or plugins failed", 3, "red")
    exit(1)

log("Generating citations for sources")

# load existing citations
citations = []
try:
    citations = load_data(config["output"])
except Exception as e:
    log(e, 2, "yellow")

# error exit flag
will_exit = False

# list of new citations to overwrite existing citations
new_citations = []
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os


def setup_webdriver():
    # 从环境变量获取Chrome和ChromeDriver路径
    chrome_binary_path = os.environ.get('CHROME_BINARY_PATH')
    chromedriver_path = os.environ.get('CHROMEDRIVER_PATH')
    
    # 设置ChromeDriver服务
    if chromedriver_path:
        print(f"使用环境变量指定的ChromeDriver路径: {chromedriver_path}")
        chrome_service = Service(chromedriver_path)
    else:
        # 如果环境变量未设置，回退到传统方式
        from webdriver_manager.chrome import ChromeDriverManager
        print("使用WebDriverManager安装ChromeDriver")
        chrome_service = Service(ChromeDriverManager().install())
    
    # 配置Chrome选项
    chrome_options = Options()
    
    # 设置Chrome二进制文件位置
    if chrome_binary_path:
        print(f"使用环境变量指定的Chrome路径: {chrome_binary_path}")
        chrome_options.binary_location = chrome_binary_path
    
    # 添加必要的Chrome选项，特别是在CI环境中
    options = [
        "--headless",  # 无头模式
        "--disable-gpu",  # 在某些Linux系统上需要
        "--window-size=1920,1200",  # 设置窗口大小
        "--ignore-certificate-errors",  # 忽略证书错误
        "--disable-extensions",  # 禁用扩展
        "--no-sandbox",  # 在CI环境中必须
        "--disable-dev-shm-usage"  # 解决在Docker/CI环境中的内存问题
    ]
    
    for option in options:
        chrome_options.add_argument(option)
    
    # 创建WebDriver实例
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver

wd = setup_webdriver()
publications={}
supervisors = ['https://scholar.google.com/citations?user=NJOnxh4AAAAJ&hl=en','https://scholar.google.com/citations?user=0HtCYQEAAAAJ&hl=en','https://scholar.google.com/citations?user=UKqaI5IAAAAJ&hl=en']
for supervisor in supervisors:
    depth = config.get("depth", 10)
    wd.get(supervisor)
    wd.find_element(By.XPATH, '//*[@id="gsc_a_ha"]/a').click()
    for i in range(10):
        wd.find_element(By.XPATH, '//*[@id="gsc_bpf_more"]/span/span[2]').click()
        sleep(1)

    for i in range(depth):
        try:
            part = wd.find_element(By.XPATH, f'//*[@id="gsc_a_b"]/tr[{i+1}]/td[1]/a')
        except:
            break
        href = part.get_attribute('href')
        sleep(1)
        wd.execute_script(f"window.open('{href}', 'new_tab')")
        wd.switch_to.window("new_tab")
        title = wd.find_element(By.ID, 'gsc_oci_title').text
        author = wd.find_element(By.CLASS_NAME, 'gsc_oci_value').text
        date = wd.find_element(By.XPATH, '//*[@id="gsc_oci_table"]/div[2]/div[2]').text.replace('/','-')
        pub = wd.find_element(By.XPATH, '//*[@id="gsc_oci_table"]/div[3]/div[2]').text
        cnt = 4
        while True:
            try:
                url = wd.find_element(By.XPATH, f'//*[@id="gsc_oci_table"]/div[{cnt}]/div[2]/div/div[1]/a').get_attribute("href")
                break
            except:
                cnt+=1
        print(title, f'{i+1}/{depth}')
        publications[title.lower()] = {'title':title, 'authors':[a.strip() for a in author.split(",")], 'publisher':pub, 'date':date, 'link':url}
        sleep(1)
        wd.close()
        wd.switch_to.window(wd.window_handles[0])
        
for pub in citations:
    title = pub["title"]
    if 'id' in pub:
        pub.pop("id")
    if '_cache' in pub:
        pub.pop("_cache")
    publications[title.lower()] = pub

def convert_to_datetime(time_string):
    try:
        return datetime.strptime(time_string, "%Y-%m-%d")
    except:
        try:
            return datetime.strptime(time_string, "%Y-%m")
        except:
            return datetime.strptime(time_string, "%Y")

new_citations = []
for id in publications:
    date = publications[id]['date'].replace('/','-')
    converted_date = convert_to_datetime(date)
    date = converted_date.strftime("%Y-%m-%d")
    new_citations.append({'id':id, 'title':publications[id]['title'], "authors":publications[id]['authors'], "publisher":publications[id]['publisher'], "date":date, "link":publications[id]['link']})

new_citations.sort(key=lambda x:convert_to_datetime(x['date']),reverse=True)
# exit at end of loop if error occurred
if will_exit:
    log("One or more sources failed to be cited", 3, "red")
    exit(1)

log("Exporting citations")

# save new citations
try:
    save_data(config["output"], new_citations)
except Exception as e:
    log(e, 2, "red")
    exit(1)

log(f"Exported {len(new_citations)} citations", 2, "green")
