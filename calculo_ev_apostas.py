
# Interface Web para calcular EV% e Stake Sugerido com Streamlit
import streamlit as st

def calcular_ev(odd_justa, odd_aposta, bankroll=1000, kelly_fracao=0.33):
    prob_justa = 1 / odd_justa
    ev_bruto = (odd_aposta * prob_justa) - 1
    stake_kelly = bankroll * ((ev_bruto / (odd_aposta - 1)) * kelly_fracao)

    return {
        "Odd Justa": odd_justa,
        "Odd da Aposta": odd_aposta,
        "Probabilidade Justa (%)": round(prob_justa * 100, 2),
        "EV (%)": round(ev_bruto * 100, 2),
        f"Stake Sugerido (Kelly {int(kelly_fracao * 100)}%)": round(stake_kelly, 2)
    }

# Interface com Streamlit
st.title("Calculadora de EV% e Stake - Apostas Desajustadas")

st.sidebar.header("Parâmetros da Aposta")
odd_justa = st.sidebar.number_input("Odd Justa (ex: Pinnacle)", min_value=1.01, value=1.50, step=0.01)
odd_aposta = st.sidebar.number_input("Odd da Casa de Aposta", min_value=1.01, value=2.00, step=0.01)
bankroll = st.sidebar.number_input("Bankroll Total", min_value=1.0, value=1000.0, step=10.0)
kelly_fracao = st.sidebar.slider("Fração de Kelly", min_value=0.05, max_value=1.0, value=0.33, step=0.01)

if st.sidebar.button("Calcular"):
    resultado = calcular_ev(odd_justa, odd_aposta, bankroll, kelly_fracao)
    st.subheader("Resultado")
    for chave, valor in resultado.items():
        st.write(f"**{chave}:** {valor}")

st.markdown("---")
st.markdown("Desenvolvido para análise de apostas com valor esperado positivo (EV+).")
