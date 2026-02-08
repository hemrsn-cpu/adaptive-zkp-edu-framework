import streamlit as st
import json
import time

# Attempt import logic
try:
    from main import AdaptiveVerifier
except ImportError:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from src.main import AdaptiveVerifier

# --- 1. Page Config (ตั้งค่าให้เป็นทางการสำหรับ RMU) ---
st.set_page_config(
    page_title="RMU Thesis: Adaptive ZKP Framework", # เปลี่ยนชื่อ Tab
    page_icon="🏛️", # เปลี่ยนไอคอนเป็นรูปสถาบัน
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. Custom CSS (ธีมสีม่วง-เหลือง หรือสีสุภาพ) ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    div.stButton > button:first-child {
        background-color: #5e2a85; /* สีม่วงราชภัฏ */
        color: white;
        border-radius: 8px;
        height: 50px;
        width: 100%;
        font-size: 18px;
    }
    .status-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Header (ส่วนหัวที่เป็นทางการ) ---
st.title("🏛️ Adaptive ZKP Credential Framework")
st.markdown("""
**Master of Science in Information and Communication Technology for Education** **Rajabhat Mahasarakham University (RMU)** *Developed by: Pannawat Chanwicha*
""")
st.markdown("---")

# --- 4. Sidebar (แผงควบคุม) ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    st.subheader("Select User Role")
    role = st.selectbox(
        "Who is verifying?",
        ("Employer (External Company)", "University Registrar (RMU)", "MoHE Auditor")
    )
    
    st.markdown("---")
    
    # Status Indicator
    if "Employer" in role:
        st.warning("🔒 **Privacy Mode: ON**\n(Zero-Knowledge Proof)")
    else:
        st.success("🔓 **Standard Mode: ON**\n(Full Transcript Access)")

# --- 5. Main Interface ---
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("🎓 Student Verification")
    st.info("System Simulation for Thesis Defense")
    
    student_id = st.text_input("Student ID:", value="STU-661440XXXX") # รหัส นศ. สมมติ
    gpa_threshold = st.slider("Minimum GPA Requirement:", 2.0, 4.0, 3.0)
    
    verify_btn = st.button("🔍 Verify Credential")

with col2:
    st.subheader("📊 Verification Result")
    
    if verify_btn:
        with st.spinner('Processing verification logic...'):
            time.sleep(1.5) 
            
            verifier = AdaptiveVerifier()
            role_key = "employer" if "Employer" in role else "university_admin"
            result = verifier.verify_degree_claim(student_id, gpa_threshold, role_key)
            
            if "error" in result:
                st.error(f"❌ Error: {result['error']}")
            else:
                if result.get('proof_valid') or result.get('actual_gpa', 0) >= gpa_threshold:
                    st.markdown(f"""
                    <div class="status-card" style="border-left: 5px solid green;">
                        <h2 style="color: green; margin:0;">✅ QUALIFIED / APPROVED</h2>
                        <p>Academic criteria met.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="status-card" style="border-left: 5px solid red;">
                        <h2 style="color: red; margin:0;">❌ NOT QUALIFIED</h2>
                        <p>Does not meet GPA requirements.</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.write("") 
                
                with st.expander("🔍 View Data Protocol (Thesis Evidence)", expanded=True):
                    if result.get('verification_mode') == 'Zero-Knowledge Proof':
                        st.info("🛡️ **PDPA Compliance Mode (ZKP)**")
                        st.write(f"**Outcome:** {result['message']}")
                        st.caption("Note: Sensitive data (GPA) remains hidden from the verifier.")
                    else:
                        st.warning("⚠️ **Administrative Mode (Full Access)**")
                        st.write(f"**GPA:** {result.get('actual_gpa')}")
                        st.json(result)

    else:
        st.markdown(
            """
            <div style="text-align: center; padding: 50px; color: grey; border: 2px dashed #ccc; border-radius: 10px;">
                Ready for verification simulation.
            </div>
            """, unsafe_allow_html=True
        )

# --- 6. Footer ---
st.markdown("---")
st.caption("© 2026 Faculty of Science and Technology, Rajabhat Mahasarakham University.")
