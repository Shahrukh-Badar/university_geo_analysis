from flask import Flask, escape, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


#
@app.route('/main')
def main():
    df = pd.read_csv('intermediate_res_2.csv', sep='|')
    return render_template('render_accordion.html', title='Top 2 Choices',
                           result=list(df.loc[:1].to_records(index=False)))


@app.route('/universities_by_region')
def universities_by_region():
    df = pd.read_csv('intermediate_res_1.csv', sep='|')
    return render_template('render_dataframe.html', title='Universities count by region', tables=[
        df.to_html(classes=["table", "table-striped"], index=False, justify='left').replace("<thead>",
                                                                                            "<thead class='thead-dark'>")],
                           titles=df.columns.values)


@app.route('/barchart')
def barchart():
    return render_template('render_image.html', title='Bar Chart')


@app.route('/university_count_by_region')
def university_count_by_region():
    df = pd.read_csv('intermediate_res.csv', sep='|')
    return render_template('render_dataframe.html', title='Universities count by region', tables=[
        df.to_html(classes=["table", "table-striped"], index=False, justify='left').replace("<thead>",
                                                                                            "<thead class='thead-dark'>")],
                           titles=df.columns.values)


# if __name__ == "__main__":
#     app.run(debug=True)
