from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Khởi tạo trình duyệt WebDriver
driver = webdriver.Chrome()  # Đảm bảo đã cài đặt ChromeDriver

# Hàm chọn Edit Court ngẫu nhiên
def select_random_edit_court():
    more_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='More']")  # Tìm các nút với nhãn 'More'
    if not more_buttons:
        print("Không tìm thấy nút 'More'")
        return False
    random_button = random.choice(more_buttons)
    random_button.click()
    time.sleep(1)
    edit_option = driver.find_element(By.XPATH, "//span[text()='Edit']")
    edit_option.click()
    return True

# Kịch bản 1: Mở trang Courts
try:
    driver.get("http://127.0.0.1:8000/Courts/")
    print("Tải trang thành công")
    
    # Chọn Edit Court ngẫu nhiên
    time.sleep(2)  # Đợi tải trang hoàn tất
    if select_random_edit_court():
        print("Chuyển trang Edit thành công")
    
        # Chuyển trang Edit và nhập dữ liệu
        driver.get("http://127.0.0.1:8000/Court-edit")
        time.sleep(2)
        print("Chuyển trang Edit thành công")
    
        # Nhập dữ liệu
        input_fields = driver.find_elements(By.TAG_NAME, "input")
        for field in input_fields:
            field.send_keys("Test Data")
        print("Nhập liệu thành công")
    
        # Lưu dữ liệu
        save_button = driver.find_element(By.XPATH, "//button[@aria-label='Save']")
        save_button.click()
        time.sleep(2)
        print("Sửa sân thành công")
    
        # Trở về trang Courts
        driver.get("http://127.0.0.1:8000/Courts/")
        print("Trở về trang sân thành công")
    else:
        print("Hủy sửa sân")
        driver.get("http://127.0.0.1:8000/Courts/")
        print("Trở về trang sân thành công")

except Exception as e:
    print(f"Lỗi: {e}")

# Kịch bản 4: Xóa sân (Delete Court)
try:
    # Chọn Delete Court
    more_buttons = driver.find_elements(By.XPATH, "//button[@aria-label='More']")
    if not more_buttons:
        print("Không tìm thấy nút 'More'")
    for button in more_buttons:
        button.click()
        delete_option = driver.find_element(By.XPATH, "//span[text()='Delete']")
        delete_option.click()
        time.sleep(2)
        print("Chấp nhận xóa sân")
    
        # Xóa sân
        confirm_delete = driver.find_element(By.XPATH, "//button[@aria-label='Confirm']")
        confirm_delete.click()
        time.sleep(2)
        print("Sân đã được xóa")
    
except Exception as e:
    print(f"Lỗi: {e}")

# Đóng trình duyệt
finally:
    driver.quit()
    print("Tất cả các thao tác đã hoàn thành")
