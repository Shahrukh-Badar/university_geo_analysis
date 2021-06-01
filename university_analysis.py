import pandas as pd
import constant as constant
import matplotlib.pyplot as plt


class UniversityAnalysis:
    df_universities = pd.DataFrame()
    df_uni_grp_by_state = pd.DataFrame()

    def __init__(self):
        self.import_universities()
        self.process_universities()

    @classmethod
    def import_universities(cls):
        df = pd.read_json(constant.INPUT_FILE_NAME)
        cls.df_universities = df[[constant.COL_NAME, constant.COL_STATE]]

    @classmethod
    def process_universities(cls):
        df_grp = cls.df_universities.groupby([constant.COL_STATE]).count().reset_index().rename(
            columns={constant.COL_NAME: constant.COL_COUNT})
        cls.df_uni_grp_by_state = df_grp.sort_values(by=constant.COL_COUNT, ascending=False)

    @classmethod
    def get_uni_count_by_region(cls):
        cls.df_uni_grp_by_state.to_csv(constant.OUTPUT_COUNT_BY_REGION, sep=constant.FILE_SEPARATOR, index=False)
        return cls.df_uni_grp_by_state

    @classmethod
    def create_chart(cls):
        fig = cls.df_uni_grp_by_state.plot.bar(x=constant.COL_STATE, y=constant.COL_COUNT,
                                               title=constant.BARCHART_TITLE,
                                               figsize=(10, 8)).get_figure()
        plt.subplots_adjust(bottom=.3)
        fig.savefig(constant.OUTPUT_BARCHART_FIGURE)

    @classmethod
    def get_intermediate_result(cls):
        df = pd.merge(cls.df_universities, cls.df_uni_grp_by_state, on=constant.COL_STATE).sort_values(
            by=constant.COL_COUNT,
            ascending=False)
        df = df[[constant.COL_STATE, constant.COL_NAME, constant.COL_COUNT]]
        df.to_csv(constant.OUTPUT_INTERMEDIATE_RESULT, sep=constant.FILE_SEPARATOR, index=False)
        return df

    @classmethod
    def get_accordion_data(cls):
        df = cls.df_universities.groupby(constant.COL_STATE)[constant.COL_NAME].apply(
            lambda x: ','.join(x.str.strip().replace(',', ''))).reset_index()
        df = pd.merge(df, cls.df_uni_grp_by_state, on=constant.COL_STATE).sort_values(by=constant.COL_COUNT,
                                                                                      ascending=False)
        df.to_csv(constant.OUTPUT_ACCORDIAN_DATA, sep=constant.FILE_SEPARATOR, index=False)
        return df
