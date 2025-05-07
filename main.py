import json
import os
from datetime import datetime

JOURNAL_FILE = "mood_journal.json"

EMOJI_MOODS = {
    "😊": "happy",
    "😔": "sad",
    "😐": "meh",
    "😡": "angry",
    "😴": "tired",
    "😰": "anxious",
    "🥰": "loved",
    "🤯": "overwhelmed",
    "✨": "grateful"
}

def load_journal():
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, "r") as f:
            return json.load(f)
    return []

def save_journal(entries):
    with open(JOURNAL_FILE, "w") as f:
        json.dump(entries, f, indent=2)

def show_mood_options():
    print("💬 How are you feeling today? Pick a vibe:")
    for emoji, label in EMOJI_MOODS.items():
        print(f" {emoji}  - {label}")
    print()

def log_mood():
    show_mood_options()
    emoji = input("Enter the emoji that matches your mood: ").strip()
    if emoji not in EMOJI_MOODS:
        print("⚠️  Hmm... that emoji isn’t in the list. Try again!")
        return

    note = input("Anything you want to add? (optional): ").strip()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "emoji": emoji,
        "mood": EMOJI_MOODS[emoji],
        "note": note
    }
    entries = load_journal()
    entries.append(entry)
    save_journal(entries)
    print(f"✅ Logged! {emoji} {EMOJI_MOODS[emoji].capitalize()} — you got this. 💪\n")

def show_journal():
    entries = load_journal()
    if not entries:
        print("📭 No moods yet. Let’s start today! 🌞\n")
        return
    print("\n📖 Your Mood Journal\n")
    for e in entries:
        print(f"{e['date']} | {e['emoji']} {e['mood'].capitalize()} | Note: {e['note'] or '—'}")
    print("\n💌 Thanks for checking in with yourself.\n")

def main():
    while True:
        print("🌸 Mood Journal 🌸")
        print("1. Log today’s mood")
        print("2. View mood journal")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            log_mood()
        elif choice == "2":
            show_journal()
        elif choice == "3":
            print("See you later, beautiful soul 🌈💫")
            break
        else:
            print("Oops! That wasn’t 1, 2, or 3. Try again 💕")

if __name__ == "__main__":
    main()
