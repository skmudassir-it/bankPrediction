from flask import Flask, redirect, render_template, request, url_for
import joblib
app = Flask(__name__)
solve = joblib.load('model')

@app.route('/', methods=['POST','GET'])
def home():
    sol = ''
    if request.method == 'POST':
        Age = float(request.form.get('age'))
        Job = float(request.form.get('job'))
        Sal = float(request.form.get('sal'))
        Rel = float(request.form.get('relation'))
        Edu = float(request.form.get('edu'))
        Def = float(request.form.get('def'))
        HouseL = float(request.form.get('hl'))
        PersonalL = float(request.form.get('pl'))
        m = [[Age,Job,Sal,Rel,Edu,Def,HouseL,PersonalL]]
        sol = solve.predict(m)
    return render_template('index.html',result = sol)

if __name__ == '__main__':
    app.run(debug = True)
