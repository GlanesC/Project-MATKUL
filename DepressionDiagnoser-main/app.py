# app.py
import streamlit as st
from deteksiDepresi import MentalHealthExpertSystem

def main():
    st.set_page_config(page_title="Sistem Pakar Kesehatan Mental Generasi Z", layout="wide")
    
    # Inisialisasi session state
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    
    # Initialize the expert system
    expert_system = MentalHealthExpertSystem()
    
    # Sidebar for navigation
    st.sidebar.title("Menu")
    page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Diagnosa Kesehatan Mental", "Tentang Sistem"])
    
    if page == "Beranda":
        show_homepage(expert_system)
    elif page == "Diagnosa Kesehatan Mental":
        show_diagnosis_page(expert_system)
    elif page == "Tentang Sistem":
        show_about_page()

def show_homepage(expert_system):
    """Display the homepage with introduction and user info form"""
    st.title("Sistem Pakar Deteksi Kondisi Kesehatan Mental Generasi Z")
    
    with st.form("user_info_form"):
        name = st.text_input("Nama Lengkap", key="name_input")
        age = st.number_input("Usia", min_value=10, max_value=30, step=1, key="age_input")
        gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan", "Lainnya"], key="gender_input")
        submitted = st.form_submit_button("Mulai Diagnosa")
        
        if submitted:
            if not name:
                st.warning("Harap masukkan nama Anda")
            else:
                st.session_state.user_data = {
                    'name': name,
                    'age': age,
                    'gender': gender
                }
                st.success("Informasi tersimpan! Silakan pilih 'Diagnosa' dari menu sebelah.")

def show_diagnosis_page(expert_system):
    """Display the diagnosis questionnaire and results"""
    # Periksa dengan key yang benar ('user_data' bukan 'user_info')
    if 'user_data' not in st.session_state or st.session_state.user_data is None:
        st.warning("Silakan lengkapi informasi pengguna di halaman Beranda terlebih dahulu.")
        return
    
    st.title("Diagnosa Kesehatan Mental")
    # Gunakan 'user_data' bukan 'user_info'
    st.write(f"Halo, {st.session_state['user_data']['name']}! Silakan jawab pertanyaan berikut sesuai dengan kondisi Anda.")
    # Get all symptoms from the expert system
    symptoms = expert_system.get_all_symptoms()
    
    # Initialize session state for responses if not exists
    if 'responses' not in st.session_state:
        st.session_state['responses'] = {}
    
    # Display symptoms in two columns for better layout
    col1, col2 = st.columns(2)
    
    for i, (code, description) in enumerate(symptoms.items()):
        # Alternate between columns
        if i % 2 == 0:
            with col1:
                response = st.radio(
                    description,
                    options=["Tidak Mengalami", "Kadang-Kadang", "Sering", "Selalu"],
                    key=code,
                    index=0 if code not in st.session_state['responses'] else st.session_state['responses'][code]
                )
                # Map response to weight (0-3)
                weight_map = {
                    "Tidak Mengalami": 0,
                    "Kadang-Kadang": 1,
                    "Sering": 2,
                    "Selalu": 3
                }
                st.session_state['responses'][code] = weight_map[response]
        else:
            with col2:
                response = st.radio(
                    description,
                    options=["Tidak Mengalami", "Kadang-Kadang", "Sering", "Selalu"],
                    key=code,
                    index=0 if code not in st.session_state['responses'] else st.session_state['responses'][code]
                )
                weight_map = {
                    "Tidak Mengalami": 0,
                    "Kadang-Kadang": 1,
                    "Sering": 2,
                    "Selalu": 3
                }
                st.session_state['responses'][code] = weight_map[response]
    
    # Submit button
    if st.button("Submit Diagnosa"):
        # Perform backward chaining with the expert system
        results = expert_system.backward_chaining(st.session_state['responses'])
        
        # Display results
        st.subheader("Hasil Diagnosa")
        st.write(f"Berikut adalah hasil diagnosa untuk {st.session_state['user_data']['name']}:")
        
        # Show results for each condition
        for condition_code, result in results.items():
            with st.expander(f"{result['name']} - Tingkat {result['severity']}"):
                st.write(f"**Skor:** {result['score']}")
                st.write(f"**Rekomendasi:** {result['recommendation']}")
                
                # Show matched symptoms
                st.write("**Gejala yang dialami:**")
                for symptom_code in result['matched_symptoms']:
                    if st.session_state['responses'][symptom_code] > 0:  # Only show symptoms with positive responses
                        st.write(f"- {expert_system.get_symptom_description(symptom_code)} (Intensitas: {get_intensity_text(st.session_state['responses'][symptom_code])})")
        
        # Add some general advice
        st.subheader("Saran Umum")
        st.write("""
        - Hasil diagnosa ini bukan pengganti konsultasi dengan profesional kesehatan mental.
        - Jika Anda merasa membutuhkan bantuan, jangan ragu untuk menghubungi psikolog atau psikiater.
        - Jaga komunikasi dengan orang-orang terdekat dan ceritakan perasaan Anda.
        - Lakukan aktivitas fisik secara teratur dan jaga pola tidur yang baik.
        """)

def get_intensity_text(weight):
    """Convert weight to intensity text"""
    return {
        0: "Tidak Mengalami",
        1: "Kadang-Kadang",
        2: "Sering",
        3: "Selalu"
    }[weight]

def show_about_page():
    """Display information about the system"""
    st.title("Tentang Sistem Pakar Ini")
    
    st.write("""
    ### Sistem Pakar Deteksi Kondisi Kesehatan Mental pada Generasi Z
    
    Sistem ini dikembangkan menggunakan metode Backward Chaining untuk membantu Generasi Z 
    dalam memahami kondisi kesehatan mental mereka berdasarkan gejala yang dialami.
    
    ### Metode Backward Chaining
    Backward Chaining adalah metode penelusuran mundur yang dimulai dari kesimpulan (hipotesis) 
    dan mencari fakta-fakta yang mendukung kesimpulan tersebut. Dalam sistem ini, kami menentukan 
    terlebih dahulu kondisi kesehatan mental yang mungkin (Depresi, Kecemasan, Stres) kemudian 
    menelusuri gejala-gejala yang dialami pengguna untuk mendukung diagnosis tersebut.
    
    ### Tingkat Keparahan
    Sistem ini mengklasifikasikan kondisi kesehatan mental menjadi 4 tingkat:
    - Normal
    - Ringan
    - Sedang
    - Berat
    
    Klasifikasi didasarkan pada skor yang dihitung dari intensitas gejala yang dialami.
    
    ### Akurasi Sistem
    Berdasarkan pengujian dengan pakar, sistem ini memiliki akurasi sebesar 91.67%.
    
    ### Tim Pengembang
    - Riska Adi Istya
    - Ika Ratna Indra Astutik
    - Hindarto
    """)
    
    st.write("""
    ### Referensi
    Sistem ini dikembangkan berdasarkan penelitian yang dipublikasikan dalam:
    JIPI (Jurnal Ilmiah Penelitian dan Pembelajaran Informatika)
    Vol. 9, No. 1, Maret 2024
    """)

if __name__ == "__main__":
    main()