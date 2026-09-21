# AI Fluency Training – Day 1

## Student Information

**Roll Number:** 7376241CS187  
**Day:** Day 1  
**Topic:** From LLMs to Agents  
**Lab:** Chatbot vs Rule-Based Workflow vs AI Agent

---

# 1. Introduction

This repository contains the implementation and results for **Day 1 of the AI Fluency Training**.

The lab focuses on understanding the difference between:

- Plain LLM Chatbots
- Rule-Based Workflows
- AI Agents
- Tool Usage
- Tool-based problem solving

The same university course-fee questions were used to compare the different approaches.

---

# 2. Objectives

The main objectives of this lab are:

1. Set up Python development in VS Code.
2. Connect a Python application to an open LLM.
3. Implement a plain LLM chatbot.
4. Implement a rule-based workflow.
5. Implement tools for retrieving course fees and performing calculations.
6. Implement an AI agent that can use tools.
7. Compare the strengths and limitations of chatbots, workflows, and agents.
8. Understand why tools and external data are useful for reliable AI applications.

---

# 3. Technologies Used

- Python
- VS Code
- OpenAI Python SDK
- Python Dotenv
- Hugging Face Inference Providers
- Git
- GitHub

---

# 4. Project Structure

```text
day1_lab/
│
├── .gitignore
├── requirements.txt
├── config.py
├── check_setup.py
├── chatbot.py
├── workflow.py
├── tools.py
├── agent.py
└── challenge.py
File Description
File
Purpose
config.py
Stores configuration, model information, course-fee data, and test questions
check_setup.py
Checks whether the environment and required configuration are ready
chatbot.py
Implements a plain LLM chatbot
workflow.py
Implements a rule-based workflow
tools.py
Implements course-fee lookup and calculator tools
agent.py
Implements an AI agent that can use tools
challenge.py
Solves the course combination budget challenge
requirements.txt
Contains Python dependencies
.gitignore
Prevents sensitive and unnecessary files from being uploaded
5. Environment Setup
A Python virtual environment was created for the project.
The required packages are listed in:
requirements.txt
The project uses:
openai
python-dotenv
The setup was verified using:
python check_setup.py
Expected result:
SETUP OK
6. Security
The Hugging Face token is stored locally in a .env file.
The .env file is not uploaded to GitHub.
The virtual environment is also excluded from GitHub.
The .gitignore file contains:
.env
.venv/
__pycache__/
*.pyc
No API key or access token is stored in this repository.
7. Course Fee Data
The lab uses the following course-fee data:
Course
Fee
CS101
Rs. 12,000
AI202
Rs. 18,000
DS303
Rs. 15,000
This data is stored in config.py.
8. Test Questions
Four questions were used to compare the different implementations.
Question 1
What is the fee for AI202?
Expected result:
Rs. 18,000
Question 2
What is the total fee for CS101 and AI202 after a 10% scholarship?
Calculation:
CS101 + AI202
= 12,000 + 18,000
= 30,000

After 10% scholarship:
30,000 × 0.90
= 27,000
Expected result:
Rs. 27,000
Question 3
Is DS303 more expensive than CS101, and by how much?
Calculation:
15,000 - 12,000
= 3,000
Expected result:
Yes, DS303 is Rs. 3,000 more expensive than CS101.
Question 4
Write a two-line welcome message for new AI students.
This question does not require course-fee data or calculations.
9. Plain LLM Chatbot
File:
chatbot.py
The plain chatbot sends the user's question directly to the LLM.
It does not have access to the private course-fee data and does not have any tools.
Observed Results
Question 1
The model did not provide the correct course fee and indicated that it did not have the required information.
Question 2
The model asked for the relevant course fees instead of reliably calculating the answer from the private course data.
Question 3
The model produced an incorrect answer instead of using the actual course-fee data.
Question 4
The model successfully generated a suitable welcome message.
Observation
The plain LLM can generate natural-language responses, but it does not automatically have access to private application data.
This demonstrates why external data and tools may be required for reliable task-specific applications.
10. Rule-Based Workflow
File:
workflow.py
The workflow uses predefined Python conditions and the course-fee data.
It does not use an LLM.
Results
Question 1
The fee for AI202 is Rs. 18000.
Question 2
The total after a 10% scholarship is Rs. 27000.
Question 3
Yes. DS303 is Rs. 3000 more expensive than CS101.
Question 4
I don't have a rule for this question.
Observation
The rule-based workflow can produce reliable results for cases that have been explicitly programmed.
However, it depends on predefined rules and therefore does not provide the flexibility of a language model for general questions.
11. Tools
File:
tools.py
Two tools were implemented.
11.1 Course Fee Tool
Function:
get_course_fee()
Example:
get_course_fee("ai202")
Result:
18000
The function converts the course code to uppercase and checks whether it exists in the course-fee data.
11.2 Calculator Tool
Function:
calculator()
Example:
calculator("(12000 + 18000) * 0.9")
Result:
27000.0
Another example:
calculator("15000 - 12000")
Result:
3000
The calculator uses Python's AST-based expression parsing with a restricted set of arithmetic operators.
12. AI Agent
File:
agent.py
The AI agent combines:
An LLM
Course-fee lookup tool
Calculator tool
A system prompt
A tool-calling loop
The agent was instructed to follow these rules:
Never guess course fees.
Use get_course_fee whenever a course fee is required.
Use calculator for arithmetic.
Answer general questions without tools when tools are not needed.
Do not use tools unnecessarily.
Stop after a maximum number of steps.
13. Agent Testing
The agent initially successfully processed the first question and returned the AI202 fee.
However, subsequent testing encountered the following Hugging Face error:
Error code: 402
You have depleted your monthly included credits.
Because the Hugging Face Inference Provider credits were exhausted, the complete agent test could not be performed using the online inference service.
The agent.py implementation is retained in the repository for the lab demonstration.
This limitation was caused by the available inference credits and was not a Python syntax or project setup error.
14. Challenge
File:
challenge.py
The challenge was:
I can pay Rs. 30,000.
Which two courses can I take together within this budget?
The program checks every possible pair of courses and prints combinations whose total fee is within the budget.
Result
=== Day 1 Challenge ===
Budget: Rs. 30000
CS101 + AI202 = Rs. 30000
CS101 + DS303 = Rs. 27000
Therefore, the two combinations found within the Rs. 30,000 budget are:
CS101 + AI202 = Rs. 30,000
CS101 + DS303 = Rs. 27,000
15. Comparison
Feature
Plain LLM Chatbot
Rule-Based Workflow
AI Agent
Uses an LLM
Yes
No
Yes
Uses tools
No
No
Yes
Uses private course data
No
Yes
Yes, through tools
Performs calculations
Not reliably from private data
Yes
Yes, through calculator
Handles general language
Yes
Limited
Yes
Can decide when to use tools
No
No
Yes
Depends on predefined rules
No
Yes
Partially
External inference required
Yes
No
Yes
16. Key Observations
Plain LLM
A plain LLM can understand and generate natural language, but it may not know private or application-specific information.
Rule-Based Workflow
A rule-based workflow provides predictable results for explicitly programmed cases, but it is less flexible for unexpected questions.
AI Agent
An AI agent combines an LLM with tools. The LLM can decide when a tool is required and use the tool result to construct an answer.
Tools
Tools allow an AI system to interact with structured data and perform operations that should not be guessed by the model.
17. Learning Outcomes
After completing this lab, the following concepts were demonstrated:
Difference between an LLM chatbot and an AI agent
Difference between workflows and agents
Use of structured application data
Function/tool calling
Course-fee lookup using a tool
Arithmetic using a calculator tool
Basic agent orchestration
Environment configuration
API credential security
Git and GitHub project management
18. Conclusion
This Day 1 lab demonstrated the progression from a simple LLM chatbot to a rule-based workflow and a tool-using AI agent.
The plain chatbot was useful for natural-language generation but did not reliably access the private course-fee data.
The rule-based workflow reliably handled programmed fee-related operations but depended on predefined rules.
The AI agent was designed to combine an LLM with tools so that it could retrieve course fees and perform calculations when required. Complete online testing of the agent was limited by the Hugging Face inference-credit error encountered during the lab.
Overall, the lab provided practical experience with the basic components required to build tool-using AI systems.
