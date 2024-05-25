import streamlit as st
from streamlit_option_menu import option_menu 
import numpy as np
import time 
import json
import requests 
from streamlit_lottie import st_lottie
from PIL import Image

def absolute_value(x):
    return (x**2) ** 0.5

with st.sidebar:
    selected_option = option_menu("ChemCals", options=["Beranda","Tentang Aplikasi", "Profil Kelompok", "Mulai Menghitung"], icons=["house-door","exclamation-circle", "person-raised-hand", "menu-button-wide"])

if selected_option == 'Beranda':
    # Tulis konten halaman sambutan
    # Menampilkan teks dengan Markdown yang telah diatur ukuran dan gayanya
    st.markdown("<h1 style='text-align: center; font-weight: bold;'>Welcome to ChemCals!</h1>", unsafe_allow_html=True)
   
    # Tambahan Animasi
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_hello = load_lottieurl("https://lottie.host/d509f90b-01d5-4dbc-9600-15f8ba10e7df/GE425GErWs.json")
    
    # Menampilkan animasi Lottie di tengah halaman
    st_lottie_container = st.empty()
    with st_lottie_container.container():
        st_lottie(lottie_hello, speed=0.6, reverse=False, loop=True, quality="medium", height=500)
    st.markdown("""
        <style>
            .stLottie > div:first-child {
                display: block;
                margin: 0 auto;
            }
        </style>
    """, unsafe_allow_html=True)
    # Menampilkan teks dengan Markdown yang telah diatur ke tengah
    st.markdown("<center>We Help you to Ease your Analyst Process</center>", unsafe_allow_html=True)
        
elif selected_option == 'Tentang Aplikasi':
    selected_option = option_menu(menu_title=None, options=['Profil Aplikasi ChemCals','Materi Standardisasi' ], icons=["glass-hour","glass-hour"], orientation='horizontal')
    
    if selected_option == 'Profil Aplikasi ChemCals':
        st.header('Profil Aplikasi ChemCals')
        st.subheader("**Deskripsi**")
        text = """
        ChemCalcs adalah aplikasi berbasis website dengan bahasa pemrograman Python yang berguna untuk menghitung konsentrasi senyawa hasil standarisasi dalam berbagai reaksi kimia analisis, termasuk standarisasi NaOH, HCl, KMnO4, Tiosulfat, dan EDTA. Aplikasi ini dirancang untuk mempermudah praktisi kimia analisis dalam melakukan perhitungan konsentrasi dengan akurat dan efisien.
        """
        # Untuk membuat text justified
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader("**Fungsi**")
        multiline_text="1. Menghitung konsentrasi senyawa hasil standardisasi \n 2. Menghitung nilai rata-rata konsentrasi senyawa hasil standardisasi \n 3. Menghitung nilai Standar Deviasi (SD) Konsentrasi Senyawa (Untuk sampel *triplo*) \n 4. Menghitung nilai Persen Relatif Standar Deviasi (%RSD) (untuk sampel *triplo*) \n 5. Menghitung Persen Relatif Persen Difference (%RPD) (untuk sampel *duplo*)"
        st.write(multiline_text)
        st.subheader("**Cara Pemakaian**")
        text = """
        1. Pilih senyawa yang akan distandarisasi dari pilihan yang disediakan, yaitu NaOH, HCl, KMnO4, Tiosulfat, atau EDTA 
        2. Pilih pengulangan titrasi yang dilakukan (*duplo* atau *triplo*) 
        3. Masukkan bobot senyawa standar baku primer sesuai hasil penimbangan, volume titran hasil titrasi, serta faktor pengali
        4. Tekan tombol 'Hitung' dan tunggu beberapa saat sampai hasil perhitungan keluar
        """
        # Untuk membuat text justified
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.divider()
        text = """
        *Catatan:*
        
        • ChemCals hanya dapat menghitung dan mengolah data hasil strandardisasi dengan metode titrasi secara tidak langsung
        
        • BE dan BM Setiap molekul sudah ditetapkan dan dihitung berdasarkan ketentuan dalam IUPAC Technical Report *Pure Appl. Chem., Vol. 81, No. 11, pp. 2131-2156, 2009.*
    
        """
        # Untuk membuat text justified
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.header('Materi Standardisasi')
        st.subheader('**Pengertian Standardisasi Senyawa**')
        text = """
        Standardisasi larutan merupakan proses saat konsentrasi larutan standar sekunder ditentukan dengan tepat dengan cara mentitrasi menggunaka larutan standar primer. Larutan standar primer adalah larutan yang konsentrasinya harus diketahui dengan teliti dengan cara penimbangan zat yang dilarutkan dalam volume tertentu. Sedangkan larutan standar sekunder adalah larutan standar yang dipersiapkan dengan menimbang dan melarutkan suatu zat tertentu dengan kemurnian relatif rendah sehingga konsentrasi diketahui dari hasil standardisasi.
        
        Standardisasi penting dilakukan agar senyawa kimia dapat digunakan dengan lebih aman, efektif, dan andal dalam berbagai aplikasi, mulai dari penelitian ilmiah hingga produksi industri dan penggunaan medis.
        """
        # Untuk membuat text justified
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Rumus-Rumus dalam Pengolahan Data Hasil Standardisasi**')
        gambar1 = Image.open('Rumus ChemCals.jpg')
        st.image(gambar1, caption='Rumus-Rumus dalam Pengolahan Data Hasil Standardisasi', use_column_width=True)
    
        st.subheader('**Normalitas (N)**')
        text = """
        Normalitas merupakan satuan konsentrasi suatu senyawa yang menggambarkan jumlah gram ekuivalen senyawa yang ada dalam larutan.
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Molaritas (M)**')
        text = """
        Molaritas adalah satuan konsentrasi suatu senyawa yang menggambarkan jumlah mol yang ada dalam larutan.
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Rata-Rata**')
        text = """
        Rata-rata yang dimaksud dalam standardisasi adalah nilai rata-rata dari Normalitas atau Molaritas senyawa yang sudah distandardisasi.
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Relative Persen Difference (%RPD)**')
        text = """
        Relative Persen Difference (%RPD) yaitu ukuran statistik yang digunakan untuk mengevaluasi perbedaan antara dua pengukuran. Nilai %RPD digunakan dalam pengolahan data hasil standardisasi secara duplo (dua kali pengulangan).
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Standar Deviasi (SD)**')
        text = """
        Standar Deviasi (SD) adalah ukuran statistik yang digunakan untuk mengukur sejauh mana data dalam sebuah himpunan cenderung bervariasi dari nilai rata-ratanya. Semakin tinggi nilai SD, maka semakin besar variasi data, artinya tingkat ketelitian hasil analisis rendah.
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
        st.subheader('**Relative Standar Deviasi (%RSD)**')
        text = """
        Relative Standar Deviasi (%RSD) adalah nilai absolut dari koefisien variasi. Nilai %RSD digunakan dalam pengolahan data hasil standardisasi secara triplo (tiga kali pengulangan).
        """
        html_content = f"""
        <div style="text-align: justify;">
            {text}
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
elif selected_option == 'Profil Kelompok':
    st.header('PROFIL KELOMPOK 3')
    gambar2 = Image.open('Chemcals Team.jpg')
    st.image(gambar2, use_column_width=True)
    text = """
    Kami adalah kelompok mahasiswa jurusan kimia analisis yang berdedikasi untuk mengembangkan aplikasi Python yang berguna bagi praktisi kimia analisis. Dengan pengetahuan mendalam tentang konsep kimia analisis dan keterampilan pemrograman, kami bertekad untuk menciptakan alat yang dapat membantu dalam perhitungan konsentrasi senyawa hasil standardisasi secara efisien dan akurat.
    """
    # Untuk membuat text justified
    html_content = f"""
    <div style="text-align: justify;">
        {text}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.subheader("**Anggota:**")
    text = """ 
    1. Devrilla Raffania Chandwita (2360102)
    2. Najwah Tsuroyya Mansyur (2360202)
    3. Nisvatul Laili (236014)
    4. Rafif Adli (2360230)
    5. Rahmi Utami Mulyadi (2360231)
    """
     # Untuk membuat text justified
    html_content = f"""
    <div style="text-align: justify;">
        {text}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    st.subheader("**Tujuan Kelompok**")
    text = """
    Mengembangkan aplikasi berbasis website dengan bahasa pemrograman Python yang dapat menghitung konsentrasi senyawa hasil standardisasi berdasarkan data percobaan kimia analisis dengan akurasi tinggi dan kemudahan penggunaan untuk mempercepat proses pengolahan data hasil analisis di laboratorium.
    """
     # Untuk membuat text justified
    html_content = f"""
    <div style="text-align: justify;">
        {text}
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)
    
else :
    st.title("ChemCals")
    selected_option = option_menu(menu_title=None, options=['NaOH','HCl', 'KMnO4', 'Tiosulfat','EDTA' ], icons=["glass-hour","glass-hour","glass-hour","glass-hour","glass-hour"], orientation='horizontal')

    #Konten halaman berdasarkan pilihan pengguna
    if selected_option == 'NaOH':
        # Standardisasi NaOH dengan Asam Oksalat
        berat_molekul = 63.03272 #satuan mg/mgrek
        selected_option = option_menu(menu_title=None, options=["Duplo","Triplo"], icons=["2-square", "3-square"], orientation="horizontal")
        st.header('Standardisasi NaOH dengan Asam Oksalat')
        st.write('**Silakan Masukkan Data Hasil Titrasi Anda**')

        if selected_option == "Duplo":
            massa_oksalat = st.number_input('Masukkan Massa Oksalat Hasil Penimbangan (mg)', placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali',value=0, placeholder="Ketikkan angka di sini...")
            col1,col2 = st.columns(2)
            with col1:
                number_one = st.number_input('Masukkan volume titran pertama (mL)', placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input('Masukkan volume titran kedua (mL)', placeholder="Ketikkan angka di sini...")
            
        
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one and number_two and massa_oksalat and massa_oksalat and faktor_pengali != 0:
                    Konsentrasi_NaOH_satu = massa_oksalat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_NaOH_dua = massa_oksalat/(faktor_pengali*number_two*berat_molekul)
                    Rata_rata_konsentrasi_NaOH = (Konsentrasi_NaOH_satu + Konsentrasi_NaOH_dua)/2
                    persen_RPD = ((absolute_value(Konsentrasi_NaOH_satu-Konsentrasi_NaOH_dua))/Rata_rata_konsentrasi_NaOH)*100
                    st.write(f'Konsentrasi NaOH pertama = {Konsentrasi_NaOH_satu:.4f}N')
                    st.write(f'Konsentrasi NaOH kedua = {Konsentrasi_NaOH_dua:.4f}N')
                    st.write(f'Rata_rata_konsentrasi_NaOH = {Rata_rata_konsentrasi_NaOH:.4f}N')
                    st.write(f'% RPD = {persen_RPD:.2f}%')
                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                    st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')

        else:
            massa_oksalat = st.number_input('Masukkan Massa Oksalat Hasil Penimbangan (mg)', placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1,col2,col3 = st.columns(3)
            with col1:
                number_one = st.number_input('Masukkan volume titran pertama (mL)', placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input('Masukkan volume titran kedua (mL)', placeholder="Ketikkan angka di sini...")
            with col3: 
                number_three = st.number_input('Masukkan volume titran ketiga (mL)', placeholder="Ketikkan angka di sini...")
            
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one and number_two and number_three and massa_oksalat and faktor_pengali != 0:
                    Konsentrasi_NaOH_satu = massa_oksalat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_NaOH_dua = massa_oksalat/(faktor_pengali*number_two*berat_molekul)
                    Konsentrasi_NaOH_tiga = massa_oksalat/(faktor_pengali*number_three*berat_molekul)
                    Rata_rata_konsentrasi_NaOH = (Konsentrasi_NaOH_satu + Konsentrasi_NaOH_dua + Konsentrasi_NaOH_tiga)/3
                    SD_NaOH = (((Konsentrasi_NaOH_satu-Rata_rata_konsentrasi_NaOH)**2+(Konsentrasi_NaOH_dua-Rata_rata_konsentrasi_NaOH)**2+(Konsentrasi_NaOH_tiga-Rata_rata_konsentrasi_NaOH)**2)/(3-1))**0.5
                    persen_RSD = (SD_NaOH/Rata_rata_konsentrasi_NaOH)*100

                    st.write(f'Konsentrasi NaOH pertama = {Konsentrasi_NaOH_satu:.4f}N')
                    st.write(f'Konsentrasi NaOH kedua = {Konsentrasi_NaOH_dua:.4f}N')
                    st.write(f'Konsentrasi NaOH ketiga = {Konsentrasi_NaOH_tiga:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi NaOH = {Rata_rata_konsentrasi_NaOH:.4f}N')
                    st.write(f'SD = {SD_NaOH:.4f}N')
                    st.write(f'% RSD = {persen_RSD:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                    st.error('Silakan lengkapi data Anda', icon="⚠️")
    
    elif selected_option == 'HCl':
        # Standardisasi HCl dengan Boraks
        berat_molekul = 190.6861 #satuan mg/mgrek
        selected_option = option_menu(menu_title=None, options=["Duplo","Triplo"], icons=["2-square", "3-square"], orientation="horizontal")
        st.header('Standardisasi HCl dengan Boraks')
        st.write('**Silakan Masukkan Data Hasil Titrasi Anda**')

        if selected_option == "Duplo":        
            massa_boraks = st.number_input('Masukkan Massa Boraks Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan boraks di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2 = st.columns(2)
            with col1:
                number_one_hcl = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two_hcl = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one_hcl and number_two_hcl and massa_boraks and faktor_pengali != 0:
                    Konsentrasi_HCl_satu = massa_boraks/(faktor_pengali * number_one_hcl * berat_molekul)
                    Konsentrasi_HCl_dua = massa_boraks/(faktor_pengali * number_two_hcl * berat_molekul)
                    Rata_rata_konsentrasi_HCl = (Konsentrasi_HCl_satu + Konsentrasi_HCl_dua)/2
                    persen_RPD_HCl =((absolute_value(Konsentrasi_HCl_satu-Konsentrasi_HCl_dua))/Rata_rata_konsentrasi_HCl)*100
                    
                    st.write(f'Konsentrasi HCl pertama = {Konsentrasi_HCl_satu:.4f}N')
                    st.write(f'Konsentrasi HCl kedua = {Konsentrasi_HCl_dua:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi HCl = {Rata_rata_konsentrasi_HCl:.4f}N') 
                    st.write(f'% RPD = {persen_RPD_HCl:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                    st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ') 
        else:
            massa_boraks = st.number_input('Masukkan Massa Boraks Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan boraks di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2, col3 = st.columns(3)
            with col1:
                number_one_hcl = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two_hcl = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col3: 
                number_three_hcl = st.number_input("Masukkan volume titran ketiga (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            

            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one_hcl and number_two_hcl and number_three_hcl and massa_boraks and faktor_pengali != 0:
                    Konsentrasi_HCl_satu = massa_boraks/(faktor_pengali * number_one_hcl * berat_molekul)
                    Konsentrasi_HCl_dua = massa_boraks/(faktor_pengali * number_two_hcl * berat_molekul)
                    Konsentrasi_HCl_tiga = massa_boraks/(faktor_pengali * number_three_hcl * berat_molekul)
                    Rata_rata_konsentrasi_HCl = (Konsentrasi_HCl_satu + Konsentrasi_HCl_dua + Konsentrasi_HCl_tiga)/3
                    SD_HCl= ((Konsentrasi_HCl_satu-Rata_rata_konsentrasi_HCl)**2+(Konsentrasi_HCl_dua-Rata_rata_konsentrasi_HCl)**2+(Konsentrasi_HCl_tiga-Rata_rata_konsentrasi_HCl)**2)/2
                    persen_RSD_HCl = (SD_HCl/Rata_rata_konsentrasi_HCl)*100
            
                    st.write(f'Konsentrasi HCl pertama = {Konsentrasi_HCl_satu:.4f}N')
                    st.write(f'Konsentrasi HCl kedua = {Konsentrasi_HCl_dua:.4f}N')
                    st.write(f'Konsentrasi HCl ketiga = {Konsentrasi_HCl_tiga:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi HCl = {Rata_rata_konsentrasi_HCl:.4f}N') 
                    st.write(f'SD = {SD_HCl:.4f}N')
                    st.write(f'% RSD = {persen_RSD_HCl:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                    st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ') 

    elif selected_option =='KMnO4':
        # Standardisasi KMnO4 dengan Asam Oksalat
        berat_molekul = 63.03272 #satuan mg/mgrek
        selected_option = option_menu(menu_title=None, options=["Duplo","Triplo"], icons=["2-square", "3-square"], orientation="horizontal")
        st.header('Standardisasi KMnO4 dengan Asam Oksalat')
        st.write('**Silakan Masukkan Data Hasil Titrasi Anda**')

        if selected_option == "Duplo": 
            massa_oksalat = st.number_input('Masukkan Massa Oksalat Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2 = st.columns(2)
            with col1:
                number_one = st.number_input('Masukkan volume titran pertama (mL)', value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input('Masukkan volume titran kedua (mL)', value=0.00, placeholder="Ketikkan angka di sini...")
        
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one and number_two and massa_oksalat and faktor_pengali != 0:
                    Konsentrasi_KMnO4_satu = massa_oksalat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_KMnO4_dua = massa_oksalat/(faktor_pengali*number_two*berat_molekul)
                    Rata_rata_konsentrasi_KMnO4 = (Konsentrasi_KMnO4_satu + Konsentrasi_KMnO4_dua)/2
                    persen_RPD = ((absolute_value(Konsentrasi_KMnO4_satu-Konsentrasi_KMnO4_dua))/Rata_rata_konsentrasi_KMnO4)*100

                    st.write(f'Konsentrasi KMnO4 pertama = {Konsentrasi_KMnO4_satu:.4f}N')
                    st.write(f'Konsentrasi KMnO4 kedua = {Konsentrasi_KMnO4_dua:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi KMnO4 = {Rata_rata_konsentrasi_KMnO4:.4f}N') 
                    st.write(f'% RPD = {persen_RPD:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                    st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')
        else:     
            massa_oksalat = st.number_input('Masukkan Massa Oksalat Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali = st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1,col2,col3 = st.columns(3)
            with col1:
                number_one = st.number_input('Masukkan volume titran pertama (mL)', value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input('Masukkan volume titran kedua (mL)', value=0.00, placeholder="Ketikkan angka di sini...")
            with col3:
                number_three = st.number_input('Masukkan volume titran ketiga (mL)', value=0.00, placeholder="Ketikkan angka di sini...")
            
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if number_one and number_two and number_three and massa_oksalat and faktor_pengali != 0:
                    Konsentrasi_KMnO4_satu = massa_oksalat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_KMnO4_dua = massa_oksalat/(faktor_pengali*number_two*berat_molekul)
                    Konsentrasi_KMnO4_tiga = massa_oksalat/(faktor_pengali*number_three*berat_molekul)
                    Rata_rata_konsentrasi_KMnO4 = (Konsentrasi_KMnO4_satu + Konsentrasi_KMnO4_dua + Konsentrasi_KMnO4_tiga)/3
                    SD_KMnO4 = (((Konsentrasi_KMnO4_satu-Rata_rata_konsentrasi_KMnO4)**2+(Konsentrasi_KMnO4_dua-Rata_rata_konsentrasi_KMnO4)**2+(Konsentrasi_KMnO4_tiga-Rata_rata_konsentrasi_KMnO4)**2)/(3-1))**0.5
                    persen_RSD = (SD_KMnO4/Rata_rata_konsentrasi_KMnO4)*100

                    st.write(f'Konsentrasi KMnO4 pertama = {Konsentrasi_KMnO4_satu:.4f}N')
                    st.write(f'Konsentrasi KMnO4 kedua = {Konsentrasi_KMnO4_dua:.4f}N')
                    st.write(f'Konsentrasi KMnO4 ketiga = {Konsentrasi_KMnO4_tiga:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi KMnO4 = {Rata_rata_konsentrasi_KMnO4:.4f}N') 
                    st.write(f'SD = {SD_KMnO4:.4f}N')
                    st.write(f'% RSD = {persen_RSD:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")

                    st.divider()
                    st.button('Hitung Ulang')
                else:
                     st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ') 
    
    elif selected_option == 'Tiosulfat':
        # Standardisasi Tiosulfat dengan K2Cr2O7
        berat_molekul = 49.03073 #satuan mg/mgrek
        selected_option = option_menu(menu_title=None, options=["Duplo","Triplo"], icons=["2-square", "3-square"], orientation="horizontal")
        st.header('Standardisasi Tiosulfat dengan K2Cr2O7')
        st.write('**Silakan Masukkan Data Hasil Titrasi Anda**')

        if selected_option == "Duplo": 
            massa_bikromat = st.number_input('Masukkan Massa K2Cr2O7 Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali= st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2 = st.columns(2)
            with col1:
                number_one = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
           
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if massa_bikromat and number_one and number_two and faktor_pengali !=0:
                    Konsentrasi_Tio_satu = massa_bikromat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_Tio_dua = massa_bikromat/(faktor_pengali*number_two*berat_molekul)
                    Rata_rata_konsentrasi_Tio = (Konsentrasi_Tio_satu + Konsentrasi_Tio_dua)/2
                    persen_RPD_Tio =((absolute_value(Konsentrasi_Tio_satu-Konsentrasi_Tio_dua))/Rata_rata_konsentrasi_Tio)*100

                    st.write(f'Konsentrasi Tio pertama = {Konsentrasi_Tio_satu:.4f}N')
                    st.write(f'Konsentrasi Tio kedua = {Konsentrasi_Tio_dua:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi Tio = {Rata_rata_konsentrasi_Tio:.4f}N') 
                    st.write(f'% RPD = {persen_RPD_Tio:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")

                    st.divider()
                    st.button('Hitung Ulang')
                else:
                     st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')
        else:
            massa_bikromat = st.number_input('Masukkan Massa K2Cr2O7 Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali= st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2, col3 = st.columns(3)
            with col1:
                number_one = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col3:
                number_three = st.number_input("Masukkan volume titran ketiga (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if massa_bikromat and number_one and number_two and number_three and faktor_pengali:
                    Konsentrasi_Tio_satu = massa_bikromat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_Tio_dua = massa_bikromat/(faktor_pengali*number_two*berat_molekul)
                    Konsentrasi_Tio_tiga = massa_bikromat/(faktor_pengali*number_three*berat_molekul)
                    Rata_rata_konsentrasi_Tio = (Konsentrasi_Tio_satu + Konsentrasi_Tio_dua + Konsentrasi_Tio_tiga)/3
                    SD_Tio = (((Konsentrasi_Tio_satu-Rata_rata_konsentrasi_Tio)**2+(Konsentrasi_Tio_dua-Rata_rata_konsentrasi_Tio)**2+(Konsentrasi_Tio_tiga-Rata_rata_konsentrasi_Tio)**2)/(3-1))**0.5
                    persen_RSD_Tio = (SD_Tio/Rata_rata_konsentrasi_Tio)*100

                    st.write(f'Konsentrasi Tio pertama = {Konsentrasi_Tio_satu:.4f}N')
                    st.write(f'Konsentrasi Tio kedua = {Konsentrasi_Tio_dua:.4f}N')
                    st.write(f'Konsentrasi Tio ketiga = {Konsentrasi_Tio_tiga:.4f}N')
                    st.write(f'Rata-Rata Konsentrasi Tio = {Rata_rata_konsentrasi_Tio:.4f}N') 
                    st.write(f'SD = {SD_Tio:.4f}N')
                    st.write(f'% RSD = {persen_RSD_Tio:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                     st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')
    else:
        # Standardisasi Larutan EDTA oleh CaCO3
        berat_molekul = 100.0869 #satuan mg/mmol
        selected_option = option_menu(menu_title=None, options=["Duplo","Triplo"], icons=["2-square", "3-square"], orientation="horizontal")
        st.header('Standardisasi Larutan EDTA oleh CaCO3')
        st.write('**Silakan Masukkan Data Hasil Titrasi Anda**')

        if selected_option == "Duplo": 
            massa_kalsium_karbonat = st.number_input('Masukkan Massa CaCO3 Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali= st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2 = st.columns(2)
            with col1:
                number_one = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
             
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if massa_kalsium_karbonat and number_one and number_two and faktor_pengali:
                    Konsentrasi_EDTA_satu = massa_kalsium_karbonat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_EDTA_dua = massa_kalsium_karbonat/(faktor_pengali*number_two*berat_molekul)
                    Rata_rata_konsentrasi_EDTA = (Konsentrasi_EDTA_satu + Konsentrasi_EDTA_dua)/2
                    persen_RPD_EDTA =((absolute_value(Konsentrasi_EDTA_satu-Konsentrasi_EDTA_dua))/Rata_rata_konsentrasi_EDTA)*100

                    st.write(f'Konsentrasi EDTA pertama = {Konsentrasi_EDTA_satu:.4f}M')
                    st.write(f'Konsentrasi EDTA kedua = {Konsentrasi_EDTA_dua:.4f}M')
                    st.write(f'Rata-Rata Konsentrasi EDTA = {Rata_rata_konsentrasi_EDTA:.4f}M') 
                    st.write(f'% RPD = {persen_RPD_EDTA:.4f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                     st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')

        else:
            massa_kalsium_karbonat = st.number_input('Masukkan Massa CaCO3 Hasil Penimbangan (mg)', value=0.00, placeholder='Ketikkan massa oksalat di sini...')
            faktor_pengali= st.number_input('Masukkan faktor pengali', value=0, placeholder="Ketikkan angka di sini...")
            col1, col2, col3 = st.columns(3)
            with col1:
                number_one = st.number_input("Masukkan volume titran pertama (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col2:
                number_two = st.number_input("Masukkan volume titran kedua (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
            with col3:
                number_three = st.number_input("Masukkan volume titran ketiga (mL)", value=0.00, placeholder="Ketikkan angka di sini...")
           
            if st.button('Hitung'):
                with st.spinner('Mohon Ditunggu'):
                    time.sleep(1)
                if massa_kalsium_karbonat and number_one and number_two and number_three and faktor_pengali != 0:
                    Konsentrasi_EDTA_satu = massa_kalsium_karbonat/(faktor_pengali*number_one*berat_molekul) 
                    Konsentrasi_EDTA_dua = massa_kalsium_karbonat/(faktor_pengali*number_two*berat_molekul)
                    Konsentrasi_EDTA_tiga = massa_kalsium_karbonat/(faktor_pengali*number_three*berat_molekul)
                    Rata_rata_konsentrasi_EDTA = (Konsentrasi_EDTA_satu + Konsentrasi_EDTA_dua + Konsentrasi_EDTA_tiga)/3
                    SD_EDTA = (((Konsentrasi_EDTA_satu-Rata_rata_konsentrasi_EDTA)**2+(Konsentrasi_EDTA_dua-Rata_rata_konsentrasi_EDTA)**2+(Konsentrasi_EDTA_tiga-Rata_rata_konsentrasi_EDTA)**2)/(3-1))**0.5
                    persen_RSD_EDTA = (SD_EDTA/Rata_rata_konsentrasi_EDTA)*100

                    st.write(f'Konsentrasi EDTA pertama = {Konsentrasi_EDTA_satu:.4f}M')
                    st.write(f'Konsentrasi EDTA kedua = {Konsentrasi_EDTA_dua:.4f}M')
                    st.write(f'Konsentrasi EDTA ketiga = {Konsentrasi_EDTA_tiga:.4f}M')
                    st.write(f'Rata-Rata Konsentrasi EDTA = {Rata_rata_konsentrasi_EDTA:.4f}M') 
                    st.write(f'SD = {SD_EDTA:.4f}M')
                    st.write(f'% RSD = {persen_RSD_EDTA:.2f}%')

                    st.success('Perhitungan Selesai', icon="✅")
                    st.divider()
                    st.button('Hitung Ulang')
                else:
                     st.error('Silakan lengkapi data Anda', icon="⚠️")
            else:
                st.write(' ')
