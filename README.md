# Research Tool

A small Streamlit app that asks a local Ollama model to write a short, plain-language report. You enter a profession and the topic you want explained. The app builds a fixed prompt and sends it to `llama3.2` through LangChain.

## What it does

`root/prompt_ui.py` is the app:

1. You type a profession and the kind of information you want.
2. The app wraps those inputs in a prompt that asks the model to act as someone with more than 10 years in that profession, stay professional, keep the summary easy for non-technical readers, use numbers where useful, and stay within a clear scope.
3. On **generate the Report**, it calls the model and shows the reply in the page.

`root/test_ollama.py` is a one-shot check that the same model answers a question from the terminal.

`root/tempreture.py` is empty.

## Requirements

- Python 3
- [Ollama](https://ollama.com/) running locally
- The `llama3.2` model pulled in Ollama

```powershell
ollama pull llama3.2
```

## Setup

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r root\requirements.txt
```

The UI only needs these packages from that file:

- `langchain`
- `langchain-ollama`
- `python-dotenv`
- `streamlit`

The requirements file also lists OpenAI, Anthropic, Google Gemini, and Hugging Face packages. The current scripts do not call those providers.

`load_dotenv()` runs at startup. The scripts do not read any specific environment variables. Ollama uses its local default endpoint.

## Run

Start the UI from the `root` folder so the script path matches:

```powershell
cd root
streamlit run .\prompt_ui.py
```

Streamlit opens a local page titled **Research Tool**. Fill in both fields and click **generate the Report**.

To check the model from the terminal:

```powershell
cd root
python .\test_ollama.py
```

A successful run prints a LangChain message whose content answers the question in the script.

## Project layout

```
ResearchToolWithAgent/
  README.md
  output.png
  root/
    prompt_ui.py      Streamlit research UI
    test_ollama.py    Terminal smoke test for llama3.2
    tempreture.py     Unused
    requirements.txt  Python dependencies
    howto.md          Short run note
```

## Notes

- The model name and temperature (`0`) are set in code, not in the UI.
- The model runs locally through Ollama. Quality of numbers and “researched” claims depends on `llama3.2`; the app does not fetch live sources.
- `output.png` is a screenshot of a generated report.
