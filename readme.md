OTP Generator Web App
Ứng dụng web tạo mã OTP (TOTP/HOTP) dựa trên HMAC-SHA1 để minh họa xác thực hai yếu tố (2FA). Được xây dựng bằng Flask (Python) với giao diện Bootstrap.
Cài đặt

Clone repository:
git clone <your-repo-url>
cd otp_web_app


Tạo môi trường  ascended
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Cài đặt các thư viện:
pip install -r requirements.txt


Chạy ứng dụng:
python app.py


Truy cập http://127.0.0.1:5000 trên trình duyệt.


Deploy lên Heroku

Cài Heroku CLI và đăng nhập:
heroku login


Tạo ứng dụng Heroku:
heroku create


Thêm file Procfile:
web: python app.py


Đẩy code lên Heroku:
git push heroku main



Cách sử dụng

Nhập secret key (base32, ví dụ: JBSWY3DPEHPK3PXP).
Chọn chế độ TOTP hoặc HOTP.
Xem mã OTP và QR code. TOTP tự động refresh sau 30 giây.

Công nghệ

Backend: Flask, Python
Frontend: Bootstrap 5, HTML, CSS, JavaScript
Thư viện: qrcode và Pillow để tạo QR code

Lưu ý

Secret key chỉ dùng cho demo, không lưu trữ thật.
Dự án minh họa, không sử dụng SHA1 cho ứng dụng thực tế (dùng SHA256 thay thế).
