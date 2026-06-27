# ============================================================
#  Classification Model — Iris Flower Dataset
#  Skills: Data Handling · Supervised Learning · Model Training
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)

# ── STEP 1: Load & Understand the Dataset ───────────────────
print("=" * 55)
print("  STEP 1: Load & Understand the Dataset")
print("=" * 55)

iris = load_iris()

# Wrap in a DataFrame for easy exploration
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(f"\nDataset shape : {df.shape}  ({df.shape[0]} samples, {df.shape[1]} columns)")
print(f"Features      : {list(iris.feature_names)}")
print(f"Classes       : {list(iris.target_names)}")

print("\n── First 5 rows ──")
print(df.head().to_string(index=False))

print("\n── Class distribution ──")
print(df["species"].value_counts().to_string())

print("\n── Basic statistics ──")
print(df.describe().round(2).to_string())

# ── STEP 2: Prepare Features & Labels ───────────────────────
print("\n" + "=" * 55)
print("  STEP 2: Prepare Features & Labels")
print("=" * 55)

X = iris.data       # Feature matrix  (150 × 4)
y = iris.target     # Label vector    (150,)

print(f"\nFeature matrix X : shape {X.shape}")
print(f"Label vector   y : shape {y.shape}")
print(f"Unique labels    : {np.unique(y)}  → {list(iris.target_names)}")

# ── STEP 3: Split into Train & Test Sets ────────────────────
print("\n" + "=" * 55)
print("  STEP 3: Train / Test Split  (80 % train, 20 % test)")
print("=" * 55)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20 % for testing
    random_state=42,    # reproducibility
    stratify=y          # keep class balance in both splits
)

print(f"\nTraining set   : {X_train.shape[0]} samples")
print(f"Testing  set   : {X_test.shape[0]} samples")
print(f"Train class dist: {dict(zip(*np.unique(y_train, return_counts=True)))}")
print(f"Test  class dist: {dict(zip(*np.unique(y_test,  return_counts=True)))}")

# ── STEP 4: Feature Scaling ──────────────────────────────────
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)   # fit on train only
X_test  = scaler.transform(X_test)        # apply same scale to test

# ── STEP 5: Train & Evaluate Three Classifiers ──────────────
print("\n" + "=" * 55)
print("  STEP 4: Train & Evaluate Classifiers")
print("=" * 55)

models = {
    "K-Nearest Neighbors (k=3)" : KNeighborsClassifier(n_neighbors=3),
    "Decision Tree"              : DecisionTreeClassifier(random_state=42),
    "Logistic Regression"        : LogisticRegression(max_iter=200, random_state=42),
}

results = {}

for name, model in models.items():
    # ── Train ────────────────────────────────────────────────
    model.fit(X_train, y_train)

    # ── Predict ──────────────────────────────────────────────
    y_pred = model.predict(X_test)

    # ── Evaluate ─────────────────────────────────────────────
    acc = accuracy_score(y_test, y_pred)
    results[name] = {"model": model, "y_pred": y_pred, "accuracy": acc}

    print(f"\n{'─'*50}")
    print(f"  {name}")
    print(f"{'─'*50}")
    print(f"  Accuracy : {acc*100:.1f} %")
    print(f"\n  Classification Report:")
    report = classification_report(y_test, y_pred, target_names=iris.target_names)
    print("  " + report.replace("\n", "\n  "))

# ── STEP 6: Pick the Best Model ─────────────────────────────
best_name = max(results, key=lambda k: results[k]["accuracy"])
best      = results[best_name]

print("=" * 55)
print(f"  Best model → {best_name}")
print(f"  Accuracy   → {best['accuracy']*100:.1f} %")
print("=" * 55)

# ── STEP 7: Predict on New Samples ──────────────────────────
print("\n── Predict on 3 new flower samples ──")

new_flowers = np.array([
    [5.1, 3.5, 1.4, 0.2],   # likely setosa
    [6.0, 2.9, 4.5, 1.5],   # likely versicolor
    [6.5, 3.0, 5.5, 2.0],   # likely virginica
])

new_scaled    = scaler.transform(new_flowers)
predictions   = best["model"].predict(new_scaled)
probabilities = best["model"].predict_proba(new_scaled) \
                if hasattr(best["model"], "predict_proba") else None

for i, (flower, pred) in enumerate(zip(new_flowers, predictions)):
    label = iris.target_names[pred]
    prob  = f"  (confidence: {probabilities[i][pred]*100:.1f}%)" \
            if probabilities is not None else ""
    print(f"  Sample {i+1}: {flower}  →  {label}{prob}")

# ── STEP 8: Visualisations ───────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Classification Model — Iris Dataset", fontsize=14, fontweight="bold", y=1.01)

colors = ["#4e79a7", "#f28e2b", "#59a14f"]

# Chart 1 — Class Distribution
ax1 = axes[0]
counts   = df["species"].value_counts()
bars     = ax1.bar(counts.index, counts.values, color=colors, edgecolor="white", width=0.5)
ax1.set_title("Class Distribution", fontweight="bold")
ax1.set_ylabel("Count")
ax1.set_ylim(0, 65)
for bar in bars:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             str(int(bar.get_height())), ha="center", va="bottom", fontsize=10)
ax1.spines[["top","right"]].set_visible(False)

# Chart 2 — Model Accuracy Comparison
ax2    = axes[1]
names  = [n.split("(")[0].strip() for n in results.keys()]
accs   = [v["accuracy"]*100 for v in results.values()]
bars2  = ax2.bar(names, accs, color=["#a8c4e0","#fdc086","#b3de69"], edgecolor="white", width=0.5)
ax2.set_title("Model Accuracy Comparison", fontweight="bold")
ax2.set_ylabel("Accuracy (%)")
ax2.set_ylim(85, 102)
for bar, acc in zip(bars2, accs):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f"{acc:.1f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax2.tick_params(axis="x", labelsize=8)
ax2.spines[["top","right"]].set_visible(False)

# Chart 3 — Confusion Matrix of best model
ax3 = axes[2]
cm  = confusion_matrix(y_test, best["y_pred"])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot(ax=ax3, colorbar=False, cmap="Blues")
ax3.set_title(f"Confusion Matrix\n({best_name.split('(')[0].strip()})", fontweight="bold")
ax3.tick_params(axis="x", labelsize=8)
ax3.tick_params(axis="y", labelsize=8)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/classification_results.png", dpi=150, bbox_inches="tight")
print("\n✅ Chart saved → classification_results.png")

# ── Summary ──────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  PIPELINE SUMMARY")
print("=" * 55)
steps = [
    ("1", "Loaded Iris dataset",          "150 samples · 4 features · 3 classes"),
    ("2", "Explored & understood data",   "Shape, distribution, statistics"),
    ("3", "Split data 80/20",             "120 train · 30 test (stratified)"),
    ("4", "Scaled features",              "StandardScaler (zero mean, unit variance)"),
    ("5", "Trained 3 classifiers",        "KNN · Decision Tree · Logistic Regression"),
    ("6", "Evaluated on test set",        "Accuracy, precision, recall, F1"),
    ("7", "Predicted new samples",        "3 unseen flower measurements"),
]
for num, step, detail in steps:
    print(f"  Step {num}: {step:<35} {detail}")
print("=" * 55)
