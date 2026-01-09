"""
Visualization Module for Battery SOH Analysis
Comprehensive visualization functions matching notebook implementations
Author: Battery SOH Analysis Project
Date: January 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. CONFIGURATION (Matches Notebook 1, Section 1.2)
# ============================================================================

def configure_visualization():
    """
    Global plotting configuration - identical to notebook settings
    Returns: EDA_DIR, MODEL_DIR paths
    """
    # Exact match with notebook 1, cell [2]
    sns.set(style="whitegrid", context="talk")
    
    # Figure directories (same structure as notebooks)
    FIG_DIR = Path("../figures")
    EDA_DIR = FIG_DIR / "eda"
    MODEL_DIR = FIG_DIR / "modeling"
    
    # Create directories if they don't exist
    for directory in [EDA_DIR, MODEL_DIR]:
        directory.mkdir(parents=True, exist_ok=True)
    
    print("Figure directories configured")
    print(f"  EDA: {EDA_DIR}")
    print(f"  Modeling: {MODEL_DIR}")
    
    return EDA_DIR, MODEL_DIR


# ============================================================================
# 2. EDA VISUALIZATIONS (Notebook 1, Section 1.9)
# ============================================================================

def plot_soh_trend(soh_df, save_dir, colors=None):
    """
    Plot SOH trend with EOL threshold - Notebook 1, Section 1.9.1.1
    """
    if colors is None:
        colors = {'AC01': '#2E86AB', 'AC02': '#A23B72'}
    
    plt.figure(figsize=(7, 5))
    
    for cell_id in sorted(soh_df['cell_id'].unique()):
        cell_data = soh_df[soh_df['cell_id'] == cell_id].sort_values('checkup_num')
        plt.plot(
            cell_data['checkup_num'],
            cell_data['soh_percentage'],
            marker='o',
            linewidth=2,
            label=cell_id,
            color=colors.get(cell_id, 'gray')
        )
    
    # Add threshold lines
    plt.axhline(80, color='red', linestyle='--', label='80% EOL Threshold')
    plt.axhline(85, color='orange', linestyle='--', label='85% Warning Level')
    
    plt.title("State of Health (SOH) Trend")
    plt.xlabel("Checkup Number")
    plt.ylabel("SOH (%)")
    plt.legend(fontsize=10, loc='upper right')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = save_dir / "fig_1_soh_trend.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    print(f"  SOH trend saved: {output_path.name}")
    return output_path


def plot_capacity_fade(soh_df, save_dir, colors=None):
    """
    Plot capacity fade over time - Notebook 1, Section 1.9.1.2
    """
    if colors is None:
        colors = {'AC01': '#2E86AB', 'AC02': '#A23B72'}
    
    plt.figure(figsize=(7, 5))
    
    for cell_id in sorted(soh_df['cell_id'].unique()):
        cell_data = soh_df[soh_df['cell_id'] == cell_id].sort_values('checkup_num')
        plt.plot(
            cell_data['checkup_num'],
            cell_data['max_capacity_mah'],
            marker='s',
            linewidth=2,
            label=cell_id,
            color=colors.get(cell_id, 'gray')
        )
    
    plt.title("Capacity Fade Over Time")
    plt.xlabel("Checkup Number")
    plt.ylabel("Discharge Capacity (mAh)")
    plt.legend(fontsize=10, loc='upper right')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = save_dir / "fig_2_capacity_fade.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    print(f"  Capacity fade saved: {output_path.name}")
    return output_path


def plot_soh_distribution(soh_df, save_dir):
    """
    Plot SOH distribution - Notebook 1, Section 1.9.1.3
    """
    plt.figure(figsize=(7, 5))
    
    plt.hist(
        soh_df['soh_percentage'], 
        bins=15,
        edgecolor='black',
        alpha=0.7,
        color='steelblue'
    )
    
    mean_soh = soh_df['soh_percentage'].mean()
    plt.axvline(80, color='red', linestyle='--', label='80% EOL Threshold')
    plt.axvline(mean_soh, color='green', linestyle='--',
                label=f"Mean: {mean_soh:.1f}%")
    
    plt.title("SOH Distribution")
    plt.xlabel("SOH (%)")
    plt.ylabel("Frequency")
    plt.legend(fontsize=10, loc='upper left')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = save_dir / "fig_3_soh_distribution.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    print(f"  SOH distribution saved: {output_path.name}")
    return output_path


def plot_degradation_rate(soh_df, save_dir):
    """
    Plot degradation rate analysis - Notebook 1, Section 1.9.1.4
    Returns: degradation_data list
    """
    plt.figure(figsize=(7, 5))
    
    degradation_data = []
    
    for cell_id in sorted(soh_df['cell_id'].unique()):
        cell_data = soh_df[soh_df['cell_id'] == cell_id].sort_values('checkup_num')
        
        if len(cell_data) > 1:
            x = cell_data['checkup_num'].values
            y = cell_data['soh_percentage'].values
            
            # Linear regression
            slope, intercept = np.polyfit(x, y, 1)
            
            # Prediction line
            x_pred = np.linspace(x.min(), x.max() + 5, 50)
            y_pred = slope * x_pred + intercept
            
            # Plot
            plt.scatter(x, y, alpha=0.7, label=f"{cell_id} Data")
            plt.plot(
                x_pred,
                y_pred,
                '-',
                label=f"{cell_id}: {slope:.3f}% / checkup"
            )
            
            degradation_data.append({
                'cell': cell_id.upper(),
                'degradation_rate': slope,
                'initial_soh': y[0],
                'current_soh': y[-1],
                'intercept': intercept
            })
    
    # EOL threshold
    plt.axhline(80, color='red', linestyle='--', alpha=0.5)
    
    plt.title("Degradation Rate Analysis")
    plt.xlabel("Checkup Number")
    plt.ylabel("SOH (%)")
    plt.legend(fontsize=10, loc='upper right')
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = save_dir / "fig_4_degradation_rate.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()
    
    print(f"  Degradation rate saved: {output_path.name}")
    
    # Print degradation statistics (matching notebook output)
    if degradation_data:
        print("\n  Degradation Rates per Checkup:")
        for item in degradation_data:
            cell = item['cell']
            rate = item['degradation_rate']
            total_loss = item['initial_soh'] - item['current_soh']
            print(f"    {cell}:")
            print(f"      Degradation rate: {rate:.3f}% per checkup")
            print(f"      Total loss: {total_loss:.1f}%")
            if rate < 0:
                checkups_to_eol = (item['current_soh'] - 80) / abs(rate)
                print(f"      Projected checkups to 80%: {checkups_to_eol:.1f}")
    
    return degradation_data


# ============================================================================
# 3. MODELING VISUALIZATIONS (Notebook 3, Section 3.3.2)
# ============================================================================

def plot_predicted_vs_actual(model_df, save_dir):
    """
    Plot predicted vs actual SOH - Notebook 3, Section 3.3.2.1
    """
    plt.figure(figsize=(10, 6))
    
    # Check which prediction columns exist
    available_models = []
    if 'soh_pred_linear' in model_df.columns:
        plt.scatter(model_df["soh"], model_df["soh_pred_linear"],
                   label="Linear Regression", alpha=0.7, s=80)
        available_models.append("Linear")
    
    if 'soh_pred_rf' in model_df.columns:
        plt.scatter(model_df["soh"], model_df["soh_pred_rf"],
                   label="Random Forest", alpha=0.7, s=80)
        available_models.append("Random Forest")
    
    if 'soh_pred_xgb' in model_df.columns:
        plt.scatter(model_df["soh"], model_df["soh_pred_xgb"],
                   label="XGBoost", alpha=0.7, s=80)
        available_models.append("XGBoost")
    
    # Perfect prediction line
    plt.plot([0.6, 1.05], [0.6, 1.05], "k--", label="Perfect Prediction",
             alpha=0.5, linewidth=2)
    
    plt.xlabel("Actual SOH")
    plt.ylabel("Predicted SOH")
    plt.title(f"Predicted vs Actual SOH ({', '.join(available_models)})")
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    output_path = save_dir / "predicted_vs_actual_soh.png"
    plt.savefig(output_path, dpi=300)
    plt.show()
    plt.close()
    
    print(f"  Predicted vs actual saved: {output_path.name}")
    return output_path


def plot_model_performance_comparison(metrics_df=None, save_dir=None):
    """
    Plot model performance comparison - Notebook 3, Section 3.3.2.2
    """
    if metrics_df is None:
        # Default metrics from notebook
        metrics_df = pd.DataFrame({
            "Model": ["Linear Regression", "Random Forest", "XGBoost"],
            "MAE": [0.0181, 0.0099, 0.0006],
            "RMSE": [0.0266, 0.0196, 0.0007],
            "R2": [0.9214, 0.9572, 0.9999]
        })
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    metrics = ['MAE', 'RMSE', 'R2']
    titles = ['Mean Absolute Error (Lower is Better)',
              'Root Mean Square Error (Lower is Better)',
              'R2 Score (Higher is Better)']
    
    colors = ['skyblue', 'lightgreen', 'salmon']
    
    for idx, (metric, title, color) in enumerate(zip(metrics, titles, colors)):
        axes[idx].bar(metrics_df['Model'], metrics_df[metric], color=color)
        axes[idx].set_title(title)
        axes[idx].set_ylabel(metric)
        axes[idx].tick_params(axis='x', rotation=45)
        axes[idx].grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for i, v in enumerate(metrics_df[metric]):
            axes[idx].text(i, v + 0.01 * v, f'{v:.4f}',
                          ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    
    if save_dir:
        output_path = save_dir / "model_performance_comparison.png"
        plt.savefig(output_path, dpi=300)
        plt.show()
        plt.close()
        print(f"  Model performance comparison saved: {output_path.name}")
        return output_path
    else:
        plt.show()
        return None


# ============================================================================
# 4. MAIN VISUALIZATION PIPELINE
# ============================================================================

def generate_eda_visualizations(soh_df, output_dir=None):
    """
    Generate all EDA visualizations from Notebook 1
    """
    if output_dir is None:
        output_dir, _ = configure_visualization()
    
    print("\n" + "="*60)
    print("GENERATING EDA VISUALIZATIONS")
    print("="*60)
    
    results = {}
    
    # 1. SOH Trend
    results['soh_trend'] = plot_soh_trend(soh_df, output_dir)
    
    # 2. Capacity Fade
    if 'max_capacity_mah' in soh_df.columns:
        results['capacity_fade'] = plot_capacity_fade(soh_df, output_dir)
    
    # 3. SOH Distribution
    results['soh_distribution'] = plot_soh_distribution(soh_df, output_dir)
    
    # 4. Degradation Rate
    results['degradation_data'] = plot_degradation_rate(soh_df, output_dir)
    
    print("\nEDA visualizations completed")
    return results


def generate_modeling_visualizations(model_df, output_dir=None):
    """
    Generate modeling visualizations from Notebook 3
    """
    if output_dir is None:
        _, output_dir = configure_visualization()
    
    print("\n" + "="*60)
    print("GENERATING MODELING VISUALIZATIONS")
    print("="*60)
    
    results = {}
    
    # Predicted vs Actual
    if any(col in model_df.columns for col in ['soh_pred_linear', 'soh_pred_rf', 'soh_pred_xgb']):
        results['pred_vs_actual'] = plot_predicted_vs_actual(model_df, output_dir)
    
    # Model Performance Comparison
    results['performance_comparison'] = plot_model_performance_comparison(
        metrics_df=None, save_dir=output_dir
    )
    
    print("\nModeling visualizations completed")
    return results


def generate_all_visualizations(soh_df, model_df=None):
    """
    Generate all visualizations from all notebooks
    """
    print("\n" + "="*70)
    print("BATTERY SOH PROJECT - VISUALIZATION PIPELINE")
    print("="*70)
    
    # Configure directories
    EDA_DIR, MODEL_DIR = configure_visualization()
    
    all_results = {
        'eda': generate_eda_visualizations(soh_df, EDA_DIR),
    }
    
    if model_df is not None:
        all_results['modeling'] = generate_modeling_visualizations(model_df, MODEL_DIR)
    
    print("\n" + "="*70)
    print("VISUALIZATION PIPELINE COMPLETED SUCCESSFULLY")
    print("="*70)
    print(f"EDA visualizations saved to: {EDA_DIR}")
    print(f"Modeling visualizations saved to: {MODEL_DIR}")
    
    return all_results


# ============================================================================
# 5. EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    """
    Example usage and demonstration
    """
    print("Battery SOH Visualization Module")
    print("This module contains all visualization functions from the notebooks.")
    
    # Example data (replace with your actual data)
    example_soh_data = pd.DataFrame({
        'cell_id': ['AC01', 'AC01', 'AC01', 'AC02', 'AC02', 'AC02'],
        'checkup_num': [0, 1, 2, 0, 1, 2],
        'soh_percentage': [100.0, 98.9, 98.1, 100.0, 97.5, 95.0],
        'max_capacity_mah': [56481.59, 55913.01, 55450.38, 56502.27, 55200.0, 54000.0]
    })
    
    example_model_data = pd.DataFrame({
        'soh': [1.0, 0.9899, 0.9817, 1.0, 0.975, 0.95],
        'soh_pred_linear': [0.995, 0.985, 0.975, 0.995, 0.980, 0.955],
        'soh_pred_rf': [0.998, 0.988, 0.982, 0.998, 0.976, 0.951],
        'soh_pred_xgb': [1.000, 0.990, 0.982, 1.000, 0.975, 0.950]
    })
    
    print("\nTo use this module:")
    print("1. Import in your script:")
    print("   from visualization import generate_all_visualizations")
    print("\n2. Load your data:")
    print("   soh_df = pd.read_csv('your_soh_data.csv')")
    print("   model_df = pd.read_csv('your_model_data.csv')")
    print("\n3. Generate visualizations:")
    print("   results = generate_all_visualizations(soh_df, model_df)")
    
    # Uncomment to run with example data
    # generate_all_visualizations(example_soh_data, example_model_data)