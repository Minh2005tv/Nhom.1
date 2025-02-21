import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/register/")

# Danh sách các kịch bản kiểm thử
test_cases = [
    {  # ✅ Kịch bản hợp lệ (Thành công)
        "username": "user123",
        "email": "user123@example.com",
        "password": "SecurePass123!",
        "password2": "SecurePass123!",
        "expected": "Đăng ký thành công!"
    },
    {  # ❌ Bỏ trống tất cả các trường
        "username": "",
        "email": "",
        "password": "",
        "password2": "",
        "expected": "Hiển thị lỗi yêu cầu nhập dữ liệu."
    },
    {  # ❌ Nhập username ngắn hơn 3 ký tự
        "username": "ab",
        "email": "user123@example.com",
        "password": "SecurePass123!",
        "password2": "SecurePass123!",
        "expected": "Tên người dùng phải có ít nhất 3 ký tự."
    },
    {  # ❌ Nhập email không hợp lệ
        "username": "user123",
        "email": "user123@wrong",
        "password": "SecurePass123!",
        "password2": "SecurePass123!",
        "expected": "Email không hợp lệ."
    },
    {  # ❌ Mật khẩu quá ngắn
        "username": "user123",
        "email": "user123@example.com",
        "password": "123",
        "password2": "123",
        "expected": "Mật khẩu phải có ít nhất 8 ký tự."
    },
    {  # ❌ Mật khẩu và xác nhận mật khẩu không khớp
        "username": "user123",
        "email": "user123@example.com",
        "password": "SecurePass123!",
        "password2": "WrongPass456!",
        "expected": "Mật khẩu không khớp."
    },
    {  # ❌ Sử dụng username đã tồn tại
        "username": "admin",
        "email": "admin@example.com",
        "password": "SecurePass123!",
        "password2": "SecurePass123!",
        "expected": "Tên người dùng đã được sử dụng."
    }
]

for case in test_cases:
    try:
        # Làm mới trang để nhập dữ liệu mới
        driver.get("http://127.0.0.1:8000/register/")

        # Nhập thông tin vào form
        driver.find_element(By.NAME, "username").send_keys(case["username"])
        time.sleep(3)
        driver.find_element(By.NAME, "email").send_keys(case["email"])
        time.sleep(3)
        driver.find_element(By.NAME, "password").send_keys(case["password"])
        time.sleep(3)
        driver.find_element(By.NAME, "password2").send_keys(case["password2"])
        time.sleep(3)

        # Click vào nút đăng ký
        driver.find_element(By.XPATH, "//button[text()='Register']").click()
        time.sleep(5)

        print(f"Kết quả mong đợi: {case['expected']}")

    except Exception as e:
        print(f"Lỗi xảy ra: {e}")

# Kiểm thử nút "Login here"
try:
    driver.get("http://127.0.0.1:8000/register/")
    
    login_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Login here"))
    )
    login_link.click()

    # Kiểm tra tiêu đề trang đăng nhập
    WebDriverWait(driver, 7).until(
        EC.title_contains("Badminton Booking")
    )
    print("Chuyển đến trang đăng nhập thành công!")

except Exception as e:
    print(f"Lỗi xảy ra khi kiểm tra Login here: {e}")

finally:
    time.sleep(5)
    driver.quit()
