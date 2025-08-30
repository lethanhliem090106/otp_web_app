from flask import Flask, render_template, request, jsonify
import hmac
import hashlib
import struct
import base64
import time
import qrcode
from io import BytesIO

app = Flask(__name__)

# Hàm HOTP: Tạo mã OTP dựa trên HMAC-SHA1
def hotp(secret, counter, digits=6):
    try:
        # Chuyển secret từ base32 sang bytes
        if isinstance(secret, str):
            secret = base64.b32decode(secret.upper())
        
        # Đóng gói counter thành bytes (big-endian)
        msg = struct.pack(">Q", counter)
        
        # Tính HMAC-SHA1
        hmac_sha1 = hmac.new(secret, msg, hashlib.sha1).digest()
        
        # Truncate theo RFC 4226
        offset = hmac_sha1[-1] & 0x0F
        binary = struct.unpack(">I", hmac_sha1[offset:offset+4])[0] & 0x7FFFFFFF
        otp = binary % (10 ** digits)
        return str(otp).zfill(digits)
    except Exception as e:
        return f"Error: Invalid secret key or counter ({str(e)})"

# Hàm TOTP: Tạo mã OTP dựa trên thời gian
def totp(secret, digits=6, time_step=30, t0=0):
    current_time = int(time.time())
    counter = (current_time - t0) // time_step
    return hotp(secret, counter, digits)

# Route trang chủ
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        secret = request.form['secret'].strip().upper()
        mode = request.form['mode']
        
        # Xử lý OTP dựa trên mode
        if mode == 'HOTP':
            try:
                counter = int(request.form['counter'])
                otp = hotp(secret, counter)
            except ValueError:
                return render_template('index.html', error="Counter phải là số nguyên!")
        else:  # TOTP
            otp = totp(secret)
        
        # Tạo QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(f'otpauth://{mode.lower()}://?secret={secret}&issuer=OTPWebApp')
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_img = base64.b64encode(buffered.getvalue()).decode('utf-8')
        
        return render_template('result.html', otp=otp, mode=mode, secret=secret, qr_img=qr_img)
    
    return render_template('index.html', error=None)

# Route để refresh TOTP qua AJAX
@app.route('/totp_refresh', methods=['POST'])
def totp_refresh():
    secret = request.json.get('secret')
    if not secret:
        return jsonify({'error': 'Missing secret key'}), 400
    otp = totp(secret)
    return jsonify({'otp': otp})

if __name__ == '__main__':
    app.run(debug=True)