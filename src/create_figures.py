"""
create_figures.py

Generate publication-ready workflow diagrams.
No experimental results are included.
"""

import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

FIGURES_DIR = "../figures"
os.makedirs(FIGURES_DIR, exist_ok=True)

COLORS = {
    "step": "#4C72B0",
    "model": "#DD8452",
    "output": "#55A868"
}

plt.rcParams.update({
    "font.size": 11,
    "font.family": "DejaVu Sans"
})


def draw_box(ax, x, y, w, h, text, color):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.03",
        linewidth=1.2,
        facecolor=color,
        edgecolor="black"
    )
    ax.add_patch(box)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        color="white",
        weight="bold"
    )


def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.5))


def training_workflow():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)

    draw_box(ax, 0.5, 1.5, 2.5, 1, "Load Dataset", COLORS["step"])
    draw_box(ax, 3.5, 1.5, 2.5, 1, "Train Model", COLORS["model"])
    draw_box(ax, 6.5, 1.5, 2.5, 1, "Cross Validation", COLORS["step"])
    draw_box(ax, 9.5, 1.5, 2.5, 1, "Store Parameters", COLORS["output"])

    arrow(ax, 3.0, 2.0, 3.5, 2.0)
    arrow(ax, 6.0, 2.0, 6.5, 2.0)
    arrow(ax, 9.0, 2.0, 9.5, 2.0)

    ax.set_title("Model Training Workflow", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(f"{FIGURES_DIR}/training_workflow.png", dpi=300)
    plt.close()


def evaluation_workflow():
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)

    draw_box(ax, 0.8, 1.5, 3, 1, "Trained Model", COLORS["model"])
    draw_box(ax, 4.2, 1.5, 3, 1, "Unseen Test Data", COLORS["step"])
    draw_box(ax, 7.6, 1.5, 3, 1, "Performance Metrics", COLORS["output"])

    arrow(ax, 3.8, 2.0, 4.2, 2.0)
    arrow(ax, 7.2, 2.0, 7.6, 2.0)

    ax.set_title("Model Evaluation Workflow", fontsize=14, weight="bold")
    plt.tight_layout()
    plt.savefig(f"{FIGURES_DIR}/evaluation_workflow.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    training_workflow()
    evaluation_workflow()
    print("High-quality figures generated successfully.")
