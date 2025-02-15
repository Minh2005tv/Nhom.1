import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminLoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def tearDown(self):
        self.driver.quit()
        
    def test_user_can_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")

        try:
            # Tìm input username
            inputUserName = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            inputUserName.send_keys("admin")

            # Tìm input password
            password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            password.send_keys("your_password")  # Thay bằng mật khẩu thực tế

            # Gửi phím RETURN
            password.send_keys(Keys.RETURN)

            # Chờ trang tải hoàn tất
            WebDriverWait(driver, 10).until(
                EC.title_contains("Site administration")
            )

            actualTitle = driver.title
            print("Đăng nhập thành công, tiêu đề trang:", actualTitle)
            self.assertEqual(actualTitle, "Site administration | Django site admin")

        except Exception as e:
            print(f"Lỗi xảy ra: {e}")
            self.fail("Test thất bại do lỗi trên.")

if __name__ == "__main__":
    unittest.main()