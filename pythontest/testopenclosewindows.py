from selenium import webdriver
import time

# เปิด Edge
edge_driver = webdriver.Edge()
edge_driver.get("https://www.bing.com/")

# จัดตำแหน่งหน้าต่างไปที่มุมซ้ายบน
edge_driver.set_window_position(0, 0)
time.sleep(5)  # รอ 2 วินาที

# พับหน้าต่าง
edge_driver.minimize_window()
time.sleep(5)  # รอ 2 วินาที

# ขยายหน้าจอเต็ม
edge_driver.maximize_window()
time.sleep(5)  # รอ 2 วินาที

# ทำให้เป็น Fullscreen
edge_driver.fullscreen_window()
time.sleep(5)  # รอ 2 วินาที





# ปิดเบราว์เซอร์
edge_driver.quit()
