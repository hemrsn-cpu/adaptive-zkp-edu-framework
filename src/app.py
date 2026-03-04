import streamlit as st
import time
from main import AdaptiveVerifier

# --- 1. Page Config ---
st.set_page_config(page_title="VeriProof: Adaptive Credential Engine", page_icon="🛡️", layout="wide")

# --- 2. Custom CSS ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    div.stButton > button:first-child {
        background-color: #1A5276;
        color: white;
        border-radius: 8px;
        height: 50px;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. Header ---
st.title("🛡️ VeriProof: Adaptive Credential Engine")
st.markdown("**Advanced Privacy-Preserving Framework for Model Academic Institutions** *Developed by: Pannawat Chanvicha*")
st.markdown("---")

# --- 4. Sidebar ---
with st.sidebar:
    st.header("⚙️ Access Control")
    role = st.selectbox("Who is verifying?", ("External Verifier (Third-Party)", "Institutional Authority (Admin)"))
    if "External" in role:
        st.warning("🔒 **Privacy Mode: ENABLED** (ZKP)")
    else:
        st.success("🔓 **Administrative Mode: ENABLED**")

# --- 5. Main Interface ---
col1, col2 = st.columns([1, 1.5])

with col1:
    st.subheader("🎓 Subject Verification")
    student_id = st.text_input("Credential ID:", value="STU-001")
    gpa_threshold = st.slider("Required Threshold (GPA):", 2.0, 4.0, 3.0, step=0.1)
    verify_btn = st.button("🔍 Execute Secure Verification")

with col2:
    st.subheader("📊 Verification Metadata")
    if verify_btn:
        with st.spinner('Calculating cryptographic proofs...'):
            time.sleep(1.2)
            verifier = AdaptiveVerifier()
            role_key = "external_verifier" if "External" in role else "internal_authority"
            result = verifier.verify_credential(student_id, gpa_threshold, role_key)
            
            if result.get("status") == "error":
                st.error(f"❌ Error: {result['message']}")
            else:
                is_qualified = result.get('is_qualified') or result.get('record')
                if is_qualified:
                    st.success("VERIFIED")
                else:
                    st.error("NOT QUALIFIED")

                with st.expander("🔍 View Protocol Evidence", expanded=True):
                    if result.get('verification_mode') == 'Zero-Knowledge Proof (ZKP)':
                        st.info("🛡️ **Protocol: Zero-Knowledge Proof (ZKP)**")
                        st.write("Outcome: Eligibility confirmed without data exposure.")
                        st.caption("Note: Sensitive attributes are mathematically proven but not revealed.")
                    else:
                        st.warning("⚠️ **Protocol: Standard Audit (Full Access)**")
                        st.json(result)
    else:
        st.info("Ready for secure verification engine simulation.")

# --- 6. Footer ---
st.markdown("---")
st.caption("© 2026 **Pannawat Chanvicha**. All rights reserved. | Proprietary Technology")