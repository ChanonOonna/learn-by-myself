from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ตั้งค่า ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # เปิดหน้าต่างเต็มจอ
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
  # ปลอม User-Agent

# เปิดเบราว์เซอร์
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

# รอให้ช่องค้นหาโหลด
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# เลียนแบบการขยับเมาส์ไปที่ช่องค้นหา
actions = ActionChains(driver)
actions.move_to_element(search_box).perform()
time.sleep(random.uniform(1, 2))  # หน่วงเวลาแบบสุ่ม

# เลียนแบบการพิมพ์ช้าๆ ทีละตัวอักษร
text_to_type = "Selenium automation"
for char in text_to_type:
    search_box.send_keys(char)
    time.sleep(random.uniform(0.2, 0.6))  # เวลาพิมพ์แต่ละตัวอักษรแบบสุ่ม

# หน่วงเวลาเพิ่มก่อนกด Enter
time.sleep(random.uniform(1, 3))

# ใช้ JavaScript คลิกปุ่ม "ค้นหา" แทนการกด Enter
search_button = driver.find_element(By.NAME, "btnK")
driver.execute_script("arguments[0].click();", search_button)

# รอให้ผลลัพธ์โหลด
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
)

# ปิดเบราว์เซอร์
driver.quit()
