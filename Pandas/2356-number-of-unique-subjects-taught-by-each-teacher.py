import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    #b.columns = ['teacher_id', 'cnt']
    #return b
    return df.rename({'subject_id':'cnt'},axis=1)