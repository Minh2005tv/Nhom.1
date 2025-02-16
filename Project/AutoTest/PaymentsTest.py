from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("http://localhost:8000/Payments") 
    
    
    input("Nhập thông tin vào form, sau đó nhấn Enter để tiếp tục kiểm thử...")

    try:
        pay_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-success")))
        pay_button.click()
    except:
        print("Thanh toán thành công!.")
    else:
        try:
            alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
            print(f"✅ Kết quả kiểm thử: {alert.text}")  
            alert.accept()  
        except:
            print("⚠️ Không có thông báo nào xuất hiện!")

finally:
    input("Nhấn Enter để đóng trình duyệt...")
    driver.quit()
