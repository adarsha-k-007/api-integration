# GenAI API Integration Assignment

## Name: Adarsha K

---

## Assignment Overview

This Assignment demonstrates the integration of multiple Generative AI APIs using Python.
Each API is implemented in a separate file with a simple and clear structure.

The project also includes a menu-driven program that allows users to query multiple APIs from a single interface.

---

## APIs Implemented

*  Groq API
*  Hugging Face API
*  Cohere API
*  Ollama (Local Model)

---

## Project Structure

```
ai-api-integration/
│
├── groq_example.py
├── huggingface_example.py
├── cohere_example.py
├── ollama_example.py
├── multi_api_query.py
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── screenshots/
```

---

##  Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Add API Keys

Create a `.env` file in the project folder and add:

```
GROQ_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
COHERE_API_KEY=your_key_here
```

---

### 3. Run Individual Programs

Example:

```bash
python groq_example.py
```

You can similarly run:

* `huggingface_example.py`
* `cohere_example.py`
* `ollama_example.py`

---

### 4. Run Multi API Program (Bonus)

```bash
python multi_api_query.py
```

This allows selecting different APIs from a menu.

---

## Key Concepts Learned

* API integration using Python
* Handling environment variables using `.env`
* Error handling using `try-except`
* Working with different AI providers
* Difference between cloud APIs and local models
* Menu-driven program design

---

## Challenges Faced

* Hugging Face API endpoint changes and routing issues
* Model compatibility (text vs chat models)
* Cohere model deprecation and updates
* Ollama memory limitations on local system
* Handling different API request formats

---

## Conclusion

This Assignment helped in understanding how different AI APIs work and how to integrate them into Python applications.
It also improved problem-solving skills and debugging ability while working with real-world APIs.

---

## Screenshots

###  Groq Output

![Groq](ai_api_intg/screenshots/groq.png)

###  Hugging Face Output

![HuggingFace](ai_api_intg/screenshots/huggingface.png)

###  Cohere Output

![Cohere](ai_api_intg/screenshots/cohere.png)

###  Ollama Output

![Ollama](ai_api_intg/screenshots/ollama.png)

###  Multi API Menu

![Multi API](ai_api_intg/screenshots/multi_api.png)

---
