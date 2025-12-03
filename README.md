# **FluxLm (GPT-2 Architecture)**

## 📖 **Project Overview**

This project is a full, from-scratch implementation of a GPT-2–style Large Language Model. Inspired by **Sebastian Raschka’s *Build a Large Language Model (From Scratch)***, the goal is to deeply understand Transformer internals without relying on high-level libraries like Hugging Face `transformers`.

Instead of assembling prebuilt components, this project constructs the core mechanisms of a GPT-style model manually—layer by layer, tensor by tensor—mirroring the idea of **building a custom bicycle from raw materials** rather than assembling a kit.

---

## 🚀 **Technical Highlights**

This implementation targets the GPT-2 (124M) architecture and includes:

### 🔹 **Causal Multi-Head Self-Attention**

* Full manual implementation
* Includes autoregressive masking to prevent future-token leakage

### 🔹 **Transformer Decoder Blocks**

* Layer Normalization applied pre-attention and pre-MLP
* GELU activation for smooth non-linearity
* Residual connections throughout

### 🔹 **Learnable Positional Embeddings**

* Adds sequence-order information to token embeddings

### 🔹 **Custom Training Loop**

* Forward pass, loss computation, and backpropagation implemented in PyTorch
* Supports training and inference from scratch

### 🔹 **Byte Pair Encoding (BPE) Tokenizer**

* Efficient text tokenization using the `tiktoken` library
* Matches GPT-2 style tokenization behavior

---

## 📂 **Repository Structure**

| File                         | Description                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| **`LLM-from-Scratch.ipynb`** | **Main Notebook** — Full GPT-2 architecture, training loop, and inference. |
| `Vector embedding.ipynb`     | Exploration of vector embeddings, cosine similarity, and semantic space.   |
| `gpt_download3.py`           | Utility for downloading datasets and model weights.                        |
| `word2evc.py`                | Custom Word2Vec implementation and embedding experiments.                  |
| `the-verdict.txt`            | Sample dataset used for testing and inference.                             |

---

## 🛠️ **Technologies Used**

* **Python**
* **Jupyter Notebook**
* **PyTorch**
* **NumPy**
* **Tiktoken (BPE Tokenizer)**

Approximate repository composition:
**Python (39.3%)** · **Jupyter Notebook (60.7%)**

---

## ⚡ **Getting Started**

### 1. **Clone the Repository**

```bash
git clone https://github.com/CombatAFK378/LLM-From-Scratch.git
cd LLM-From-Scratch
```

### 2. **Install Dependencies**

```bash
pip install torch numpy jupyter
```

### 3. **Run the Main Notebook**

```bash
jupyter notebook
```

Open **`LLM-from-Scratch.ipynb`** to explore the model architecture step-by-step.

---

## 📄 **License**

This project is licensed under the **Apache-2.0 License**.


