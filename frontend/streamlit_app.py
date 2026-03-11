import streamlit as st
import requests

API_URL = "https://ai-agent.c-321a6c0.stage.kyma.ondemand.com/research"

st.set_page_config(page_title="AI Research Agent")

st.title(" AI Autonomous Research Agent")

query = st.text_input("Enter research topic")

if st.button("Run Research"):

    if query:

        with st.spinner("AI agents researching..."):

            response = requests.post(
                API_URL,
                json={"query": query}
            )

            result = response.json()

            st.subheader("Research Report")
            st.markdown(result["report"])

            st.subheader("Sources")

            st.write(result["report"])
            for url in result["sources"]:
                st.markdown(f"[{url}]({url})")