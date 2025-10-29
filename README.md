# To-Do List App

A simple, interactive to-do list application built with [Reflex](https://reflex.dev/), a Python web framework for building full-stack applications.

If these scripts were useful to you, consider donating to support the Developer Service Blog: https://buy.stripe.com/bIYdTrggi5lZamkdQW

## Features

- ✅ Add new tasks to your to-do list
- ❌ Remove tasks with a single click
- ⚡ Real-time updates with reactive state management

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone this repository:

```bash
git clone <repository-url>
cd Reflex-Article
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the development server:

```bash
reflex run
```

Open your browser and navigate to `http://localhost:3000` (or the URL shown in the terminal).

## Project Structure

```
Reflex-Article/
├── my_todo_app/
│   ├── __init__.py
│   └── my_todo_app.py      # Main application code
├── rxconfig.py             # Reflex configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## How It Works

The application uses Reflex's reactive state management:

- **State Class**: Manages the list of todos and the current input value
- **add_todo()**: Adds a new task to the list when the input is not empty
- **remove_todo()**: Removes a task from the list by its index

The UI is defined using Reflex components that automatically update when the state changes.

## Configuration

The app is configured in `rxconfig.py` with:

- Tailwind CSS v4 for styling
- Sitemap plugin for SEO

## Dependencies

- `reflex` - The Reflex framework for building full-stack Python apps

## License

This project is open source and available for personal and educational use.
