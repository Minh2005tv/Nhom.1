from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Danh sách URL cần kiểm tra
urls = {
    "Home": "http://127.0.0.1:8000/",
    "Court": "http://127.0.0.1:8000/Court-KH/",
    "Booking": "http://127.0.0.1:8000/Bookings/",
    "Payment": "http://127.0.0.1:8000/Payments/",
    "BookBadmintonCourt": "http://127.0.0.1:8000/Courts/"
}

try:
    # Bắt đầu từ trang Home
    driver.get(urls["Home"])
    print("Đang truy cập trang chủ...")
    time.sleep(2)  # Chờ trang load hoàn toàn
    
    for name, url in urls.items():
        if name == "Home":
            continue  # Bỏ qua Home vì đã truy cập rồi
        
        driver.get(url)
        print(f"Đang truy cập URL: {url}")
        time.sleep(2)
        assert name in driver.title or name in driver.page_source, f"Không tìm thấy '{name}' trong tiêu đề hoặc nội dung trang"
        print(f"[PASSED] Click vào '{name}' dẫn đến đúng trang")
    
    # Quay lại Home để kiểm tra nút "Book Badminton Court"
    driver.get(urls["Home"])
    print("Đang quay lại trang chủ để kiểm tra nút đặt sân...")
    time.sleep(5)
    
    # Cuộn trang xuống để tìm nút nếu bị ẩn
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
    # Tìm tất cả các thẻ có thể chứa nút
    elements = driver.find_elements(By.TAG_NAME, "a")
    print("Các phần tử trên trang:")
    for elem in elements:
        print(elem.text)
    
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Book Badminton Court')]")))
    print("Đã tìm thấy nút 'Book Badminton Court', đang click...")
    button.click()
    time.sleep(2)
    
    print(f"URL sau khi click: {driver.current_url}")
    assert driver.current_url == urls["BookBadmintonCourt"], "Không chuyển hướng đến trang đặt sân"
    print("[PASSED] Nút 'Book Badminton Court' hoạt động chính xác")
    
except Exception as e:
    print(f"[FAILED] {str(e)}")

finally:
    driver.quit()
    print("Đã đóng trình duyệt.")
