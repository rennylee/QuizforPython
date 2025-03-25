from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods=['POST'])

def upload_csv():

    file = request.files['file']

    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    try:
        df = pd.read_csv(file)

        insights = {
            "message": "CSV processed successfully",
            "row_count": len(df),
            "columns": df.columns.tolist(),
            "sample_data": df.head(5).to_dict(orient="records")
        }

        return jsonify(insights), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
