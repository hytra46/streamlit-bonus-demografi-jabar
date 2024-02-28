import streamlit as st
import altair as alt
import pandas as pd
import base64
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("ANALISIS BONUS DEMOGRAFI DI JAWA BARAT")
    st.write("Dibuat Oleh: Henry Saputra")
    st.write("Email: henrysaputra008@gmail.com")
    st.header("Pendahuluan")
    # Misalkan kita memiliki DataFrame berikut:
    usia_produktif = pd.read_excel("Streamlit Jumlah Angkatan Kerja.xlsx")

    # Membuat line chart
    chart = alt.Chart(usia_produktif).mark_line(point=True).encode(
        x=alt.X('Tahun', axis=alt.Axis(title='Tahun')),
        y=alt.Y('Jumlah Angkatan Kerja', axis=alt.Axis(title='Populasi'), scale=alt.Scale(domain=[29000000, 35000000])),
        tooltip=['Tahun', 'Jumlah Angkatan Kerja']
    ).properties(
        title='Jumlah Penduduk Jawa Barat berdasarkan Usia Produktif (15-64 Tahun)',
        width=600,
        height=400
    ).interactive()

    # Menampilkan line chart di Streamlit
    st.altair_chart(chart, use_container_width=True)
    st.write("""
    Jawa Barat diperkirakan akan mengalami bonus demografi pada tahun 2030, dengan jumlah penduduk usia produktif diperkirakan akan meningkat sekitar 60%. Bonus demografi ini dapat menjadi peluang besar bagi pembangunan ekonomi dan sosial di Jawa Barat jika dikelola dengan baik.
    """)

    st.header("Analisis")
    st.subheader("Potensi Bonus Demografi")

    # Misalkan kita memiliki DataFrame berikut:
    kelompok_usia = pd.read_excel("Streamlit Kelompok Usia 2022.xlsx")

    # Membuat donut chart
    chart = alt.Chart(kelompok_usia).mark_arc(innerRadius=95).encode(
        theta='jumlah:Q',
        color='kategori:N',
        tooltip=['kategori', 'jumlah']
    ).properties(
        width=400,
        height=400
    )

    # Menampilkan donut chart di Streamlit
    st.altair_chart(chart, use_container_width=True)

    st.write("""
    Berdasarkan data dari Badan Pusat Statistik (BPS), pada tahun 2022, Jawa Barat memiliki populasi usia produktif (15-64 tahun) sebesar **34.368.297 jiwa**, terdiri dari **17.033.643 perempuan** dan **17.334.654 laki-laki**. Jumlah tersebut mendominasi 70% dibandingkan usia non-produktif dan **mengalami peningkatan 3,19%** 
    dari pada jumlah di tahun sebelumnya. Ini menunjukkan bahwa Jawa Barat sedang berada dalam masa bonus demografi.
    """)

    st.subheader("Risiko dan Tantangan")
    # Misalkan kita memiliki DataFrame berikut:
    IPM = pd.read_excel("Streamlit IPM.xlsx")
    # Membuat bar chart
    highlight = alt.condition("datum.Provinsi == 'JAWA BARAT'", alt.value('red'), alt.value('pink'))
    chart = alt.Chart(IPM).mark_bar().encode(
        x=alt.X('Provinsi:N', sort='-y'),
        y=alt.Y('IPM:Q', axis=alt.Axis(title='IPM'), scale=alt.Scale(domain=[0, 90], )),
        color=highlight 
    ).properties(
        title='Top 10 Indeks Pembangunan Manusisa (IPM) di Indonesia (2022)',
        width=600,
        height=400
    )

    # Menampilkan bar chart di Streamlit
    st.altair_chart(chart, use_container_width=True)
    st.write("""
    Indeks Pembangunan Manusia (IPM) memiliki pengaruh yang signifikan terhadap bonus demografi. Pada tahun 2022, IPM Jawa Barat berada status ‘tinggi’ mencapai 73,12 dan menempati peringkat ke-10 secara nasional. Namun, ada risiko dan tantangan yang harus dihadapi untuk memanfaatkan bonus demografi. Berikut adalah beberapa risiko dan tantangan yang mungkin dihadapi:
    """)

    st.write("""
    1. **Pendidikan dan Keterampilan**: Jika pendidikan dan keterampilan penduduk usia produktif tidak memadai, hal ini dapat menghambat pemanfaatan bonus demografi.
    2. **Kesehatan**: Kesehatan penduduk usia produktif juga menjadi faktor penting. Jika kondisi kesehatan penduduk usia produktif buruk, hal ini dapat mengurangi produktivitas mereka.
    3. **Lapangan Pekerjaan**: Dengan meningkatnya jumlah penduduk usia produktif, kebutuhan akan lapangan pekerjaan juga akan meningkat. Jika lapangan pekerjaan tidak tersedia, hal ini dapat menyebabkan pengangguran dan kemiskinan.
    """)

    st.header("Rekomendasi")
    # Misalkan kita memiliki DataFrame berikut:
    korelasi = pd.read_excel("Streamlit Korelasi.xlsx")

    # Menghitung matriks korelasi
    corr = korelasi.corr()

    # Membuat heatmap
    plt.figure(figsize=(5, 3))
    sns.heatmap(corr, annot=True, fmt=".2f")

    # Menampilkan heatmap di Streamlit
    st.pyplot(plt.gcf())
    st.write("""
    Gambar di atas merupakan hubungan antara indeks pembangunan manusia (IPM), indeks pendidikan (IP), indeks kesehatan (IK) dan tingkat pengangguran terbuka (TPT). Nilai IPM, IP, dan IK memiliki hubungan positif yang erat, kenaikan salah satu nilai akan mempengaruhi kenaikan yang lainnya. Namun, TPT juga memiliki hubungan positf yang rendah dengan variabel lainnya. Untuk mengatasi tantangan-tantangan tersebut, berikut adalah beberapa rekomendasi:
    """)

    st.write("""
    1. **Peningkatan Kualitas Pendidikan dan Pelatihan Keterampilan**: Pemerintah perlu meningkatkan kualitas pendidikan dan menyediakan pelatihan keterampilan untuk mempersiapkan penduduk usia produktif agar siap bekerja.
    2. **Peningkatan Akses dan Kualitas Layanan Kesehatan**: Pemerintah perlu meningkatkan akses dan kualitas layanan kesehatan untuk menjaga kesehatan penduduk usia produktif.
    3. **Penciptaan Lapangan Pekerjaan**: Pemerintah perlu menciptakan lapangan pekerjaan baru dan mengembangkan sektor-sektor ekonomi yang dapat menyerap tenaga kerja.
    """)

    st.header("Kesimpulan")
    st.write("""
    Bonus demografi di Jawa Barat dapat menjadi peluang besar bagi pembangunan ekonomi dan sosial di provinsi ini. Namun, ada beberapa risiko dan tantangan yang perlu dihadapi. Dengan strategi dan kebijakan yang tepat, Jawa Barat dapat memanfaatkan bonus demografi ini untuk mencapai pertumbuhan ekonomi yang berkelanjutan.
    """)

    st.write("""
    *NO ID: TETRIS-090*
    """)

if __name__ == "__main__":
    main()  


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg('background streamlit (2).jpg')
