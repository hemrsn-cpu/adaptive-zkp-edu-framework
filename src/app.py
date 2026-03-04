import streamlit as st
import time
from main import AdaptiveVerifier

st.set_page_config(page_title="VeriProof: Adaptive Credential Engine", page_icon="🛡️", layout="wide")

st.markdown("<style>.main { background-color: #f8f9fa; } div.stButton > button:first-child { background-color: #1A5276; color: white; border-radius: 8px; height: 50px; width: 100%; font-size: 18px; font-weight: bold; }</style>", unsafe_allow_html=True)

st.title("🛡️ VeriProof: Adaptive Credential Engine")
st.markdown("**Advanced Privacy-Preserving Framework for Model Academic Institutions** *Developed by: Pannawat Chanvicha*")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Access Control")
    role = st.selectbox("Who is verifying?", ("External Verifier (Third-Party)", "Institutional Authority (Admin)"))
    if "External" in role:
        st.warning("🔒 **Privacy Mode: ENABLED** (ZKP)")
    else:
        st.success("🔓 **Administrative Mode: ENABLED**")

col1, col2 = st.columns([1, 1.5])
with col1:
    st.subheader("🎓 Subject Verification")
    student_id = st.text_input("Credential ID:", value="STU-001")
    threshold = st.slider("Required Threshold (GPA):", 2.0, 4.0, 3.0, step=0.1)
    if st.button("🔍 Execute Secure Verification"):
        with st.spinner('Calculating proofs...'):
            time.sleep(1.2)
            verifier = AdaptiveVerifier()
            role_key = "external_verifier" if "External" in role else "internal_authority"
            result = verifier.verify_credential(student_id, threshold, role_key)
            with col2:
                st.subheader("📊 Verification Metadata")
                if result.get("status") == "error": st.error(result["message"])
                else:
                    is_ok = result.get('is_qualified') or result.get('record')
                    st.success("VERIFIED") if is_ok else st.error("NOT QUALIFIED")
                    st.json(result)

st.markdown("---")
st.caption("© 2026 **Pannawat Chanvicha**. All rights reserved. | Proprietary Technology")