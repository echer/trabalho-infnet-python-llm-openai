import streamlit as st
from agent import Agent

open_ai_key = "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"
agent = Agent(open_ai_key)

# Título do app
st.title("App de Auxílio em Aprendizagem")

# Campo de texto longo
texto = st.text_area("Digite sua pergunta aqui: ", height=200)

# Botão de ação
if st.button("Obter resposta"):
    # Processamento do texto (exemplo simples)
    resposta = agent.get_answer(texto)
    
    # Seção de saída
    st.subheader("Resposta:")
    st.write(resposta["learn_answer"])
