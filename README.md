# AI Fluency Training – Day 1 Practice & Evidence

## Student Information

**Name:** M D GOKULA HARINI  
**Roll Number:** 7376241CS187  
**Training:** AI Fluency Training  
**Day:** Day 1  
**Topic:** From LLMs to Agents  
**Project Type:** Training, Practice and Learning Evidence  
**Programming Language:** Python  
**Development Environment:** Visual Studio Code  
**Repository Purpose:** Practice, experimentation and documentation of Day 1 concepts

---

# 1. About This Repository

This repository contains my **Day 1 AI Fluency Training practice work and learning evidence**.

The purpose of this repository is to understand the difference between:

1. A Plain LLM Chatbot
2. A Rule-Based Workflow
3. A Tool-Using AI Agent

The same set of questions was used to understand how these three approaches behave differently.

This repository contains the Python source code, configuration files, tool implementations, challenge solution, and screenshots of the outputs obtained during the practice session.

This is an **educational and practice project** created as part of AI Fluency Training. It is not intended to be a production-ready application.

---

# 2. Day 1 Learning Objective

The main objective of Day 1 was to understand the progression from a basic Large Language Model to an AI Agent.

The practical exercise demonstrates three different approaches to solving the same type of problem:

### System 1 – Plain LLM Chatbot

A basic chatbot sends the user's question directly to the LLM.

It does not have access to the private course-fee data through tools.

---

### System 2 – Rule-Based Workflow

A rule-based program uses predefined conditions such as:

- `if`
- `elif`
- string matching
- predefined calculations

It does not depend on an LLM for decision-making.

---

### System 3 – Tool-Using AI Agent

An AI agent uses an LLM together with tools.

The agent can decide when it needs information from a tool and when it needs a calculation.

The tools used in this project are:

- `get_course_fee`
- `calculator`

The agent follows a loop of:

**Question → LLM → Tool Selection → Tool Execution → Result → LLM → Final Answer**

---

# 3. Technologies Used

The following technologies were used for this practice project:

- Python 3.11+
- Visual Studio Code
- OpenAI Python SDK
- Hugging Face Inference Providers
- `python-dotenv`
- Hugging Face `openai/gpt-oss-20b`
- Git
- GitHub

---

# 4. Project Structure

The project contains the following files:

```text
AI-Fluency-Day1-Evidence/
│
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   └── output3.png
│
├── .gitignore
├── requirements.txt
├── config.py
├── check_setup.py
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
├── challenge.py
└── README.md
