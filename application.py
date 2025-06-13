from flask import Flask, request, jsonify

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho API
@app.route('/predict', methods=['POST'])
def predict():
    # Nhận dữ liệu từ yêu cầu POST
    data = request.get_json()

    # Lấy email_content từ yêu cầu JSON
    email_content = data['email_content']

    # Dự đoán (ví dụ đơn giản: nếu từ "free" có trong email thì spam)
    if 'free' in email_content.lower():
        prediction = 'spam'
    else:
        prediction = 'ham'

    # Trả kết quả dự đoán
    return jsonify({'prediction': prediction})

# Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
