# Python Pomodoro Timer Desktop App 🍅

A simple Pomodoro Timer desktop application built using Python and Tkinter.

This project was originally created as a Python script and later improved, debugged, and packaged into a Windows desktop application using PyInstaller.

## 📌 About the Project

This is a mini productivity app based on the Pomodoro technique. It helps users stay focused by dividing time into work sessions and break sessions.

The app includes work timers, short breaks, long breaks, animated GIF support, session tick marks, reset functionality, and a packaged Windows `.exe` version.

## 🛠️ Technologies Used

* Python
* Tkinter
* Pillow
* PyInstaller

## ✨ Features

* 25-minute work sessions
* 5-minute short breaks
* 20-minute long breaks
* Animated GIFs for different timer modes
* Visual tick marks to track completed work sessions
* Reset button to restart the timer
* Packaged as a Windows desktop application

## 📂 Project Structure

```text
PythonPomodoroApp/
│
├── main.py
├── resized_peek_bear_300_proportional.gif
├── resized_cheer_bear_300_proportional.gif
├── resized_fan_bear_300_proportional.gif
├── resized_pomodoro_timer_300_proportional.gif
└── README.md
```

## 🚀 How to Run

Clone the repository:

```bash
git clone <your-repository-link>
```

Navigate to the project folder:

```bash
cd PythonPomodoroApp
```

Install the required packages:

```bash
pip install pillow
```

Run the application:

```bash
python main.py
```

## 📦 Desktop Application

This project was also packaged into a Windows desktop `.exe` application using PyInstaller.

Example PyInstaller command:

```bash
pyinstaller --onefile --windowed main.py
```

## 🎯 Learning Outcome

Through this project, I learned how to:

* Build a desktop GUI application using Tkinter
* Work with timers and countdown logic
* Add animated GIFs to a Python desktop app
* Improve and debug an existing Python script
* Package a Python project into a Windows executable using PyInstaller

## 📌 About

A minimal and simple Pomodoro timer desktop app made with Python.
