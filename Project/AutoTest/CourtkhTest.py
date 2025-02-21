import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Cập nhật ChromeDriver tự động
chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Giữ trình duyệt mở khi lỗi

# Khởi tạo trình duyệt
try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print("❌ Lỗi khi khởi động ChromeDriver:", e)
    exit()

# Mở trang danh sách sân cầu lông
driver.get("http://127.0.0.1:8000/Court-KH/")

# Chờ trang tải xong
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ Tải trang thành công")

# Chờ thêm 5 giây trước khi thực hiện hành động tiếp theo
time.sleep(5)

# Kiểm tra xem có nút 'Book Now' nào không
try:
    book_now_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Book Now')]")))
    assert book_now_buttons, "Không tìm thấy nút 'Book Now'!"
    print(f"✅ Tìm thấy {len(book_now_buttons)} nút 'Book Now'")

    # Nhấn vào nút 'Book Now' ngẫu nhiên
    random.choice(book_now_buttons).click()
    time.sleep(2)

    # Kiểm tra URL đã chuyển sang trang đặt sân
    assert "Bookings" in driver.current_url, "Chuyển hướng đến trang đặt sân thất bại!"
    print("✅ Chuyển hướng đến trang đặt sân thành công")
except Exception as e:
    print("❌ Lỗi khi kiểm tra nút 'Book Now':", e)
    driver.quit()
    exit()

# Thông báo kiểm tra thành công
print("✅ Kiểm tra thành công")

# Đóng trình duyệt
print("🔒 Đóng trình duyệt...")
driver.quit()
