import pandas as pd
import constant as constant
import matplotlib.pyplot as plt


class UniversityAnalysis:
    df_universities = pd.DataFrame()
    df_uni_count_by_region = pd.DataFrame()

    def __init__(self):
        self.import_universities()

    @classmethod
    def import_universities(cls):
        if cls.df_universities.empty:
            df = pd.read_json('data/thailand_universities.json')
            cls.df_universities = df[['name', 'state-province']]

    @classmethod
    def get_uni_count_by_region(cls):
        df_grp = cls.df_universities
        df_grp = df_grp.groupby(['state-province']).count().reset_index().rename(columns={'name': 'count'})
        df_grp = df_grp.sort_values(by='count', ascending=False)
        cls.df_uni_count_by_region = df_grp
        df_grp.to_csv('uni_count_by_region.csv', sep='|', index=False)
        return df_grp

    @classmethod
    def create_chart(cls):
        if cls.df_uni_count_by_region.empty:
            cls.get_uni_count_by_region()
        fig = cls.df_uni_count_by_region.plot.bar(x='state-province', y='count', title='Universities count by region.',
                                                  figsize=(10, 8)).get_figure()
        plt.subplots_adjust(bottom=.3)
        fig.savefig('./static/assets/barchart.jpg')

    @classmethod
    def get_intermediate_result(cls):
        cls.get_uni_count_by_region()
        df_grp = cls.df_uni_count_by_region
        dff = pd.merge(cls.df_universities, df_grp, on='state-province').sort_values(by='count', ascending=False)
        dff = dff[['state-province', 'name', 'count']]
        dff.to_csv('intermediate_result.csv', sep='|', index=False)
        return dff

    @classmethod
    def get_accordion_data(cls):
        df = cls.df_universities
        df_grp = cls.get_uni_count_by_region()
        df = df.groupby('state-province')['name'].apply(
            lambda x: ','.join(x.str.strip().replace(',', ''))).reset_index()
        df = pd.merge(df, df_grp, on='state-province').sort_values(by='count', ascending=False)
        df.to_csv('accordion_data.csv', sep='|', index=False)
        return df
