import pandas as pd

sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}

df = pd.DataFrame(sample_data)
tb_korelasi = df.corr(numeric_only=True)

# CETAK TABEL KORELASI
print(tb_korelasi)

tb_covariance = df.cov(numeric_only=True)

# CETAK TABEL COVARIANCE
print(tb_covariance)
