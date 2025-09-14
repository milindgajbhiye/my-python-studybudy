import tkinter as tk
from tkinter import messagebox
import random
import threading
import time

# ----------------- Main Window -----------------
root = tk.Tk()
root.title("🌟 Virtual Study Buddy 🌟")
root.geometry("420x500")
root.configure(bg="#f0f8ff")  # Light blue background

# ----------------- Welcome Label -----------------
label = tk.Label(
    root,
    text="Welcome to Study Buddy! 📚",
    font=("Comic Sans MS", 18, "bold"),
    fg="#ff4500",      # Orange text
    bg="#f0f8ff"
)
label.pack(pady=20)

# ----------------- Reminder Button -----------------
def study_reminder():
    messagebox.showinfo("Reminder", "⏰ Time to study! 💪")

reminder_button = tk.Button(
    root,
    text="📝 Get Reminder",
    command=study_reminder,
    font=("Arial", 14),
    fg="white",
    bg="#32cd32",  # Lime green
    width=20,
    height=2
)
reminder_button.pack(pady=10)

# ----------------- Motivation Button -----------------
quotes = [
    "✨ You can do it! ✨",
    "💡 Keep going, success is near!",
    "🔥 Never give up on your dreams!",
    "🌱 Small steps lead to big success!"
]

def show_motivation():
    messagebox.showinfo("Motivation", random.choice(quotes))

motivation_button = tk.Button(
    root,
    text="💡 Get Motivation",
    command=show_motivation,
    font=("Arial", 14),
    fg="white",
    bg="#1e90ff",  # Dodger blue
    width=20,
    height=2
)
motivation_button.pack(pady=10)

# ----------------- Study Tips -----------------
tips = [
    "📖 Break study sessions into chunks (25-30 minutes).",
    "🧘 Take short breaks to refresh your brain.",
    "📱 Keep your phone away while studying.",
    "💧 Drink water and stay hydrated!",
    "✅ Revise after finishing each chapter."
]

def show_tip():
    messagebox.showinfo("Study Tip", random.choice(tips))

tip_button = tk.Button(
    root,
    text="📖 Get Study Tip",
    command=show_tip,
    font=("Arial", 14),
    fg="white",
    bg="#ff69b4",  # Hot pink
    width=20,
    height=2
)
tip_button.pack(pady=10)

# ----------------- Timer Feature -----------------
timer_label = tk.Label(
    root,
    text="⏳ Timer: Not started",
    font=("Arial", 14, "bold"),
    fg="#800080",  # Purple
    bg="#f0f8ff"
)
timer_label.pack(pady=20)

session_count = 0  # Track study sessions

def start_timer():
    def countdown(seconds):
        global session_count
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_label.config(text=f"⏳ Timer: {mins:02d}:{secs:02d}")
            time.sleep(1)
            seconds -= 1
        session_count += 1
        timer_label.config(text="✅ Session Complete!")
        messagebox.showinfo("Great Job!", f"🎉 You completed {session_count} study session(s)!")

    # Run timer in separate thread so UI doesn't freeze
    threading.Thread(target=countdown, args=(10800,), daemon=True).start()  # 10 seconds for demo

timer_button = tk.Button(
    root,
    text="▶️ Start 3 Hour Timer",
    command=start_timer,
    font=("Arial", 14),
    fg="white",
    bg="#ff8c00",  # Orange
    width=20,
    height=2
)
timer_button.pack(pady=10)

# ----------------- Footer Label -----------------
footer = tk.Label(
    root,
    text="✨ Stay Focused, Stay Awesome! ✨",
    font=("Arial", 12, "italic"),
    fg="white",
    bg="#222222",  # Dark footer
    pady=10
)
footer.pack(side="bottom", fill="x")

# ----------------- Run the App -----------------
root.mainloop()
