import streamlit as st
from agents.travel_agent import plan_trip
from tools.location_validator import validate_location


st.title("Planejar roteiro de viagem")

destination = st.text_input("Qual o nome do local que deseja visitar")
duration = st.number_input("Quantos dias pretende ficar lá?", min_value=1, value=1, max_value=365, step=1)

if st.button("Enviar"):

    if not destination or not duration:
        st.warning("Por favor, preencha o destino e os dias da viagem.")
    
    else:
        local_info = validate_location(destination)

        if not local_info:
            st.error("Localização inválida. Por favor, insira um local válido.")

        else:
            try:
                with st.spinner("Planejando sua viagem..."):
                    result = plan_trip(destination, duration, idioma='pt')

                st.success("Roteiro gerado com sucesso!")
                st.write(result)

            except Exception as e:
                st.error("Ocorreu um erro ao gerar o roteiro.")
                st.exception(e)