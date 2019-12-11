from flask import Flask ,render_template,url_for, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submitform', methods=['POST', 'GET'])
def submitform():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            with open('database.txt','a') as database:
                write_txt = database.write(str(data)+'\n')
            return redirect('/thankyou.html')
        except:
            return 'data is not save to database'
    else:
        return 'something went wrong'


