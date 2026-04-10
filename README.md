# ✈️ AI Travel Planner

Um assistente que gera roteiros de viagem personalizados com base no destino e na duração da viagem.

O projeto utiliza agentes de IA para organizar atividades de forma inteligente e automatizada.

---

## ✨ Tecnologias

- Python  
- Streamlit  

---

## 🚀 Funcionalidades

- Geração automática de roteiros de viagem  
- Validação de localização (cidade, estado ou país)  
- Interface web interativa com Streamlit  
- Interface via terminal (CLI)  
- Suporte a múltiplos idiomas (CLI)  

---

## 📍 Processo de Desenvolvimento

Este projeto foi criado para aprimorar minhas habilidades práticas na implementação de agentes de IA.

A ideia surgiu como inspiração em projetos pesquisados que poderiam facilitar o dia a dia de planejamento de viagens.

O projeto ainda está em fase inicial, contando com apenas um agente simples, mas já está estruturado para ser altamente escalável.

**Roadmap de Desenvolvimento:**

- [ ] Integração de Agente de Clima (previsão meteorológica local)  
- [ ] Integração de Agente Financeiro (conversão de moedas e estimativa de custos)  
- [ ] Exportação de roteiros para PDF

---

## 🚦 Rodando o Projeto

Siga os passos abaixo para executar o projeto localmente.

1. Gere uma chave de API do **Google Gemini**.
2. Clone este repositório.
3. Crie um ambiente virtual com `python -m venv venv`.
4. Ative o ambiente virtual (**Linux/macOS:** `source venv/bin/activate` | **Windows:** `venv\Scripts\activate`).
5. Instale as dependências do projeto com `pip install -r requirements.txt`.
6. Crie o arquivo `.env` e adicione sua chave de API `GEMINI_API_KEY=sua_chave_aqui`.
7. Execute a interface web com **Streamlit** usando `streamlit run app.py` e acesse `http://localhost:8501`.
8. Para executar a interface via terminal (**CLI**), rode `python main.py`.
