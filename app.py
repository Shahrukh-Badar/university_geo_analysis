from flask import Flask, escape, request, render_template
import pandas as pd
app = Flask(__name__)

#
# @app.route('/')
# def hello():
#     name = request.args.get("name", "World")
#     # return f'Hello, {escape(name)}!'
#     df = pd.read_csv('intermediate_res.csv', sep='|')
#     return render_template('simple.html',  tables=[df.to_html(classes='table').replace("<thead>", "<thead class='thead-light'>")], titles=df.columns.values)

@app.route('/')
def home():
    df = pd.read_csv('intermediate_res.csv', sep='|')
    return render_template('base.html',  tables=[df.to_html(classes='table').replace("<thead>", "<thead class='thead-light'>")], titles=df.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
