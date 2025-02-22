from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    # Mở trang chỉnh sửa sân cầu lông
    driver.get("http://127.0.0.1:8000/Court-edit/28/")
    print("✅ Tải trang thành công")
    
    # Chờ trang tải hoàn tất
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name_court"))
    )
    time.sleep(1.5)


     #Sửa dữ liệu trong form
    print("🔄 Đang chỉnh sửa dữ liệu...")
    
    name_field = driver.find_element(By.NAME, "name_court")
    start_time_field = driver.find_element(By.NAME, "start_time")
    end_time_field = driver.find_element(By.NAME, "end_time")
    type_field = driver.find_element(By.NAME, "type_court")
    cost_field = driver.find_element(By.NAME, "cost_court")
    status_field = driver.find_element(By.NAME, "status")
    location_field = driver.find_element(By.NAME, "location")
    
    name_field.clear()
    name_field.send_keys("Sân Cầu Lông VIP")
    time.sleep(1.5)

    start_time_field.send_keys("06:00AM")
    time.sleep(1.5)
    end_time_field.send_keys("22:00PM")
    time.sleep(1.5)

    type_field.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    type_field.send_keys(Keys.RETURN)
    time.sleep(1.5)

    cost_field.clear()
    cost_field.send_keys("120000")
    time.sleep(1.5)
    
    status_field.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    status_field.send_keys(Keys.RETURN)
    time.sleep(1.5)

    location_field.clear()
    location_field.send_keys("Hà Nội")
    time.sleep(1.5)

    print("✅ Chỉnh sửa dữ liệu thành công")

    # 4️⃣ Kiểm tra nếu có lỗi trước khi lưu
    try:
        error_message = driver.find_element(By.CLASS_NAME, "error-message").text
        if error_message:
            print(f"❌ Lỗi khi chỉnh sửa dữ liệu: {error_message}")
            driver.quit()
            exit()
    except:
        print("✅ Không có lỗi khi chỉnh sửa dữ liệu")
    
    time.sleep(2)

    # 5️⃣ Nhấn nút Save
    print("🔄 Đang lưu chỉnh sửa...")
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save')]"))
    )
    save_button.click()
    
    time.sleep(3)  # Chờ dữ liệu được xử lý

    # 6️⃣ Chờ trang chuyển về danh sách sân (`http://127.0.0.1:8000/Courts/`)
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://127.0.0.1:8000/Courts/")
    )
    print("✅ Chỉnh sửa sân thành công")
    time.sleep(2)

except Exception as e:
    print(f"❌ Lỗi: {e}")

finally:
    # 7️⃣ Đóng trình duyệt
    print("🛑 Đóng trình duyệt sau 3 giây...")
    time.sleep(3)
    driver.quit()
    print("✅ Đã đóng trình duyệt thành công")
