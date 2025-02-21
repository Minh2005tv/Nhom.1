import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):
    def setUp(self):
        """Khởi tạo trình duyệt trước mỗi test case"""
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/customer-login/")
    
    def tearDown(self):
        """Đóng trình duyệt sau mỗi test case"""
        time.sleep(5)
        self.driver.quit()
    
    def login(self, username, password):
        """Hàm thực hiện đăng nhập"""
        driver = self.driver
        
        # Tìm input username
        inputUserName = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        inputUserName.send_keys(username)
        time.sleep(3)
        
        # Tìm input password
        passwordInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        passwordInput.send_keys(password)
        time.sleep(3)
        
        # Nhấn ENTER để đăng nhập
        passwordInput.send_keys(Keys.RETURN)
        
    def test_correct_username_correct_password(self):
        """Nhập đúng cả tài khoản và mật khẩu -> Đăng nhập thành công"""
        self.login("abc", "123456")
        WebDriverWait(self.driver, 7).until(
            EC.title_contains("Navbar with Search")
        )
        print("Đăng nhập thành công!")
    
    def test_correct_username_wrong_password(self):
        """Nhập đúng tài khoản, sai mật khẩu -> Đăng nhập thất bại"""
        self.login("abc", "1")
        WebDriverWait(self.driver, 7).until(
            EC.title_contains("Badminton Booking")
        )
        print("Đăng nhập thất bại!")
    
    def test_wrong_username_correct_password(self):
        """Nhập sai tài khoản, đúng mật khẩu -> Đăng nhập thất bại"""
        self.login("abcd", "123456")
        WebDriverWait(self.driver, 7).until(
            EC.title_contains("Badminton Booking")
        )
        print("Đăng nhập thất bại!")
    
    def test_empty_username_and_password(self):
        """Không nhập gì cả -> Đăng nhập thất bại"""
        self.login("", "")
        WebDriverWait(self.driver, 7).until(
            EC.title_contains("Badminton Booking")
        )
        print("Đăng nhập thất bại!")

if __name__ == "__main__":
    unittest.main()
