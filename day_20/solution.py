# # For Mac
# from os import system
# names = ["Akash", "Alok", "Akhil", "Amvi", "Aarushi", "Abhigya",
#          "Anushri", "Aditi", "Arohi", "Akanksha", "Aashi", "Ananya"]
# for name in names:
#     system(f'say Shoutout to {name}')


# For window
import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")
names = ["Akash", "Alok", "Akhil","Atul", "Amvi", "Aarushi", "Abhigya",
        "Anushri", "Aditi", "Arohi", "Akanksha", "Aashi", "Ananya"]
for i in names:
    print("Shoutout to " +i)

for name in names:
    names = name.split()
    shoutout = f"shoutout to {name}"
    speaker.Speak(shoutout)

print("Shoutout to everyone")