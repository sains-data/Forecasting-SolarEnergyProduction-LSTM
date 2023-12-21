# Web Application For Stock Price Prediction

## Table Of Content

+ [Demo](#demo)
+ [Overview](#overview)
+ [Technical Aspects](#technincal)
+ [Installation](#installation)
+ [Deployment on Streamlit](#deploy)
+ [Technologies Used](#tech)
+ [Team](#team)
+ 
<a id="demo"></a><h2>Demo</h2>

### Interface
![Cuplikan layar 2023-12-21 204347](https://github.com/sains-data/Forecasting-SolarEnergyProduction-LSTM/assets/143611789/4f7cbdee-64d7-44bb-8a59-78c594393654)

**input data untuk prediksi**
![Cuplikan layar 2023-12-21 204523](https://github.com/sains-data/Forecasting-SolarEnergyProduction-LSTM/assets/143611789/fb6cd7b6-e64c-48d0-abf7-63aa514004e7)

**hasil prediksi**
![Cuplikan layar 2023-12-21 204601](https://github.com/sains-data/Forecasting-SolarEnergyProduction-LSTM/assets/143611789/aa5f80ca-f615-4397-9002-759a80883fea)

**bisa juga menggunakan data pickle**
![Cuplikan layar 2023-12-21 204618](https://github.com/sains-data/Forecasting-SolarEnergyProduction-LSTM/assets/143611789/ff40b7e9-2abb-464f-ac38-bc840a8f9482)

The App [link](https://sains-data-forecasting-solarenergyproduction-lstm-app-oywnzv.streamlit.app/)

<a id="overview"></a><h2>Overview</h2>
Ini adalah aplikasi web yang dibangun dengan menggunakan konsep **Prediksi Produksi Energi Surya**. Aplikasi web dibuat menggunakan kerangka kerja Streamlit bersama dengan TensorFlow untuk tujuan Deep Learning dan telah diterapkan di cloud streamlit. Project ini menggunakan LSTM untuk memprediksi produksi energi surya di masa mendatang, yang dipengaruhi oleh variabel-variabel eksogen. Dengan Hasil Evaluasi Matriks RMSE yaitu 523.22775.

<a id="technincal"></a><h2>Technical Aspects</h2>

Seluruh project dikerjakan menggunakan python di google colab.

### Proyek Berfungsi
Pengerjaan proyek ini dibagi menjadi 4 langkah

+ **Mengambil Data**
  + Dataset didapatkan dari website Mendeley Data, dibuat oleh California Independent System Opreator (CAISO) 
dan the National Renewable Energy Laboratory (NREL). Dataset ini merupakan produksi energi surya (PV production) setiap 5 menit dari tahun 2019 sampai tahun 2021. Serta variabel endogen atau variabel yang mempengaruhi nya mencakup season, hari dalam seminggu, radiasi matahari, kecepatan angin, kelembapan udara dan suhu udara.
  
+ **Memproses Data terlebih dahulu**
  + Saat mengambil data, kami perlu memprosesnya terlebih dahulu. Kami menggunakan LSTM karena cocok untuk analisis deret waktu. Jadi kita perlu mengubah data ke dalam format yang kompatibel dengan LSTM.

+ **Model Pelatihan**
  + Setelah pra-pemrosesan, data dikirim ke model untuk dilatih.

+ **Menghasilkan prakiraan dan menampilkan**
  + Setelah pelatihan, data baru digunakan untuk memperkirakan nilai masa depan.

<a id="installation"></a><h2>Installation</h2>
 Untuk menginstal paket dan pustaka yang diperlukan, jalankan perintah ini di direktori proyek setelah mengkloning repositori:
 ``` pip install -r requirements.txt```


<a id="running"></a><h2>Execution</h2>

```streamlit run appName.py```

+ Buat akun di streamlit
+ Hubungkan akun github Anda dengan akun streamlit.
+ Buat aplikasi dengan memilih pengaturan masing-masing seperti repositori

<a id="tech"></a><h2>Technologies Used</h2>

| Libraries        | Usage       
| ------------- |:-------------:|
**Numpy**  | Digunakan untuk komputasi numerik di Python.
 **Pandas** | Digunakan untuk membaca file dan operasi lainnya saat bekerja dengan data besar.
 **Scikit-learn** | Library machine learning untuk Python.
 **Keras** | Framework high-level untuk membangun dan melatih model deep learning.
 **TensorFlow** | Library deep learning yang digunakan untuk membangun dan melatih model neural network.
 **Streamlit** | Framework untuk membuat antarmuka web aplikasi dengan cepat.

<a id="team"></a><h2>Team</h2>
**Muhammad Dafha Syahrizal**
**Akbar Fadillah Irsyad**
**Quenna Aurora Batubara**

