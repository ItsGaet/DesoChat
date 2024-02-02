# Install Chatbot

## 1. Install Ollama

```bash
curl https://ollama.ai/install.sh | sh
```

```bash
ollama pull stablelm2
```

```bash
ollama serve
```

>può dare errore, vuol dire solo che è gia esposto il modello

## 2. Clone della repo

```bash
git clone https://github.com/ItsGaet/DesoChat
```

```bash
cd DesoChat
```

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

## 4. Run the App

```bash
streamlit run app/app.py
```
