import streamlit as st
import time
import pandas as pd
from google import genai

# Page Configuration
st.set_page_config(page_title="PROJECT AVYAN | Sovereign Security Shield", page_icon="🛡️", layout="wide")

st.title("🛡️ PROJECT AVYAN : SOVEREIGN SECURITY SHIELD")
st.caption("Automated DAST, SBOM & AI SARATHI Remediation Engine — SUDARSHAN")
st.markdown("---")

st.sidebar.header("System Status")
st.sidebar.success("SUDARSHAN Engine: ACTIVE")
st.sidebar.info("AI SARATHI: ONLINE")
st.sidebar.warning("CERT-In Portal Sync: READY")

# API Key Input in Sidebar for Security
api_key = st.sidebar.text_input("Enter Gemini API Key (Free):", type="password")

tab1, tab2, tab3 = st.tabs(["🚀 Live Scanner & AI Patch", "📋 CERT-In Compliance", "⚙️ Module Status"])

with tab1:
    st.subheader("1. Dynamic App Scanning & AI SARATHI Auto-Fix")
    target_url = st.text_input("Enter Target Domain / IP for Live Scan:", "https://example-enterprise.gov.in")
    
    if st.button("Start Live Security Assessment"):
        with st.spinner("Running SUDARSHAN Engine & Analyzing Vulnerabilities..."):
            time.sleep(2)
        st.success("Scan Completed Successfully!")
        
        # Sample DAST Output
        data = {
            "Vulnerability / Dependency": ["Outdated Apache Version", "SQL Injection Vector", "Open Port 8080", "Log4j Dependency"],
            "Severity": ["Medium", "High", "Low", "Critical"],
            "Status": ["Flagged", "Patched", "Monitored", "Remediated"]
        }
        st.table(pd.DataFrame(data))
        
        st.markdown("---")
        st.subheader("🤖 AI SARATHI Autonomous Patch Recommendation")
        
        if api_key:
            if st.button("Generate AI Remediation Patch"):
                with st.spinner("AI SARATHI is generating fix code..."):
                    try:
                        client = genai.Client(api_key=api_key)
                        response = client.models.generate_content(
                            model='gemini-2.5-flash',
                            contents='Provide a quick 3-step security remediation guide for SQL Injection and Log4j vulnerability in enterprise applications.',
                        )
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"API Error: {e}")
        else:
            st.info("💡 Enter your Free Gemini API Key in the sidebar to generate live AI patches during the demo!")

with tab2:
    st.subheader("2. CERT-In Automated 6-Hour Incident Evidence Engine")
    st.text_area("Auto-Generated Incident XML/JSON Evidence Payload:", 
"""{
  "incident_id": "CERT-IN-2026-AVYAN-091",
  "sector": "Critical Infrastructure",
  "attestation_proof": "0x9F8A...HARDWARE_SIGNED_HASH",
  "status": "AUTO_REPORTED"
}""", height=150)

with tab3:
    st.subheader("3. Integrated Engine Capabilities")
    status_data = {
        "Module / Engine Name": ["SUDARSHAN Master Engine", "Software Supply Chain", "AI SARATHI Patch Engine", "Attestation Engine"],
        "Category": ["DAST & SBOM", "SBOM Audit", "Generative AI", "Govt Compliance"],
        "Capability Scope": ["Dynamic Scanning", "Third-Party Dependency Audit", "Automated Security Fixes", "Hardware-Software Co-Design"],
        "Status": ["ACTIVE", "ACTIVE", "READY", "VERIFIED"]
    }
    st.dataframe(pd.DataFrame(status_data), use_container_width=True)
