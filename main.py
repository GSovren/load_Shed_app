from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store the load shedding data
# load_shedding_data = []


  


@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__': 
    app.run(host='172.16.3.132') 


@app.route('/home', methods=['POST', 'GET'])
def home():
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

    return render_template('home.html')

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
