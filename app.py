from flask import Flask, jsonify
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

@app.route('/time', methods=['POST'])
def get_iran_time():
    tehran_tz = ZoneInfo("Asia/Tehran")
    current_time = datetime.now(tehran_tz)
    
    return jsonify({
        "time": current_time.strftime("%H:%M:%S")
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
