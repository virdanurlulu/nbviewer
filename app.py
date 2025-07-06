import streamlit as st
import math

def hitung_radius_alonso(mass, Hc, eta, Z):
    E = eta * mass * Hc
    W_tnt = E / 4184
    R = Z * W_tnt ** (1/3)
    return R

st.title("Simulasi Radius Ledakan (Metode Alonso)")
mass = st.number_input("Massa bahan bakar (kg)", value=100.0)
Hc = st.number_input("Kalor pembakaran (kJ/kg)", value=46400.0)
eta = st.number_input("Efisiensi pembakaran", value=0.05)
Z = st.number_input("Scaled distance (Z)", value=6.5)

if st.button("Hitung Radius"):
    radius = hitung_radius_alonso(mass, Hc, eta, Z)
    st.success(f"Radius Bahaya: {radius:.2f} meter")
