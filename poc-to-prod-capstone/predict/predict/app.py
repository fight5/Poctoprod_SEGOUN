from flask import Flask, request, render_template_string
from predict.predict.run import TextPredictionModel
app = Flask(__name__)
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>StackOverflow Tags Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f7f7f7;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        form {
            text-align: center;
            margin-top: 20px;
        }
        textarea {
            width: 80%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: vertical;
        }
        button {
            padding: 10px 20px;
            background-color: #0000FF;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .predictions {
            margin-top: 20px;
            text-align: center;
        }
        .predictions ul {
            list-style-type: none;
            padding: 0;
        }
        .predictions li {
            display: inline-block;
            margin: 5px;
            padding: 8px 16px;
            background-color: #ddd;
            border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h2>Tag Prediction</h2>
    <form action="/" method="post">
        <textarea name="text" rows="4" placeholder="Hey...,type your title here"></textarea><br>
        <button type="submit">Predict</button>
    </form>
    {% if predictions %}
    <div class="predictions">
        <strong>Predictions:</strong>
        <ul>
            {% for prediction in predictions %}
                <li>{{ prediction }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %}
     <div class="gif-container">
        <p align="center">
        <img src="https://media.giphy.com/media/PMVL0gikEmYBygyzL0/giphy.gif" alt="MAFS GIF" align = "center" >
        </p>
    </div>
</body>
</html>
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    predictions = None
    if request.method == 'POST':
        text_list = [request.form['text']]
        model = TextPredictionModel.from_artefacts('C:\\Data engineering 4th year\\Poc to prod\\poc-to-prod-capstone\\train\\data\\artefacts')
        predictions = model.predict(text_list)
    return render_template_string(HTML_TEMPLATE, predictions=predictions)
if __name__ == '__main__':
    app.run(debug=True)
