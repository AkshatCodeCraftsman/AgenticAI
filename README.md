# AI Personal Finance Advisor

An AI-powered Personal Finance Advisor built with **Python**, **LangChain**, **Google Gemini**, and **yFinance**.

The project follows a modular multi-agent architecture where specialized agents collaborate to analyze a user's financial situation and generate personalized savings and investment recommendations.

## Features

- Natural language financial data extraction
- Planner agent for workflow orchestration
- Deterministic financial calculator
- Savings analysis agent
- Investment analysis agent
- Market agent for live market data retrieval
- Real-time market data using yFinance
- Report agent for consolidated responses
- Modular and extensible architecture

## Architecture

```text
User Query
    │
    ▼
Extractor
    │
    ▼
Planner
    │
    ├── Calculator
    ├── Market Agent
    ├── Savings Agent
    ├── Investment Agent
    └── Report Agent
```

## Project Structure

```text
Server/
│
├── agents/
├── core/
├── prompts/
├── services/
├── main.py
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Server
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

### 5. Run

```bash
python main.py
```

## Current Capabilities

- Personalized savings advice
- Personalized investment advice
- Financial data extraction from natural language
- Workflow planning through a Planner Agent
- Live stock market data retrieval using yFinance
- Multi-agent orchestration

## Future Enhancements

- Conversation memory
- Automatic stock screening
- Mutual fund analysis
- ETF analysis
- Portfolio tracking
- Goal-based financial planning
- CrewAI integration

## Tech Stack

- Python
- LangChain
- Google Gemini
- yFinance

## License

This project is intended for learning and educational purposes.
