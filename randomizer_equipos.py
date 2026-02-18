import random
import streamlit as st
import os

st.set_page_config(page_title="HSR - Randomizer de Equipos", page_icon="⚔️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Raleway:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    background-color: #0a0a1a;
    color: #e8e0ff;
    font-family: 'Raleway', sans-serif;
}

.stApp {
    background: radial-gradient(ellipse at top, #1a0a2e 0%, #0a0a1a 60%);
}

h1 {
    font-family: 'Cinzel', serif;
    font-size: 2.4rem;
    text-align: center;
    background: linear-gradient(135deg, #c9a0ff, #7ee8fa, #c9a0ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.1em;
    margin-bottom: 0.2em;
}

.subtitulo {
    text-align: center;
    color: #8877aa;
    font-size: 0.95rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

.equipo-card {
    background: linear-gradient(135deg, rgba(120, 60, 220, 0.15), rgba(40, 20, 80, 0.4));
    border: 1px solid rgba(180, 130, 255, 0.25);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    backdrop-filter: blur(10px);
}

.equipo-titulo {
    font-family: 'Cinzel', serif;
    font-size: 1.1rem;
    color: #c9a0ff;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 1rem;
    border-bottom: 1px solid rgba(180, 130, 255, 0.2);
    padding-bottom: 0.5rem;
}

.personaje-tag {
    display: inline-block;
    background: rgba(100, 50, 180, 0.3);
    border: 1px solid rgba(180, 130, 255, 0.35);
    border-radius: 20px;
    padding: 0.4rem 1rem;
    margin: 0.3rem;
    font-size: 0.95rem;
    color: #e8e0ff;
    font-weight: 600;
}

.divider {
    text-align: center;
    color: #4a3a6a;
    font-size: 1.5rem;
    margin: 1rem 0;
}

.stButton > button {
    background: linear-gradient(135deg, #7b2fff, #4a0aaa);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 0.7rem 2.5rem;
    font-family: 'Cinzel', serif;
    font-size: 1rem;
    letter-spacing: 0.1em;
    width: 100%;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(120, 50, 255, 0.4);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #9b4fff, #6a2aee);
    box-shadow: 0 6px 28px rgba(120, 50, 255, 0.6);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

with open("personajes.txt", "r", encoding="utf-8") as f:
    personajes = [linea.strip() for linea in f if linea.strip()]

def random_teams(personajes):
    seleccionados = random.sample(personajes, 8)
    equipo1 = seleccionados[:4]
    equipo2 = seleccionados[4:]
    return equipo1, equipo2

st.markdown("<h1>⚔️ HSR Team Randomizer</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Honkai: Star Rail — Generador de Equipos</p>', unsafe_allow_html=True)

if st.button("✦ Generar Equipos Aleatorios ✦"):
    equipo1, equipo2 = random_teams(personajes)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="equipo-card">', unsafe_allow_html=True)
        st.markdown('<div class="equipo-titulo">⚡ Equipo 1</div>', unsafe_allow_html=True)
        for p in equipo1:
            st.markdown(f'<span class="personaje-tag">{p}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="equipo-card">', unsafe_allow_html=True)
        st.markdown('<div class="equipo-titulo">🌙 Equipo 2</div>', unsafe_allow_html=True)
        for p in equipo2:
            st.markdown(f'<span class="personaje-tag">{p}</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="divider">— VS —</div>', unsafe_allow_html=True)
