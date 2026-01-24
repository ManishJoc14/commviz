import streamlit as st
from modules.signals import run_signals_module

st.set_page_config(layout="wide", page_title="CS Viz", menu_items={})
st.sidebar.markdown("## Comm. Systems Visualizer")
st.sidebar.markdown("---")

signal_topic = st.sidebar.radio(
    "Signal Analysis",
    [
        "Signal Fundamentals",
        "Basic Signal Operations",
        "Energy and Power Signals",
        "Convolution",
    ],
    key="signal_analysis",
)

if signal_topic == "Signal Fundamentals":
    run_signals_module()
