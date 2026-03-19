# 🐾 PawPal+: Smart Pet Care Scheduler

PawPal+ is an intelligent pet care planning assistant designed to help busy owners manage their pets' daily routines. Built with a robust Python backend and a modern Streamlit interface, PawPal+ uses algorithmic logic to ensure critical pet needs are prioritized and scheduled without conflicts.

## 🌟 Key Features

- **Priority-Based Scheduling:** Automatically organizes your day by prioritizing 'High' importance tasks (like medication) over 'Medium' or 'Low' tasks (like playtime).
- **Real-Time Conflict Detection:** The system intelligently flags overlapping tasks, providing visual warnings if two activities are scheduled for the same time.
- **Multi-Pet Management:** Track independent schedules for multiple pets (dogs, cats, and more) under a single owner profile.
- **Interactive UI:** A clean, emoji-coded dashboard that allows for quick task entry and instant schedule generation.
- **Verified Reliability:** Core logic is backed by an automated `pytest` suite to ensure scheduling accuracy.

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- [Streamlit](https://streamlit.io/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Moubarak-01/ai110-module2show-pawpal-starter.git
   cd ai110-module2show-pawpal-starter
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser to the provided local URL (usually `http://localhost:8501`)
3. Add tasks with priorities and times, then generate your optimized schedule!

## 🧪 Testing
Run the test suite to verify core functionality:
```bash
pytest
```

## 📋 Project Structure
- `pawpal_system.py` - Core classes and scheduling logic
- `app.py` - Streamlit web interface
- `reflection.md` - Project reflection and design decisions
- `requirements.txt` - Python dependencies

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements!

## 📄 License
This project is open source. See individual files for license details.
