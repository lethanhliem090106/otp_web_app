OTP Generator Web App
Ứng dụng web tạo mã OTP (TOTP/HOTP) dựa trên HMAC-SHA1 để minh họa xác thực hai yếu tố (2FA). Được xây dựng bằng Flask (Python) với giao diện Bootstrap.
Cài đặt

Clone source về:
git clone https://github.com/lethanhliem090106/otp_web_app.git

Truy cập và thư mục source code:
cd otp_web_app

Cài đặt những thành phần phụ thuộc khi để chạy app:

khi dùng Windows:
pip install -r requirements.txt 

khi dùng Ubuntu:
sudo apt install python3-flask python3-qrcode python3-pil python-is-python3 

Chạy ứng dụng: 
python ./app.py

Truy cập http://127.0.0.1:5000 trên trình duyệt để test.



Công nghệ

Backend: Flask, Python
Frontend: Bootstrap 5, HTML, CSS, JavaScript
Thư viện: qrcode và Pillow để tạo QR code

Lưu ý

Secret key chỉ dùng cho demo, không lưu trữ thật.
Dự án minh họa, không sử dụng SHA1 cho ứng dụng thực tế (dùng SHA256 thay thế).
