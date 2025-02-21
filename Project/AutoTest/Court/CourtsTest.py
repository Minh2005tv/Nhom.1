from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

# Cập nhật ChromeDriver tự động
chromedriver_autoinstaller.install()

# ⚙️ Cấu hình trình duyệt
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Giữ trình duyệt mở
options.add_argument("--start-maximized")  # Mở toàn màn hình
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-extensions")  # Tắt phần mở rộng

def test_courts_page():
    driver = webdriver.Chrome(options=options)
    
    try:
        print("✅ Tải trang thành công Courts...")
        driver.get("http://127.0.0.1:8000/Courts/")

        # Chờ tiêu đề trang xuất hiện
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Badminton Courts & Schedule')]"))
        )
        print("✅ Trang tải thành công")
        
        # Kiểm tra danh sách sân hiển thị
        print("🔍 Đang kiểm tra danh sách sân...")
        courts = driver.find_elements(By.XPATH, "//tr")
        if len(courts) > 1:
            print("✅ Kiểm tra danh sách sân: Thành công")
        else:
            raise Exception("Không có sân nào hiển thị!")

        # Kiểm tra chức năng Edit
        edit_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Edit')]")
        if edit_buttons:
            print("🔄 Đang kiểm tra chức năng Edit...")
            edit_buttons[0].click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Edit Court')]"))
            )
            print("✅ Kiểm tra chức năng Edit: Thành công")
            driver.back()
            time.sleep(2)
        else:
            print("⚠️ Không tìm thấy nút Edit.")

        # Kiểm tra chức năng Delete
        delete_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Delete')]")
        if delete_buttons:
            print("🔄 Đang kiểm tra chức năng Delete...")
            delete_buttons[0].click()
            time.sleep(2)
            print("✅ Kiểm tra chức năng Delete: Thành công")
        else:
            print("⚠️ Không tìm thấy nút Delete.")

        # Kiểm tra chức năng Add Court
        print("🔄 Đang kiểm tra chức năng Add Court...")
        try:
            add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Court')]")
            add_button.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Create New Court')]"))
            )
            print("✅ Kiểm tra chức năng Add Court: Thành công")
        except:
            print("❌ Lỗi: Không tìm thấy nút Add Court.")

    except Exception as e:
        print(f"❌ Lỗi xảy ra: {e}")

    finally:
        input("Nhấn Enter để thoát...")  # Giữ trình duyệt mở
        driver.quit()

if __name__ == "__main__":
    test_courts_page()
