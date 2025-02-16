import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Cài đặt ChromeDriver tự động
chromedriver_autoinstaller.install()

# Khởi tạo WebDriver với tuỳ chọn
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Giữ trình duyệt mở khi lỗi

driver = webdriver.Chrome(options=options)

# Mở trang danh sách sân cầu lông
driver.get("http://127.0.0.1:8000/Court-KH/")

# Chờ bảng danh sách sân hiển thị
wait = WebDriverWait(driver, 10)
court_table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
court_rows = court_table.find_elements(By.TAG_NAME, "tr")
assert len(court_rows) > 1, "Danh sách sân không hiển thị hoặc bị lỗi!"
print("✅ Danh sách sân hiển thị đúng")

# --- TEST 2: Kiểm tra nút 'Book Now' hoạt động đúng ---
book_now_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'Book Now')]")))
assert len(book_now_buttons) > 0, "Không tìm thấy nút 'Book Now'!"

# Nhấn vào nút 'Book Now' đầu tiên
book_now_buttons[0].click()
time.sleep(2)

# Kiểm tra URL đã chuyển sang trang đặt sân
assert "Bookings" in driver.current_url, "Chuyển hướng đến trang đặt sân thất bại!"
print("✅ Chuyển hướng đến trang đặt sân thành công")

# --- TEST 3: Kiểm tra ô tìm kiếm hoạt động ---
search_box = driver.find_element(By.XPATH, "//input[@type='text']")
search_box.send_keys("Sân Cầu Số 2")  # Nhập tên sân cần tìm
search_box.send_keys(Keys.RETURN)
time.sleep(2)

filtered_courts = driver.find_elements(By.TAG_NAME, "tr")
assert len(filtered_courts) <= len(court_rows), "Tìm kiếm không hoạt động đúng!"
print("✅ Chức năng tìm kiếm hoạt động chính xác")

# Đóng trình duyệt sau khi hoàn thành kiểm thử
print("Kiểm thử hoàn tất, đóng trình duyệt...")
driver.quit()
