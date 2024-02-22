import datetime
import locale

from flask import Flask, request, render_template, redirect, url_for


last_incident = 'last_incident.txt'
locale.setlocale(locale.LC_ALL, '')
app = Flask(__name__)


def new_incident():
    now = datetime.datetime.now()
    with open(last_incident, 'w') as f:
        f.write(f'{now.isoformat()}')

    return now


def incident_info(units):
    try:
        with open(last_incident, 'r') as f:
            then = datetime.datetime.fromisoformat(f.readline())
    except FileNotFoundError:
        then = new_incident()

    elapsed_time = datetime.datetime.now() - then
    elapsed_seconds = elapsed_time.total_seconds()

    match units:
        case 'days':
            elapsed_units = int(elapsed_seconds / 60 / 60 / 24)
        case 'hours':
            elapsed_units = int(elapsed_seconds / 60 / 60)
        case 'minutes':
            elapsed_units = int(elapsed_seconds / 60)
        case 'seconds':
            elapsed_units = int(elapsed_seconds)

    return elapsed_units, then.isoformat()


def display(units='days'):
    elapsed_time, last_incident = incident_info(units)
    if elapsed_time == 1:
        units = units[:-1]

    return render_template(
        'placard.html', 
        time=f'{elapsed_time:n}', 
        units=units, 
        last_incident=last_incident
    )



@app.route('/')
def index():
    return display()


@app.route('/days')
def days():
    return display('days')

@app.route('/hours')
def hours():
    return display('hours')


@app.route('/minutes')
def minutes():
    return display('minutes')


@app.route('/seconds')
def seconds():
    return display('seconds')


@app.route('/oopsie', methods=['POST'])
def oopsie():
    new_incident()
    return 'Go forth and reload!'

if __name__ == '__main__':
    app.run()
