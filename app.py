from flask import Flask, escape, request, render_template
from university_analysis import UniversityAnalysis
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/main')
def main():
    obj = UniversityAnalysis()
    return render_template('render_accordion.html', title='Top 2 Choices',
                           result=list(obj.get_accordion_data().loc[:1].to_records(index=False)))


@app.route('/universities_by_region')
def universities_by_region():
    obj = UniversityAnalysis()
    df = obj.get_intermediate_result() # pd.read_csv('intermediate_res_1.csv', sep='|')
    return render_template('render_dataframe.html', title='Universities count by region', tables=[
        df.to_html(classes=["table", "table-striped"], index=False, justify='left').replace("<thead>",
                                                                                            "<thead class='thead-dark'>")],
                           titles=df.columns.values)


@app.route('/barchart')
def barchart():
    obj = UniversityAnalysis()
    obj.create_chart()
    return render_template('render_image.html', title='Bar Chart')


@app.route('/university_count_by_region')
def university_count_by_region():
    obj = UniversityAnalysis()
    df = obj.get_uni_count_by_region() # pd.read_csv('intermediate_res.csv', sep='|')
    return render_template('render_dataframe.html', title='Universities count by region', tables=[
        df.to_html(classes=["table", "table-striped"], index=False, justify='left').replace("<thead>",
                                                                                            "<thead class='thead-dark'>")],
                           titles=df.columns.values)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
