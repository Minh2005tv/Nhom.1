import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

try:
    # Tìm input username
    inputUserName = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))  # Sửa "Username" -> "username"
    )
    print(inputUserName)
    inputUserName.send_keys("admin")
    time.sleep(2)

    # Tìm input password
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    print(password)
    password.send_keys("your_password")  # Thay bằng mật khẩu thực tế
    time.sleep(2)

    # Gửi phím RETURN để đăng nhập
    password.send_keys(Keys.RETURN)

    # Chờ trang tải hoàn tất
    WebDriverWait(driver, 10).until(
        EC.title_contains("Site administration")
    )

    print("Đăng nhập thành công!")

except Exception as e:
    print(f"Lỗi xảy ra: {e}")

finally:
    time.sleep(5)
    driver.quit()