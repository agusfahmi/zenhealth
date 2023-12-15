import streamlit as st

def term():
    st.header('Petunjuk Penggunaan')
    st.write("Chatbot Kesehatan ini dirancang untuk memberikan informasi dan saran kesehatan dasar dalam bahasa inggris.")
    st.write("Berikut adalah langkah-langkah penggunaan chatbot ini:")

    # Step 1
    st.subheader('1. Mulai Percakapan')
    st.write("Klik tombol 'Konsultasi' pada bagian kiri layar untuk memulai interaksi dengan chatbot.")
    # Step 2
    st.subheader('2. Pertanyaan dan Jawaban')
    st.write("Pengguna dapat mengajukan pertanyaan tentang kesehatan .")
    st.write("Berikan pertanyaan-pertanyaan tersebut sejelas mungkin.")

    # Step 3
    st.subheader('3. Hasil dan Saran')
    st.write("Setelah pertanyaan-pertanyaan selesai, chatbot akan memberikan hasil dan saran kesehatan.")
    st.write("Apabila terdapat jawaban yang kurang maksimal, bisa diberikan kata spesifik ")

    # Step 4
    st.subheader('4. Hapus History')
    st.write("Anda dapat menghapus riwayat chatbot dengan kil 'clear chat history' pada bagian kiri.")
    # Step 5
    st.subheader('5. Selesai')
    st.write("Jika Anda telah selesai menggunakan chatbot, bisa tutup tab.")
