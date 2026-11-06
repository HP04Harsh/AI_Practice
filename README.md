# Applied AI Engineer Study

Hands-on exercises and small projects documenting my journey toward becoming
an **Applied AI Engineer**. This repository includes Python fundamentals,
Bash scripting, and LangGraph examples, with room to grow into automation,
machine learning, generative AI, and deployment.

## Repository structure

```text
.
├── bash/       # Linux command-line and system-administration exercises
├── LangGraph/  # LangGraph examples using Groq
└── python/     # Python fundamentals and small programming exercises
```

## Python exercises

The [`python/`](python/) directory contains standalone examples covering:

- VAT calculations: [`check_vat.py`](python/check_vat.py)
- Iterating over paired lists: [`enumerate-food.py`](python/enumerate-food.py)
- The `nonlocal` keyword and nested functions: [`nonlocal_keyword.py`](python/nonlocal_keyword.py)
- A temperature loop: [`tea-heating.py`](python/tea-heating.py)
- Conditional temperature and device-state checks: [`themostat-alert.py`](python/themostat-alert.py)
- `match`/`case` selection for train seats: [`train-info.py`](python/train-info.py)
- Coupon discounts: [`user-discount.py`](python/user-discount.py)
- Banking inheritance practice: [`banking_inheritance.py`](python/banking_inheritance.py) and [`checking_account_inheritance.py`](python/checking_account_inheritance.py)

Run an exercise with Python 3:

```bash
python python/check_vat.py
```

`train-info.py` uses structural pattern matching and requires Python 3.10 or
newer. Some exercises prompt for input; follow the prompts in the terminal.

## LangGraph examples

The [`LangGraph/`](LangGraph/) directory contains:

- [`chat.py`](LangGraph/chat.py): a simple graph with chatbot and weather nodes.
- [`ai_llm.py`](LangGraph/ai_llm.py): a LangGraph workflow that calls a Groq chat model.

### Setup and run

From the repository root, create and activate a virtual environment, then
install the project dependencies:

```powershell
cd LangGraph
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Create a `.env` file in `LangGraph/` and add your Groq API key:

```env
GROQ_API_KEY=your-groq-api-key
```

Run either example from the `LangGraph/` directory:

```powershell
python chat.py
python ai_llm.py
```

`ai_llm.py` sends a request to Groq and requires a valid API key. Keep the key
private; `.env` and `.venv/` are excluded from Git.

## Bash exercises

The [`bash/`](bash/) directory contains scripts for:

- Creating a timestamped archive backup: [`backupfile-script.sh`](bash/backupfile-script.sh)
- Renaming `.txt` files to `.md`: [`bulk-rename.sh`](bash/bulk-rename.sh)
- Checking root filesystem usage: [`disk-monitor.sh`](bash/disk-monitor.sh)
- Displaying a system health summary: [`healthdashboard.sh`](bash/healthdashboard.sh)
- Navigating a simple system-information menu: [`interactive-menu.sh`](bash/interactive-menu.sh)
- Checking whether a local system user exists: [`user-check.sh`](bash/user-check.sh)

Run a script from a Bash-compatible environment:

```bash
bash bash/disk-monitor.sh
```

These scripts are intended for Linux or a compatible environment such as WSL.
Some use system utilities or paths that may not be available on other
operating systems. Review a script before running it, especially when it
reads, modifies, or archives files.

## Learning goals

- Build practical programming and automation skills.
- Strengthen Linux, Bash, and Python fundamentals.
- Progress toward machine learning, generative AI, MLOps, and reliable AI
  application development.

The examples are learning exercises and are not intended as production-ready
tools.
