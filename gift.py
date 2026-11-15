
import tkinter as tk
import random
import math
from PIL import Image, ImageTk, ImageOps
from pathlib import Path

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("BASMA - Birthday Surprise")
root.geometry("600x700")
root.configure(bg="black")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=600,
    height=700,
    bg="black",
    highlightthickness=0
)
canvas.pack()

BASE_DIR = Path(__file__).resolve().parent

# =========================
# LOAD BASMA PHOTOS
# =========================

photo_folder = BASE_DIR / "picture"

photo_files = sorted(
    p for p in photo_folder.rglob("*")
    if p.suffix.lower() in [".jpg", ".jpeg", ".png"]
) if photo_folder.exists() else []

photos = []
heart_photos = []

for file in photo_files:
    try:
        img = Image.open(file).convert("RGBA")

        # Photos for slideshow
        display_img = img.copy()
        display_img.thumbnail((400, 420))
        photos.append(ImageTk.PhotoImage(display_img))

        # Small square photos for the heart
        heart_img = ImageOps.fit(img, (28, 28))
        heart_photos.append(ImageTk.PhotoImage(heart_img))

    except Exception as error:
        print("Photo error:", file, error)


# =========================
# MATRIX
# =========================

columns = []

for x in range(0, 600, 20):
    columns.append({
        "x": x,
        "y": random.randint(-700, 0),
        "speed": random.uniform(4, 8),
        "length": random.randint(5, 12)
    })

symbols = ["0", "1", "♡", "✦"]
matrix_active = True


def matrix():
    if not matrix_active:
        return

    canvas.delete("rain")

    for col in columns:
        x = col["x"]
        y = col["y"]

        for j in range(col["length"]):
            yy = y - j * 20

            if 0 <= yy <= 700:
                canvas.create_text(
                    x, yy,
                    text=random.choice(symbols),
                    fill=random.choice([
                        "#ff1493",
                        "#ff69b4",
                        "#c71585"
                    ]),
                    font=("Arial", 13),
                    tags="rain"
                )

        col["y"] += col["speed"]

        if col["y"] > 850:
            col["y"] = random.randint(-300, 0)

    root.after(25, matrix)


# =========================
# COUNTDOWN
# =========================

def countdown(number):

    canvas.delete("all")

    if number > 0:
        canvas.create_text(
            300, 330,
            text=str(number),
            fill="#ff69b4",
            font=("Arial", 120, "bold")
        )

        root.after(
            850,
            lambda: countdown(number - 1)
        )
    else:
        show_happy()


# =========================
# HAPPY
# =========================

def show_happy():
    canvas.delete("all")

    canvas.create_text(
        300, 330,
        text="HAPPY",
        fill="#ff69b4",
        font=("Arial", 65, "bold")
    )

    root.after(1300, show_birthday)


# =========================
# BIRTHDAY
# =========================

def show_birthday():
    canvas.delete("all")

    canvas.create_text(
        300, 330,
        text="BIRTHDAY",
        fill="#ff1493",
        font=("Arial", 53, "bold")
    )

    root.after(1300, show_to)


# =========================
# TO
# =========================

def show_to():
    canvas.delete("all")

    canvas.create_text(
        300, 330,
        text="TO",
        fill="#ff69b4",
        font=("Arial", 75, "bold")
    )

    root.after(1000, show_gift)


# =========================
# BASMA SCREEN
# =========================

def show_gift():
    global matrix_active
    matrix_active = False
    canvas.delete("rain")
    canvas.delete("all")
    canvas.configure(bg="black")

    for x in [220, 270, 320, 370]:
        canvas.create_rectangle(
            x, 180, x + 12, 260,
            fill="#ff69b4",
            outline="white"
        )

        canvas.create_oval(
            x + 2, 150, x + 10, 178,
            fill="#ffd700",
            outline="#ff9900"
        )

    canvas.create_text(
        300, 370,
        text="BASMA",
        fill="#ff1493",
        font=("Georgia", 75, "bold")
    )

    canvas.create_text(
        300, 460,
        text="Happy Birthday ❤️",
        fill="white",
        font=("Arial", 20, "italic")
    )

    root.after(1800, animate_bunny)


# =========================
# PURPLE BUNNY
# =========================

def animate_bunny(index=0):
    canvas.delete("all")
    canvas.configure(bg="#160b27")

    bounce = 15 if index % 2 == 0 else -15

    # Sparkles
    for i in range(25):
        x = random.randint(20, 580)
        y = random.randint(20, 620)

        canvas.create_text(
            x, y,
            text="✦",
            fill=random.choice([
                "#ff69b4",
                "#d8a0ff",
                "white"
            ]),
            font=("Arial", random.randint(10, 20))
        )

    # Ears
    canvas.create_oval(
        235, 150+bounce, 275, 280+bounce,
        fill="#c77dff",
        outline="#e8baff",
        width=3
    )

    canvas.create_oval(
        325, 150-bounce, 365, 280-bounce,
        fill="#c77dff",
        outline="#e8baff",
        width=3
    )

    # Inner ears
    canvas.create_oval(
        246, 170+bounce, 265, 260+bounce,
        fill="#ff69b4",
        outline=""
    )

    canvas.create_oval(
        336, 170-bounce, 355, 260-bounce,
        fill="#ff69b4",
        outline=""
    )

    # Head
    canvas.create_oval(
        220, 230+bounce, 380, 390+bounce,
        fill="#d8a0ff",
        outline="#f3d5ff",
        width=4
    )

    # Eyes
    for x in [260, 325]:
        canvas.create_oval(
            x, 290+bounce, x+15, 310+bounce,
            fill="#351044",
            outline=""
        )

    # Cheeks
    canvas.create_oval(
        240, 320+bounce, 270, 338+bounce,
        fill="#ff69b4",
        outline=""
    )

    canvas.create_oval(
        330, 320+bounce, 360, 338+bounce,
        fill="#ff69b4",
        outline=""
    )

    # Nose and smile
    canvas.create_oval(
        295, 320+bounce, 305, 330+bounce,
        fill="#ff69b4",
        outline=""
    )

    canvas.create_text(
        300, 345+bounce,
        text="ω",
        fill="#351044",
        font=("Arial", 20, "bold")
    )

    # Body
    canvas.create_oval(
        245, 365+bounce, 355, 510+bounce,
        fill="#b76bdf",
        outline="#e8baff",
        width=3
    )

    # Dancing arms
    if index % 2 == 0:
        arms = [(190, 350), (410, 350)]
    else:
        arms = [(190, 450), (410, 450)]

    canvas.create_line(
        250, 400+bounce,
        *arms[0],
        fill="#d8a0ff",
        width=18,
        capstyle=tk.ROUND
    )

    canvas.create_line(
        350, 400+bounce,
        *arms[1],
        fill="#d8a0ff",
        width=18,
        capstyle=tk.ROUND
    )

    # Heart
    canvas.create_text(
        300, 425+bounce,
        text="♥",
        fill="#ff69b4",
        font=("Arial", 35)
    )

    # Feet
    canvas.create_oval(
        225, 485+bounce, 285, 530+bounce,
        fill="#d8a0ff",
        outline="#e8baff",
        width=2
    )

    canvas.create_oval(
        315, 485+bounce, 375, 530+bounce,
        fill="#d8a0ff",
        outline="#e8baff",
        width=2
    )

    # Messages
    canvas.create_text(
        300, 590,
        text="Dance, Birthday Princess!",
        fill="#e8baff",
        font=("Georgia", 20, "italic")
    )

    canvas.create_text(
        300, 635,
        text="Happy Birthday BASMA 💜",
        fill="#ff69b4",
        font=("Arial", 17, "bold")
    )

    if index < 29:
        root.after(
            140,
            lambda: animate_bunny(index + 1)
        )
    else:
        show_photos()



# =========================
# HEART DRAWING WITH PHOTOS
# =========================

def show_photo_heart():
    canvas.delete("all")
    canvas.configure(bg="black")

    # Welcome text in the center
    canvas.create_text(
        300, 340,
        text="WELCOME 20",
        fill="#ff69b4",
        font=("Georgia", 32, "bold")
    )

    canvas.create_text(
        300, 385,
        text="HAPPY BIRTHDAY BASMA",
        fill="white",
        font=("Georgia", 13, "italic")
    )

    if not heart_photos:
        return

    points = []

    # Classic heart outline
    for t in range(0, 361, 3):
        angle = math.radians(t)

        x = 16 * math.sin(angle)**3

        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        )

        px = 300 + x * 12.5
        py = 350 - y * 12.5

        points.append((px, py))

    # Draw heart gradually with photos
    def draw_heart(i=0):

        if i >= len(points):
            canvas.create_text(
                300, 630,
                text="FOREVER FRIENDS ❤️",
                fill="#ff69b4",
                font=("Georgia", 21, "bold")
            )
            return

        x, y = points[i]

        photo = heart_photos[i % len(heart_photos)]

        canvas.create_image(
            x, y,
            image=photo
        )

        root.after(
            35,
            lambda: draw_heart(i + 1)
        )

    draw_heart()


    # Create a filled heart shape
    for y in range(-110, 111, 9):
        for x in range(-125, 126, 9):

            nx = x / 110
            ny = y / 110

            value = (
                (nx**2 + ny**2 - 1)**3
                - nx**2 * ny**3
            )

            if value <= 0:
                px = 300 + x * 1.35
                py = 345 - y * 1.35

                heart_points.append((px, py))

    def draw_step(i=0):

        if i >= len(heart_points):
            canvas.create_text(
                300, 650,
                text="FOREVER FRIENDS ❤️",
                fill="#ff69b4",
                font=("Georgia", 22, "bold")
            )
            return

        x, y = heart_points[i]

        photo = heart_photos[i % len(heart_photos)]

        canvas.create_image(
            x, y,
            image=photo
        )

        root.after(
            35,
            lambda: draw_step(i + 1)
        )

    draw_step()


# =========================
# BASMA PHOTOS
# =========================

def show_photos(index=0):
    canvas.delete("all")
    canvas.configure(bg="#160b27")

    if not photos:
        canvas.create_text(
            300, 300,
            text="No photos found!",
            fill="white",
            font=("Arial", 22, "bold")
        )

        canvas.create_text(
            300, 360,
            text="Put photos inside picture folder",
            fill="#ff69b4",
            font=("Arial", 15)
        )
        return

    canvas.create_text(
        300, 75,
        text="OUR BEAUTIFUL BASMA 💜",
        fill="#ff69b4",
        font=("Georgia", 25, "bold")
    )

    # Photo frame
    canvas.create_rectangle(
        85, 125, 515, 570,
        outline="#ff69b4",
        width=5
    )

    canvas.create_image(
        300, 345,
        image=photos[index]
    )

    canvas.create_text(
        300, 615,
        text="Happy Birthday Princess! 👑",
        fill="white",
        font=("Georgia", 19, "italic")
    )

    canvas.create_text(
        300, 660,
        text="Forever Friends ❤️",
        fill="#ff69b4",
        font=("Arial", 17, "bold")
    )

    if index < len(photos) - 1:
        root.after(
            1800,
            lambda: show_photos(index + 1)
        )
    else:
        root.after(1800, show_photo_heart)


# =========================
# START
# =========================

matrix()

root.after(
    6000,
    lambda: countdown(3)
)

root.mainloop()
