def merge_words(words, y_threshold=8):
    words = sorted(words, key=lambda w: (w["top"], w["x0"]))
    blocks = []

    for w in words:
        text = w["text"].strip().upper()
        if not text.isalpha() and len(text) < 3:
            continue

        if not blocks:
            blocks.append({**w, "text": text})
            continue

        prev = blocks[-1]

        if abs(w["top"] - prev["top"]) <= y_threshold:
            prev["text"] += " " + text
            prev["x1"] = max(prev["x1"], w["x1"])
            prev["bottom"] = max(prev["bottom"], w["bottom"])
        else:
            blocks.append({**w, "text": text})

    return blocks
