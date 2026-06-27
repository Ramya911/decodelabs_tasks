# ============================================================
#  Simple Recommendation System — Based on User Preferences
#  Skills: Logic Building · Pattern Matching · Recommendations
# ============================================================

import math

# ── STEP 1: Item Catalogue ───────────────────────────────────
# Each item is tagged with genre, mood, theme, and a rating.
# These tags are what we match against user preferences.

MOVIES = [
    {"id": 1,  "title": "Inception",            "genre": ["sci-fi","thriller"],        "mood": ["mind-bending","dark"],        "theme": ["dream","technology"],         "rating": 8.8},
    {"id": 2,  "title": "The Dark Knight",       "genre": ["action","thriller"],        "mood": ["dark","intense"],             "theme": ["justice","crime"],            "rating": 9.0},
    {"id": 3,  "title": "Interstellar",          "genre": ["sci-fi","drama"],           "mood": ["emotional","mind-bending"],   "theme": ["space","family","technology"],"rating": 8.6},
    {"id": 4,  "title": "The Notebook",          "genre": ["romance","drama"],          "mood": ["emotional","heartwarming"],   "theme": ["love","family"],              "rating": 7.9},
    {"id": 5,  "title": "Avengers: Endgame",     "genre": ["action","sci-fi"],          "mood": ["exciting","emotional"],       "theme": ["superhero","friendship"],     "rating": 8.4},
    {"id": 6,  "title": "The Grand Budapest Hotel","genre": ["comedy","drama"],          "mood": ["quirky","fun"],               "theme": ["mystery","friendship"],       "rating": 8.1},
    {"id": 7,  "title": "Get Out",               "genre": ["horror","thriller"],        "mood": ["dark","intense"],             "theme": ["mystery","social"],           "rating": 7.7},
    {"id": 8,  "title": "La La Land",            "genre": ["romance","musical"],        "mood": ["emotional","heartwarming"],   "theme": ["love","music","dreams"],      "rating": 8.0},
    {"id": 9,  "title": "Parasite",              "genre": ["thriller","drama"],         "mood": ["dark","mind-bending"],        "theme": ["social","crime"],             "rating": 8.6},
    {"id": 10, "title": "Toy Story",             "genre": ["animation","comedy"],       "mood": ["fun","heartwarming"],         "theme": ["friendship","family"],        "rating": 8.3},
    {"id": 11, "title": "The Martian",           "genre": ["sci-fi","drama"],           "mood": ["exciting","fun"],             "theme": ["space","technology"],         "rating": 8.0},
    {"id": 12, "title": "Crazy Rich Asians",     "genre": ["romance","comedy"],         "mood": ["fun","heartwarming"],         "theme": ["love","family"],              "rating": 7.3},
    {"id": 13, "title": "A Quiet Place",         "genre": ["horror","thriller"],        "mood": ["intense","dark"],             "theme": ["family","survival"],          "rating": 7.5},
    {"id": 14, "title": "The Shawshank Redemption","genre":["drama"],                   "mood": ["emotional","heartwarming"],   "theme": ["justice","friendship"],       "rating": 9.3},
    {"id": 15, "title": "Spirited Away",         "genre": ["animation","fantasy"],      "mood": ["mind-bending","heartwarming"],"theme": ["dreams","family"],           "rating": 8.6},
]

BOOKS = [
    {"id": 1,  "title": "Dune",                  "genre": ["sci-fi","fantasy"],         "mood": ["mind-bending","intense"],     "theme": ["technology","survival"],      "rating": 8.7},
    {"id": 2,  "title": "Atomic Habits",         "genre": ["self-help"],                "mood": ["motivating"],                 "theme": ["self-improvement"],           "rating": 8.5},
    {"id": 3,  "title": "The Alchemist",         "genre": ["fiction","fantasy"],        "mood": ["heartwarming","motivating"],  "theme": ["dreams","self-improvement"],  "rating": 8.4},
    {"id": 4,  "title": "Gone Girl",             "genre": ["thriller","mystery"],       "mood": ["dark","intense"],             "theme": ["crime","mystery"],            "rating": 8.1},
    {"id": 5,  "title": "Pride and Prejudice",   "genre": ["romance","classic"],        "mood": ["heartwarming","fun"],         "theme": ["love","social"],              "rating": 8.3},
    {"id": 6,  "title": "Sapiens",               "genre": ["non-fiction"],              "mood": ["mind-bending","motivating"],  "theme": ["social","technology"],        "rating": 8.9},
    {"id": 7,  "title": "The Hitchhiker's Guide","genre": ["sci-fi","comedy"],          "mood": ["fun","quirky"],               "theme": ["space","technology"],         "rating": 8.2},
    {"id": 8,  "title": "It",                    "genre": ["horror","thriller"],        "mood": ["dark","intense"],             "theme": ["friendship","survival"],      "rating": 8.0},
    {"id": 9,  "title": "The Great Gatsby",      "genre": ["classic","drama"],          "mood": ["emotional","dark"],           "theme": ["love","social"],              "rating": 7.9},
    {"id": 10, "title": "Harry Potter (Series)", "genre": ["fantasy","adventure"],      "mood": ["fun","exciting"],             "theme": ["friendship","magic"],         "rating": 9.0},
]

MUSIC = [
    {"id": 1,  "title": "Bohemian Rhapsody",     "genre": ["rock","classic"],           "mood": ["exciting","emotional"],       "theme": ["music","drama"],              "rating": 9.2},
    {"id": 2,  "title": "Blinding Lights",       "genre": ["pop","synth-pop"],          "mood": ["exciting","fun"],             "theme": ["love","music"],               "rating": 8.8},
    {"id": 3,  "title": "Someone Like You",      "genre": ["pop","soul"],               "mood": ["emotional","heartwarming"],   "theme": ["love"],                       "rating": 8.7},
    {"id": 4,  "title": "Lose Yourself",         "genre": ["hip-hop","rap"],            "mood": ["intense","motivating"],       "theme": ["dreams","self-improvement"],  "rating": 9.0},
    {"id": 5,  "title": "Hotel California",      "genre": ["rock","classic"],           "mood": ["mind-bending","dark"],        "theme": ["mystery","music"],            "rating": 9.1},
    {"id": 6,  "title": "Shape of You",          "genre": ["pop","dance"],              "mood": ["fun","exciting"],             "theme": ["love","music"],               "rating": 8.3},
    {"id": 7,  "title": "Billie Jean",           "genre": ["pop","r&b"],               "mood": ["exciting","fun"],             "theme": ["drama","music"],              "rating": 9.0},
    {"id": 8,  "title": "Numb",                  "genre": ["rock","metal"],             "mood": ["intense","dark"],             "theme": ["self-improvement","music"],   "rating": 8.8},
    {"id": 9,  "title": "Happier",               "genre": ["pop","indie"],              "mood": ["heartwarming","emotional"],   "theme": ["love","friendship"],          "rating": 8.2},
    {"id": 10, "title": "Stairway to Heaven",    "genre": ["rock","classic"],           "mood": ["mind-bending","emotional"],   "theme": ["music","dreams"],             "rating": 9.3},
]

CATALOGUES = {"movies": MOVIES, "books": BOOKS, "music": MUSIC}

# ── STEP 2: Cosine Similarity ────────────────────────────────
# Converts tag lists into binary vectors and computes similarity.
# cos(θ) = (A·B) / (|A| × |B|)  →  1.0 = perfect match

def build_vector(tags, all_tags):
    return [1 if t in tags else 0 for t in all_tags]

def cosine_similarity(vec_a, vec_b):
    dot   = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a * a for a in vec_a))
    mag_b = math.sqrt(sum(b * b for b in vec_b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)

# ── STEP 3: Recommendation Engine ───────────────────────────
def recommend(category, user_genres, user_moods, user_themes, top_n=5):
    """
    Scores every item in the catalogue using:
      • Cosine similarity on genre + mood + theme tags  (70 %)
      • Normalised item rating                           (30 %)
    Returns top_n items sorted by final score.
    """
    items = CATALOGUES[category]

    # Build a universal tag vocabulary for this catalogue
    all_genres = sorted({t for item in items for t in item["genre"]})
    all_moods  = sorted({t for item in items for t in item["mood"]})
    all_themes = sorted({t for item in items for t in item["theme"]})
    all_tags   = all_genres + all_moods + all_themes

    # User preference vector
    user_tags   = user_genres + user_moods + user_themes
    user_vector = build_vector(user_tags, all_tags)

    scores = []
    for item in items:
        item_tags   = item["genre"] + item["mood"] + item["theme"]
        item_vector = build_vector(item_tags, all_tags)

        sim          = cosine_similarity(user_vector, item_vector)
        norm_rating  = (item["rating"] - 7.0) / (9.5 - 7.0)   # scale to 0-1
        final_score  = 0.70 * sim + 0.30 * norm_rating

        scores.append({
            "title"      : item["title"],
            "genre"      : ", ".join(item["genre"]),
            "mood"       : ", ".join(item["mood"]),
            "rating"     : item["rating"],
            "similarity" : round(sim * 100, 1),
            "score"      : round(final_score * 100, 1),
        })

    scores.sort(key=lambda x: x["score"], reverse=True)
    return scores[:top_n]

# ── STEP 4: Display Helpers ──────────────────────────────────
def display_banner():
    print("\n" + "=" * 60)
    print("   🎯  SMART RECOMMENDATION SYSTEM")
    print("   Powered by Cosine Similarity + Preference Matching")
    print("=" * 60)

def choose_from_list(prompt, options):
    """
    Presents a numbered menu and lets the user pick
    one or more options (comma-separated). Returns a list.
    """
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        raw = input("  Enter numbers (e.g. 1,3): ").strip()
        try:
            indices = [int(x.strip()) - 1 for x in raw.split(",") if x.strip()]
            chosen  = [options[i] for i in indices if 0 <= i < len(options)]
            if chosen:
                return chosen
            print("  ⚠  Please pick at least one valid option.")
        except (ValueError, IndexError):
            print("  ⚠  Invalid input. Use numbers separated by commas.")

def display_recommendations(recs, category):
    print(f"\n{'─'*60}")
    print(f"  🏆  Top {len(recs)} {category.upper()} Recommendations For You")
    print(f"{'─'*60}")
    medals = ["🥇","🥈","🥉","4️⃣ ","5️⃣ "]
    for i, item in enumerate(recs):
        bar_filled = int(item["similarity"] / 10)
        bar = "█" * bar_filled + "░" * (10 - bar_filled)
        print(f"\n  {medals[i]}  {item['title']}")
        print(f"      Genre      : {item['genre']}")
        print(f"      Mood       : {item['mood']}")
        print(f"      Rating     : {item['rating']} / 10")
        print(f"      Match      : [{bar}] {item['similarity']}%")
        print(f"      Score      : {item['score']} / 100")
    print(f"\n{'─'*60}")

# ── STEP 5: Tag Menus ────────────────────────────────────────
GENRE_OPTIONS = {
    "movies": ["action","sci-fi","thriller","romance","drama",
               "comedy","horror","animation","fantasy","musical"],
    "books" : ["sci-fi","fantasy","thriller","romance","drama",
               "comedy","horror","non-fiction","self-help","classic"],
    "music" : ["pop","rock","hip-hop","r&b","soul",
               "jazz","classical","indie","metal","dance"],
}

MOOD_OPTIONS = ["fun","exciting","emotional","dark","heartwarming",
                "mind-bending","intense","motivating","quirky","romantic"]

THEME_OPTIONS = ["love","friendship","family","technology","space",
                 "crime","mystery","survival","dreams","self-improvement",
                 "social","music","superhero","justice","drama"]

# ── STEP 6: Main Interactive Loop ───────────────────────────
def main():
    display_banner()
    print("""
  How it works:
    1. Choose a category (movies / books / music)
    2. Tell us your genre, mood, and theme preferences
    3. We compute cosine similarity between your taste
       and every item in the catalogue
    4. Top matches are displayed with scores
    """)

    while True:
        # ── Category selection ────────────────────────────────
        print("\n  What would you like recommendations for?")
        print("  1. Movies  2. Books  3. Music  4. Quit")
        cat_choice = input("  Enter 1–4: ").strip()

        if cat_choice == "4":
            print("\n  👋  Thanks for using the Recommendation System!\n")
            break
        if cat_choice not in ("1","2","3"):
            print("  ⚠  Please enter 1, 2, 3, or 4.")
            continue

        category = {"1":"movies","2":"books","3":"music"}[cat_choice]

        # ── Preference gathering ──────────────────────────────
        print(f"\n  ── Tell us your {category} preferences ──")
        user_genres = choose_from_list(
            f"Pick your favourite genres:",
            GENRE_OPTIONS[category]
        )
        user_moods  = choose_from_list(
            "What mood are you in?",
            MOOD_OPTIONS
        )
        user_themes = choose_from_list(
            "Which themes interest you?",
            THEME_OPTIONS
        )

        # ── Echo user preferences ─────────────────────────────
        print(f"\n  ✅  Your preferences captured:")
        print(f"      Genres : {', '.join(user_genres)}")
        print(f"      Moods  : {', '.join(user_moods)}")
        print(f"      Themes : {', '.join(user_themes)}")

        # ── Compute & display recommendations ─────────────────
        recs = recommend(category, user_genres, user_moods, user_themes, top_n=5)
        display_recommendations(recs, category)

        # ── Explanation of the top pick ───────────────────────
        top = recs[0]
        print(f"  💡  Why '{top['title']}'?")
        print(f"      It shares the most tag overlap with your")
        print(f"      selected genres, moods, and themes, and")
        print(f"      has a strong rating of {top['rating']}/10.")
        print(f"      Combined score: {top['score']}/100\n")

        again = input("  🔄  Get more recommendations? (y/n): ").strip().lower()
        if again != "y":
            print("\n  👋  Thanks for using the Recommendation System!\n")
            break

if __name__ == "__main__":
    main()
