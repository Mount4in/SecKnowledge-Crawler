import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from toollib import autodriver
import markdownify
from bs4 import BeautifulSoup
import os
import requests

def filename_filter(filename):  
    string1="\/:*?\"<>|"
    for s1 in string1:
        filename= filename.replace(s1," ")
    return(filename)

if __name__ == '__main__':
    # 自动下载驱动，默认下载本地浏览器对应的版本（各参数可自行指定）
    # driver_path = autodriver.chromedriver()
    driver_path = "chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=Service(driver_path),options=chrome_options)
    for i in range(10000, 15000):#15023):
        try:
            id = str(i)
            url = "https://xz.aliyun.com/t/" + id
            print(url)

            driver.get(url)
            headers = {
                "Referer": "https://xz.aliyun.com/"
            }

            html_content = driver.page_source
            soup = BeautifulSoup(html_content, "html.parser")
            img_tags = soup.find_all("img")
            title_tag = soup.find('title')
            title_text = title_tag.text if title_tag else None
            print(title_text)
            if not title_text or ('400 -' in title_text) :
                time.sleep(10)
                continue
            f = filename_filter(title_text)
            filename = "./xianzhi/"+id+"-"+ f + ".md"

            if not os.path.exists("./xianzhi/images"):
                os.makedirs("./xianzhi/images")

            for img_tag in img_tags:
                img_url = img_tag.get("src")
                img_name = os.path.basename(img_url)
                img_data = requests.get(img_url,headers=headers).content
                with open(f"./xianzhi/images/{img_name}", "wb") as f:
                    f.write(img_data)

            md_content = markdownify.markdownify(html_content, heading_style="ATX")

            for img_tag in img_tags:
                img_url = img_tag.get("src")
                # print(img_url)
                img_name = os.path.basename(img_url)
                md_content = md_content.replace(img_url, f"images/{img_name}")

            with open(filename, "w", encoding="utf-8") as f:
                f.write(md_content)
        except Exception as e:
            print(str(e))
            pass
        time.sleep(10)
    driver.quit()
    
