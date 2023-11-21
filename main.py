from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store the load shedding data
# load_shedding_data = []


  


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/shed', methods=['POST', 'GET'])
def shed():
    if request.method == 'POST':
        
        req = request.form

        sub_trans = request.form['sub_trans']
        shed_megawatts = request.form['shed_megawatts']
        restored_time = request.form['restored_time']
        date = request.form['date']
        time = request.form['time']
        comments = request.form['comments']
        
        print(sub_trans, shed_megawatts, restored_time, date, time, comments)

        return redirect(request.url)

    return render_template('shed.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/restore')
def restore():
    return render_template('restore.html')

# @app.route('/submit', methods=['POST'])
# def home():
#     return render_template('success.html')
#     # sub_trans = request.form['sub_trans']
#     # shed_megawatts = request.form['shed_megawatts']
#     # restored_time = request.form['restored_time']
#     # date = request.form['date']
#     # time = request.form['time']
#     # comments = request.form['comments']

#     # load_shedding_data.append({
#     #     'sub_trans': sub_trans,
#     #     'shed_megawatts': shed_megawatts,
#     #     'restored_time': restored_time,
#     #     'date': date,
#     #     'time': time,
#     #     'comments': comments
#     # })

#     return render_template('success.html')

#  

if __name__ == '__main__':
    app.run(debug=True)
