from flask import Flask, request
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form{{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-redius: 10px;
                }}
                textarea{{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method = 'POST'>
                <label>
                    Rotate by:
                    <input name='rot' type='text' value='0' />
                </label>
                <textarea name='text'>{0}</textarea>
                <input type="submit" value="Submit Query" />
            </form>
        </body>
    </html>
"""

@app.route("/")
def index():
    empty_string = ''
    return form.format(empty_string)

@app.route("/", methods=['POST'])
def encrypt():
    rot_input = int(request.form['rot'])
    message_input = request.form['text']
    encryption = rotate_string(message_input, rot_input)
    return form.format(encryption)

app.run()