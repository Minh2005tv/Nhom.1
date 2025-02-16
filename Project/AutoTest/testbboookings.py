from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# URL trang Booking
booking_url = "http://127.0.0.1:8000/Bookings/?name_court=Sân%201&type_court=Indoor&cost_court=100000&location=Hà%20Nội"

try:
    # Truy cập trang đặt sân
    driver.get(booking_url)
    print("Đang truy cập trang Booking Court...")
    time.sleep(2)  

    # Kiểm tra tiêu đề trang
    assert "Booking Court" in driver.page_source, "[FAILED] Không tìm thấy tiêu đề 'Booking Court'"
    
    # Nhập thời gian bắt đầu
    start_time_input = driver.find_element(By.ID, "start_time")
    start_time_input.clear()
    start_time_input.send_keys("14:30")

    # Nhập thời gian kết thúc
    end_time_input = driver.find_element(By.ID, "end_time")
    end_time_input.clear()
    end_time_input.send_keys("15:30")

    print("[PASSED] Đã nhập thời gian thành công.")

    # Kiểm tra nút Book Now
    wait = WebDriverWait(driver, 10)
    book_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Book Now')]")))
    
    print("[PASSED] Tìm thấy nút 'Book Now', đang click...")
    book_button.click()
    time.sleep(2)

    # Kiểm tra modal xác nhận hiện ra
    assert "Xác nhận thanh toán" in driver.page_source, "[FAILED] Modal xác nhận không hiển thị"
    print("[PASSED] Modal xác nhận hiển thị đúng.")

    # Click nút xác nhận trong modal
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Xác nhận')]")))
    confirm_button.click()
    time.sleep(2)

    # Kiểm tra chuyển hướng đến trang thanh toán
    assert "Payments" in driver.current_url, "[FAILED] Không chuyển hướng đến trang thanh toán"
    print("[PASSED] Chuyển hướng đến trang thanh toán thành công.")

except Exception as e:
    print(f"[FAILED] {str(e)}")

finally:
    driver.quit()
    print("Đã đóng trình duyệt.")
