from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# ⚙️ Khởi tạo trình duyệt Chrome với tùy chọn
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Giữ trình duyệt mở
options.add_argument("--start-maximized")  # Mở toàn màn hình
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

# Khởi tạo trình duyệt
try:
    driver = webdriver.Chrome(options=options)
    driver.get("http://127.0.0.1:8000/Court-new/")
    
    # Chờ trang tải hoàn tất
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name_court"))
    )
    print("✅ Đã vào trang thêm sân cầu lông")
    
    # Nhập dữ liệu vào form
    name_field = driver.find_element(By.NAME, "name_court")
    start_time_field = driver.find_element(By.NAME, "start_time")
    end_time_field = driver.find_element(By.NAME, "end_time")
    type_field = driver.find_element(By.NAME, "type_court")
    cost_field = driver.find_element(By.NAME, "cost_court")
    status_field = driver.find_element(By.NAME, "status")
    location_field = driver.find_element(By.NAME, "location")
    
    name_field.send_keys(f"Sân Cầu {random.randint(10, 99)}")
    start_time_field.send_keys("06:00")
    end_time_field.send_keys("22:00")
    type_field.send_keys(Keys.ARROW_DOWN)
    type_field.send_keys(Keys.RETURN)
    cost_field.send_keys(str(random.randint(50000, 200000)))
    status_field.send_keys(Keys.ARROW_DOWN)
    status_field.send_keys(Keys.RETURN)
    location_field.send_keys("TPHCM")
    
    # 🛑 Dừng lại để kiểm tra trước khi lưu
    input("✅ Kiểm tra xong, nhấn Enter để lưu...")
    
    # Lưu dữ liệu
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
    save_button.click()
    
    # Chờ quay lại trang danh sách sân
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add Court')]")
    ))
    print("✅ Thêm sân thành công")
    
    # 🛑 Giữ trình duyệt mở để kiểm tra sau khi lưu
    input("✅ Kiểm tra sau khi lưu, nhấn Enter để kết thúc...")
    
except Exception as e:
    print(f"❌ Lỗi: {e}")
    input("Nhấn Enter để đóng trình duyệt...")
finally:
    driver.quit()