FROM python:3.10

WORKDIR /app

COPY frontend/streamlit_app.py .

RUN pip install streamlit requests

EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]