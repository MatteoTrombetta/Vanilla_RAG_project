# 🧠 Vanilla RAG (Retrieval-Augmented Generation) from Scratch

A purely educational project built to understand the inner workings of Generative AI and Retrieval-Augmented Generation systems from first principles. 

This project intentionally avoids high-level "black-box" frameworks like LangChain or LlamaIndex. Instead, it relies on standard Python libraries, linear algebra, and pure REST API calls to local AI models to build a complete RAG pipeline from the ground up.

## ⚠️ **Disclaimer**: 

Because this project adheres to a 100% local architecture, it relies on your machine's hardware to run both the embedding model and the Large Language Model (LLM) via Ollama. This could take minutes run.


### ⚙️ Architecture & Core Modules

The system is strictly divided into functional modules following the Single Responsibility Principle:

1. **`document_processor.py`**: Handles local file ingestion and implements a custom sliding-window algorithm for text chunking with overlap.
2. **`embedder.py`**: A custom REST client using the `requests` library to communicate with local embedding models and transform text chunks into high-dimensional vectors.
3. **`retriever.py`**: The mathematical core. Uses `numpy` and linear algebra to compute the **Cosine Similarity** between the user query vector and the knowledge base vectors.
4. **`generator.py`**: Manages prompt engineering, injecting retrieved context into strict prompt templates, and handling the generation via LLM.
5. **`Main.py`**: The entry point that orchestrates the entire pipeline (Ingestion -> Embedding -> Retrieval -> Generation).

### 🛠️ Prerequisites

* **Python 3.10+**
* **Ollama**: Must be installed and running locally to serve the models privately and for free.

#### Required Local Models
Before running the project, pull the necessary models via Ollama:

**Model for generating 768-dimensional vector embeddings**

```ollama pull nomic-embed-text```

**Model for final text generation**

```ollama pull llama3```


## 🚀 Setup and Installation
1. Clone the repository:

```git clone [https://github.com/MatteoTrombetta/vanilla-rag-project.git](https://github.com/MatteoTrombetta/vanilla-rag-project.git) ```

```cd vanilla-rag-project```

2. Create and activate a virtual environment:

```python -m venv .venv```

**On Windows**:

```.\.venv\Scripts\activate```

**On macOS/Linux**:

```source .venv/bin/activate```

3. Install Depedencies:

```pip install -r requirements.txt```

4. Add your documents:

Place your raw .txt files inside the src/docs/ directory.

5. Run the pipelines

```python Main.py```


# 🗺️ Roadmap & Future Improvements
While this project successfully proves the concept of a Vanilla RAG, transitioning it to an Enterprise-grade system requires a few architectural upgrades. Here are the planned future improvements:
* [ ] **Semantic Chunking**: Replace the current "N-character" brute-force chunking with NLP libraries like nltk or spaCy to dynamically split text at the end of sentences or paragraphs, preserving better semantic meaning.

* [ ] **Integration of a real Vector Database**: As the document base grows, iterating over an in-memory Python list becomes inefficient. Future iterations will replace the custom Retriever list with a lightweight, optimized vector database like ChromaDB or Qdrant.

* [ ] **Advanced Document Parsers**: Expand the DocumentProcessor to handle real-world messy data formats (e.g., PDFs, HTML, tabular data) using libraries like PyPDF2 or BeautifulSoup.

* [ ] **Evaluation Metrics**: Implement an automated testing framework using tools like RAGAS or TruLens to mathematically evaluate the quality of the retrieved context and the accuracy of the generated answers, preventing silent regressions.

