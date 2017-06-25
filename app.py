from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-time')
def get_time():
    dt = datetime.datetime.now()
    dt = dt.timetuple()
    total_seconds = dt[3]*3600 + dt[4]*60 + dt[5]
    if dt[3] >= 10:
        hour = str(dt[3])
    else:
        hour = "0" + str(dt[3])
    if dt[4] >= 10:
        minute = str(dt[4])
    else:
        minute = "0" + str(dt[4])
    if dt[5] >= 10:
        seconds = str(dt[5])
    else:
        seconds = "0" + str(dt[5])
    time_array = [hour, minute, seconds]
    return render_template('time.html', time_array=time_array, total_seconds=total_seconds)

"""@app.route('/enter')
def enter():

@app.route('/exit')
def exit():

@app.route('/list')
def list():"""

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
