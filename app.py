import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly

st.set_page_config(
    page_title='Analisis Perkembangan Kelapa Sawit di Indonesia', page_icon="chart_with_upwards_trend"
)

# Read Data
luas_peng = pd.read_excel('merge.xlsx',sheet_name=3)
prod_peng = pd.read_excel('merge.xlsx', sheet_name=4)
prov_sentra = pd.read_excel('merge.xlsx',sheet_name=6)
kinerja = pd.read_excel('merge.xlsx', sheet_name=5)

luas_peng['Year'] = luas_peng['Year'].apply(str)
prod_peng['Year'] = prod_peng['Year'].apply(str)

# Total Luas
total_luas = luas_peng[['Year','Total']]
total_luas.rename(columns={"Total": "Total_luas"}, inplace=True)

# Total Produksi
total_prod = prod_peng[['Year','Total']]
total_prod.rename(columns={"Total": "Total_prod"}, inplace=True)

#Merge
merge_luas_prod = pd.merge(total_luas, total_prod, on="Year")

st.title('Analisis Perkembangan Kelapa Sawit di Indonesia')
st.write("By [Ade Fasha Nugraha](https://www.linkedin.com/in/ade-fasha-nugraha-343b4312b)")

st.markdown(
    """
    <div style="text-align: justify;">
    
    Indonesia merupakan negara agraris dengan sebagian besar penduduknya bekerja di sektor pertanian. 
    Salah satu potensi ekosistem pertanian yang dimiliki Indonesia adalah tanaman kelapa sawit,
    yang memiliki peran strategis dalam pembangunan ekonomi negara ini. 
    Menurut Badan Statistik Indonesia, sektor pertanian menyerap sekitar 29,59% tenaga kerja di Indonesia. Industri kelapa sawit, 
    sebagai penghasil terbesar di dunia, telah memberikan kontribusi yang signifikan dalam menciptakan lapangan kerja,baik secara langsung maupun tidak langsung.

    Bagaimana pertumbuhan industri kelapa sawit di Indonesia?
    <div style="text-align: justify;">
    """, unsafe_allow_html=True
)
st.subheader('Luas Perkebunan Sawit Bedasarkan Penguasaan di Indonesia')
chart = alt.Chart(luas_peng).transform_fold(
    ['SmallHolders', 'Government', 'Private']
).mark_line().encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-60)),
    y='value:Q',
    color='key:N'
)
st.altair_chart(chart, use_container_width=True)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.write(
        """<div style='text-align: center'> Sumber data: Portal Satu Data Pertanian</div>""",
        unsafe_allow_html=True,
    )
st.write(
    """
    Keterangan:
    
    *) Angka Sementara
    
    **) Angka Estimasi
    """
)
st.markdown(
    """
    <div style="text-align: justify;">
    
    Dari data yang terlihat pada grafik di atas, terlihat bahwa industri kelapa sawit di Indonesia mengalami pertumbuhan yang signifikan dalam kurun waktu lima tahun, yaitu dari 2014 hingga 2018.
    Luas areal perkebunan kelapa sawit pada sektor SmallHolders atau perkebunan rakyat mengalami peningkatan dari 4,4 juta hektar pada tahun 2014 menjadi 5,9 juta hektar pada tahun 2018. Sementara itu, luas areal perkebunan kelapa sawit pada sektor swasta meningkat dari 5,6 juta hektar pada tahun 2014 menjadi 7,9 juta hektar pada tahun 2018.
    
    Namun, perkembangan luas areal perkebunan milik negara kurang mengalami perkembangan yang signifikan dalam periode yang sama. 
    Dari data tersebut dapat disimpulkan bahwa pengembangan perkebunan kelapa sawit yang dimiliki oleh rakyat dan sektor swasta memiliki peran yang sangat penting dalam pertumbuhan total industri kelapa sawit di Indonesia.
   
    **Pengembangan perkebunan milik rakyat dan milik swasta akan sangat berpengaruh terhadap pengembangan total perkebunan
    sawit di Indonesia.**
    
    </div>
    """,unsafe_allow_html=True
)

st.subheader('Perbandingan Laju Pertumbuhan Luas Areal Kelapa Sawit dan Produksi Kelapa Sawit di Indonesia')
chart = alt.Chart(merge_luas_prod).transform_fold(
    ['Total_prod', 'Total_luas']
).mark_bar().encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=-60)),
    y='value:Q',
    color='key:N'
)
# Menambahkan label pada bar chart
text = chart.mark_text(
    align='center',
    baseline='middle',
    dy=-5  # Mengatur posisi label di atas bar
).encode(
    text='value:Q', # Menampilkan nilai di atas bar
    color=alt.value('white') # Mengatur warna
)

# Menggabungkan chart dan label
chart_with_labels = (chart + text)
st.altair_chart(chart_with_labels, use_container_width=True)
kol1, kol2, kol3 = st.columns([1, 3, 1])
with kol2:
    st.markdown(
        """<div style='text-align: center'> Sumber data: Portal Satu Data Pertanian</div>
        
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div style="text-align: justify;">
    
    Terdapat hubungan kuat antara luas areal kelapa sawit dengan produksi kelapa sawit di Indonesia yang dapat dilihat pada chart
    di atas dimana seiring bertambahnya luas areal kelapa sawit maka produksi kelapa sawit juga ikut naik.
    
    Saat ini provinsi sentra yang menguasai produksi kelapa sawit di Indonesia pada tahun 2015-2020 berada di pulau Sumatera dan Kalimantan.
    Hal ini bisa terjadi dikarenakan kondisi fisik dan lingkungan pada pulau Sumatera dan Kalimantan sangat mendukung untuk perkembangan Kelapa Sawit. 
    
    </div>
    """, unsafe_allow_html=True
)
values = prov_sentra['Rata-Rata']
names = prov_sentra['Provinsi']

fig = px.pie(prov_sentra,
             values=values,
             names=names,
             title='Provinsi Sentra Produksi Kelapa Sawit di Indonesia',
             width=550,
             height=550
)

fig.update_traces(
    textposition = 'inside',
    textinfo = 'percent+label'
)
st.plotly_chart(fig, use_container_width=True)
kolom1, kolom2, kolom3 = st.columns([1, 3, 1])
with kolom2:
    st.markdown(
        """<div style='text-align: center'> Sumber data: Portal Satu Data Pertanian</div>
        
        """,
        unsafe_allow_html=True,
    )
    
st.subheader('Perkembangan Harga Tandan Buah Segar (TBS) Bulanan dalam Negeri')

freeOption = st.selectbox(
    "Pilih Tahun",
    options=('2018','2019','2020','2021')
)
chart = alt.Chart(kinerja).transform_fold(
    [freeOption]
).mark_line().encode(
    x=alt.X('Bulan', sort=None, axis=alt.Axis(labelAngle=-60)),
    y='value:Q',
    color='key:N',
)
st.altair_chart(chart, use_container_width=True)

kolom1, kolom2, kolom3 = st.columns([1, 3, 1])
with kolom2:
    st.markdown(
        """<div style='text-align: center'> Sumber data: Portal Satu Data Pertanian</div>
        
        """,
        unsafe_allow_html=True,
    )
    
st.markdown(
    """
    <div style="text-align: justify;">
    
    Harga TBS bulanan mengalami fluktuasi dari waktu ke waktu, dapat dipengaruhi oleh faktor-faktor seperti penawaran dan permintaan, kebijakan pemerintah, dan faktor-faktor ekonomi lainnya.
    Harga TBS cenderung meningkat dengan harga per tahun sebesar 13,82%. Harga tertinggi TBS
    terjadi pada bulan September 2021 sebesar Rp. 2.536 per Kg, sedangkan terendah terjadi pada bulan Desember 2018
    sebesar Rp. 1.143 per kg.
    Harga pembelian TBS merupakan harga yang ditetapkan oleh pemerintah.
    
    </div>
    """, unsafe_allow_html=True
)

st.subheader('Kesimpulan dan Rekomendasi')
st.markdown(
    """
    <div style="text-align: justify;">
    
    Terdapat variasi luas perkebunan sawit berdasarkan penguasaan di Indonesia,
    termasuk perkebunan milik perusahaan dan perkebunan rakyat.
    
    **Rekomendasi yang dapat dilakukan ialah dikarenakan perkebunan milik negara tidak mengalami perkembangan yang berarti, 
    pemerintah dapat melakukan valuasi terhadap penguasaan lahan perkebunan sawit, termasuk perlindungan terhadap hak-hak masyarakat dan upaya meningkatkan efisiensi pengelolaan perkebunan sawit.**
    
    Terdapat hubungan positif antara pertumbuhan luas areal kelapa sawit dan produksi kelapa sawit di Indonesia.
    
    **Rekomendasi yang dapat dilakukan Meningkatkan upaya pengembangan dan perluasan areal perkebunan sawit di wilayah yang memiliki potensi pertumbuhan yang baik. Selain itu, perlu dilakukan pengawasan dan pengelolaan yang baik untuk memastikan keberlanjutan produksi kelapa sawit
    pada provinsi sentra kelapa sawit untuk meningkatkan kontribusi mereka dalam industri kelapa sawit secara nasional.**
    
    Harga TBS bulanan mengalami fluktuasi dari waktu ke waktu, dapat dipengaruhi oleh faktor-faktor seperti penawaran dan permintaan, kebijakan pemerintah, dan faktor-faktor ekonomi lainnya.
    
    **Rekomendasi yang dapat dilakukan adalah pemantauan terus-menerus terhadap harga TBS dan analisis yang mendalam untuk memahami faktor-faktor yang mempengaruhi fluktuasi harga. Hal ini dapat membantu dalam pengambilan keputusan strategis terkait penentuan harga jual dan kebijakan pemasaran kelapa sawit.**
    </div>
    """, unsafe_allow_html=True
)