import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# Kiểm tra và cập nhật ChromeDriver nếu cần
chromedriver_autoinstaller.install()

# Cấu hình Chrome
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")  # Tránh lỗi render
options.add_argument("--no-sandbox")   # Hữu ích khi chạy trên môi trường CI/CD

# Khởi tạo trình duyệt
driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

try:
    # Chờ input username xuất hiện (tăng timeout lên 15s)
    inputUserName = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))  
    )
    inputUserName.send_keys("admin")
    time.sleep(1)

    # Chờ input password xuất hiện
    password = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.send_keys("123456")
    time.sleep(1)

    # Gửi phím RETURN để đăng nhập
    password.send_keys(Keys.RETURN)

    # Chờ trang quản trị tải hoàn tất
    WebDriverWait(driver, 15).until(
        EC.title_contains("Site administration")
    )

    print("✅ Đăng nhập thành công!")

except Exception as e:
    print(f"❌ Lỗi xảy ra: {e}")

finally:
    time.sleep(3)
    driver.quit()
