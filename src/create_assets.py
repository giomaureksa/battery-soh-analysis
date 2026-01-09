"""
create_assets.py

Generate high-quality architectural and conceptual diagrams
for documentation and portfolio use.

Industry-grade visualization:
- Clean layout
- Consistent color palette
- Publication-ready (300 DPI)
"""

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ASSETS_DIR = "../assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ------------------ STYLE CONFIG ------------------ #
COLORS = {
    "input": "#4C72B0",      # blue
    "process": "#8172B2",    # purple
    "model": "#DD8452",      # orange
    "output": "#55A868"      # green
}

plt.rcParams.update({
    "font.size": 11,
    "font.family": "DejaVu Sans"
})


def draw_box(ax, x, y, w, h, text, color):
    box = FancyBboxPatch(
        (x, y),
        w, h,
        boxstyle="round,pad=0.03,rounding_size=0.04",
        linewidth=1.2,
        edgecolor="black",
        facecolor=color,
        alpha=0.95
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        color="white",
        weight="bold",
        wrap=True
    )


def arrow(ax, x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", lw=1.5)
    )


# ------------------ DIAGRAMS ------------------ #

def pipeline_overview():
    fig, ax = plt.subplots(figsize=(11, 4))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)

    draw_box(ax, 0.5, 1.5, 2.5, 1, "Raw Battery Data\n(External Dataset)", COLORS["input"])
    draw_box(ax, 3.5, 1.5, 2.5, 1, "Preprocessing\n& Cleaning", COLORS["process"])
    draw_box(ax, 6.5, 1.5, 2.5, 1, "Feature Engineering", COLORS["process"])
    draw_box(ax, 9.5, 1.5, 2.5, 1, "ML Model\nTraining", COLORS["model"])

    arrow(ax, 3.0, 2.0, 3.5, 2.0)
    arrow(ax, 6.0, 2.0, 6.5, 2.0)
    arrow(ax, 9.0, 2.0, 9.5, 2.0)

    ax.set_title("Project Pipeline Overview", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/pipeline_overview.png", dpi=300)
    plt.close()


def model_architecture():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.axis("off")
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 7)

    draw_box(ax, 1.5, 5.5, 3, 1, "Engineered Features", COLORS["input"])
    draw_box(ax, 1.5, 3.8, 3, 1, "Regression Model\n(Random Forest / XGBoost)", COLORS["model"])
    draw_box(ax, 1.5, 2.1, 3, 1, "State of Health (SoH)\nPrediction", COLORS["output"])

    arrow(ax, 3.0, 5.5, 3.0, 4.8)
    arrow(ax, 3.0, 3.8, 3.0, 3.1)

    ax.set_title("Model Architecture", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/model_architecture.png", dpi=300)
    plt.close()


def system_concept():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)

    draw_box(ax, 0.8, 1.5, 3.2, 1, "Battery System\n(Sensors & Measurements)", COLORS["input"])
    draw_box(ax, 5.8, 1.5, 3.2, 1, "Data-Driven\nHealth Estimation Model", COLORS["model"])

    arrow(ax, 4.0, 2.0, 5.8, 2.0)

    ax.set_title("System-Level Concept", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/system_concept.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    pipeline_overview()
    model_architecture()
    system_concept()
    print("High-quality assets generated successfully.")
