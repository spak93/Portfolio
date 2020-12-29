from flask import Flask, render_template, url_for, request, redirect
import csv
#render_template allows us to map to html file

app = Flask(__name__) #we use Flask class to instantiate an app. This is the flask app
#print(__name__) #__name__ = 'main' because this is the main file we're running

@app.route('/') #decrorator. home page
def start_page():
    return render_template('index.html') #render the html file in the 'templates' folder

@app.route('/<string:page_name>') #takes in the hrefs from the html files
def html_page(page_name): #you cannot have functions with the same name
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csv_data:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html') #redirecting to the thank you page
        except:
            return "Could not save to database."
    else:
        return 'Something went wrong. Try again.'
