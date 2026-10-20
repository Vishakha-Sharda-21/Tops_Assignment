"""Small custom dataset: 10 sample tweets (1 = positive, 0 = negative). Shared by tasks 2, 4, 5."""
DATA = [
    ("I love the new Instagram update, it is so smooth!", 1),
    ("Zomato delivered my food super fast today.", 1),
    ("What a fantastic match, India played brilliantly!", 1),
    ("Best biryani I have ever ordered, totally worth it.", 1),
    ("Amazing customer support, my problem was solved in minutes.", 1),
    ("The app keeps crashing, very frustrating experience.", 0),
    ("Food arrived cold and very late, never ordering again.", 0),
    ("Worst service ever, nobody replied to my complaint.", 0),
    ("Terrible update, the app is slow and full of bugs.", 0),
    ("I am so disappointed with this product, complete waste of money.", 0),
]
TEXTS = [t for t, _ in DATA]
LABELS = [l for _, l in DATA]
