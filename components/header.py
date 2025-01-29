import streamlit as st

def render_header():
    st.markdown("""
        <div class="enterprise-header">
            <div class="logo-container">🏭</div>
            <div class="header-title">AI Warehouse Manager</div>
            <div class="header-subtitle">AI Powered Warehouse Analysis System</div>
        </div>
    """, unsafe_allow_html=True)