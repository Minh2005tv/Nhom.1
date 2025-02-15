import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentsTest(unittest.TestCase):
    
    def setUp(self):
        """Khởi tạo trình duyệt trước mỗi test"""
        self.driver = webdriver.Chrome()

    def tearDown(self):
        """Đóng trình duyệt sau mỗi test"""
        self.driver.quit()

    def test_payment_process(self):
        """Test quy trình thanh toán thành công"""
        driver = self.driver
        driver.get("http://127.0.0.1:8000/Payments/")  # Cập nhật URL của bạn

        try:
            # Nhập số thẻ
            card_number = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "card_number"))
            )
            card_number.send_keys("4111111111111111")  # Thẻ hợp lệ

            # Nhập ngày hết hạn
            expiry_date = driver.find_element(By.NAME, "expiry_date")
            expiry_date.send_keys("12/25")

            # Nhập mã CVV
            cvv = driver.find_element(By.NAME, "cvv")
            cvv.send_keys("123")

            # Nhấn nút thanh toán
            pay_button = driver.find_element(By.ID, "pay-button")
            pay_button.click()

            # Chờ phản hồi
            success_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "payment-success"))
            ).text

            # Kiểm tra kết quả
            self.assertIn("Thanh toán thành công", success_message)
            print("✅ Test thanh toán thành công!")

        except Exception as e:
            print(f"❌ Lỗi kiểm thử: {e}")
            self.fail("Test thất bại do lỗi trên.")

if __name__ == "__main__":
    unittest.main()