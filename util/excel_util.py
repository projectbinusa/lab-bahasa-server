import pandas as pd


def export_to_excel(data, file_path):
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False)
    return file_path


def import_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')
