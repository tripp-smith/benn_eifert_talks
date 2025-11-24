# Plotting Dynamics: Color Schemes and Formatting Preferences

This document catalogs all color schemes, plot formatting preferences, and styling conventions discovered across the notebooks in this repository.

## 🎨 Color Scheme Philosophy

The plotting style is inspired by **UNC baseball dark jerseys**, featuring a dark mode theme that is easy on the eyes for extended reading and analysis. The color palette emphasizes:

- **Navy blue tones** for backgrounds and structure
- **Carolina blue** for primary accents and highlights
- **Semantic colors** (red/green) for financial data (losses/profits, puts/calls)
- **High contrast** for readability

---

## 🎯 Base Color Palette

### Background Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Navy Blue** | `#1B3A6B` | Figure background, legend background, text box backgrounds |
| **Dark Navy** | `#0F1F3A` | Axes background (darker than figure for contrast) |
| **Grid Color** | `#2A4A6B` | Grid lines (subtle, low alpha) |

### Primary Accent Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Carolina Blue** | `#4B9CD3` | Primary accent color, axes edges, legend edges, default plot color |
| **Light Carolina Blue** | `#7BAFD4` | Secondary accent, alternative series colors |
| **Teal** | `#20B2AA` | Additional accent for diagrams and special highlights |

### Text and Reference Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Light Gray/White** | `#E8E8E8` | All text, tick labels, reference lines (zero lines, ATM markers) |

---

## 📊 Semantic Color Assignments

### Financial Data Colors

#### Options Trading (Puts vs Calls)
- **Puts (Long Put, OTM Puts)**: 
  - Fill: `#CD5C5C` (Indian Red)
  - Edge: `#8B3A3A` (Dark Red)
  
- **Calls (Short Call, OTM Calls)**:
  - Fill: `#66CDAA` (Medium Aquamarine)
  - Edge: `#3A8B6B` (Sea Green)

#### Profit/Loss Visualization
- **Losses/Red Quadrants**: `#CD5C5C` (Indian Red)
- **Profits/Green Quadrants**: `#66CDAA` (Medium Aquamarine)
- **Neutral/Zero**: `#1B3A6B` (Navy Blue)

#### Market Data Series
- **SPY (S&P 500)**: `#4B9CD3` (Carolina Blue) - default primary
- **VIX (Volatility Index)**: `#7BAFD4` (Light Carolina Blue) - secondary series
- **Trend Lines**: `#CD5C5C` (Indian Red) - for emphasis
- **Reference Lines**: `#E8E8E8` (Light Gray) - zero lines, ATM markers

---

## 🎨 Custom Colormaps

### PnL Heatmap Colormap

For visualizing portfolio profit/loss across spot-volatility space:

```python
from matplotlib.colors import LinearSegmentedColormap

colors_list = ['#CD5C5C', '#8B3A3A', '#1B3A6B', '#3A8B6B', '#66CDAA']
cmap_custom = LinearSegmentedColormap.from_list('dark_pnl', colors_list, N=100)
```

**Color Progression:**
- `#CD5C5C` → Deep red (large losses)
- `#8B3A3A` → Dark red (moderate losses)
- `#1B3A6B` → Navy blue (neutral/zero)
- `#3A8B6B` → Dark green (moderate profits)
- `#66CDAA` → Bright green (large profits)

**Usage:** Heatmaps, contour plots, 3D surfaces showing financial PnL terrain

---

## ⚙️ Matplotlib Configuration

### Standard Setup

```python
import matplotlib.pyplot as plt

# Dark mode styling inspired by UNC baseball dark jerseys
plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': '#1B3A6B',      # Navy blue figure background
    'axes.facecolor': '#0F1F3A',        # Dark navy axes background
    'axes.edgecolor': '#4B9CD3',        # Carolina blue axes edges
    'axes.labelcolor': '#E8E8E8',       # Light gray text for labels
    'xtick.color': '#E8E8E8',           # Light gray tick labels
    'ytick.color': '#E8E8E8',           # Light gray tick labels
    'text.color': '#E8E8E8',            # Light gray for all text
    'grid.color': '#2A4A6B',            # Subtle navy grid
    'grid.alpha': 0.3,                  # Low opacity for subtlety
    'figure.figsize': (12, 6),          # Default figure size
    'legend.facecolor': '#1B3A6B',      # Navy legend background
    'legend.edgecolor': '#4B9CD3',      # Carolina blue legend border
    'legend.framealpha': 0.9,           # Slightly transparent
})
```

### Alternative Styles (for specific notebooks)

Some notebooks may use:
- `seaborn-v0_8-darkgrid` or `seaborn-darkgrid` (fallback)
- `seaborn.set_palette("husl")` for additional color variety

---

## 📐 Plot Formatting Conventions

### Figure Sizes

| Plot Type | Size | Usage |
|-----------|------|-------|
| Standard plots | `(12, 6)` | Default for most single plots |
| Wide plots | `(14, 6)` | Time series, comparison plots |
| Tall plots | `(12, 8)` | Multi-panel vertical layouts |
| Square plots | `(10, 10)` | Scatter plots, correlation plots |
| Large comparison | `(16, 7)` | Side-by-side comparisons |
| 3D plots | `(16, 8)` | 3D surface visualizations |

### Line Styles and Widths

| Element | Linewidth | Alpha | Style | Usage |
|---------|-----------|-------|-------|-------|
| Primary data lines | `1.5-2.0` | `0.7-0.8` | `-` | Main time series |
| Secondary data lines | `0.8-1.0` | `0.6` | `-` | Additional series |
| Reference lines (zero) | `0.5` | `1.0` | `--` | Zero lines, baselines |
| Reference lines (ATM) | `2.0` | `0.6` | `--` | At-the-money markers |
| Trend lines | `2.0` | `1.0` | `-` | Regression lines, emphasis |
| Grid lines | `0.5` | `0.3` | `--` | Background grid |
| Contour lines | `0.5-2.5` | `0.2-0.7` | `-` | Contour plots |

### Scatter Plot Settings

```python
# Standard scatter plot
plt.scatter(x, y, 
           s=60,                    # Marker size
           alpha=0.7,               # Transparency
           color='#4B9CD3',         # Fill color
           edgecolors='#E8E8E8',    # Edge color (optional)
           linewidth=0.5,           # Edge width
           zorder=3)                # Layer order
```

### Histogram Settings

```python
# Standard histogram
plt.hist(data, 
        bins=50,                    # Number of bins
        alpha=0.7,                  # Transparency
        edgecolor='#4B9CD3',        # Edge color
        color='#4B9CD3')            # Fill color
```

### Bar Chart Settings

```python
# Standard bar chart
bars = ax.bar(positions, values,
              color=colors,         # List of colors
              alpha=0.7,            # Transparency
              edgecolor='#4B9CD3',  # Edge color
              linewidth=1.5)       # Edge width
```

---

## 🎯 Text Box and Annotation Formatting

### Standard Text Box Style

```python
props = dict(
    boxstyle='round',              # Rounded corners
    facecolor='#1B3A6B',           # Navy background
    alpha=0.9,                     # Slight transparency
    edgecolor='#4B9CD3',          # Carolina blue border
    linewidth=1                   # Border width
)

ax.text(x, y, text,
       fontsize=10,                # Text size
       color='#E8E8E8',            # Light gray text
       bbox=props,                 # Apply box style
       verticalalignment='top')    # Text alignment
```

### Annotation Styles

**Profit Quadrant Labels:**
```python
bbox=dict(
    boxstyle='round',
    facecolor='#1B3A6B',
    alpha=0.9,
    edgecolor='#66CDAA',          # Green border for profit
    linewidth=2
)
color='#3A8B6B'                    # Green text
```

**Loss Quadrant Labels:**
```python
bbox=dict(
    boxstyle='round',
    facecolor='#1B3A6B',
    alpha=0.9,
    edgecolor='#CD5C5C',          # Red border for loss
    linewidth=2
)
color='#8B3A3A'                    # Dark red text
```

---

## 📊 Specialized Plot Types

### Heatmaps and Contour Plots

```python
# Contour fill
im = ax.contourf(x, y, z,
                levels=50,          # Number of contour levels
                cmap=cmap_custom,  # Custom colormap
                alpha=0.9,         # Transparency
                extend='both')     # Extend beyond data range

# Contour lines
contour_lines = ax.contour(x, y, z,
                          levels=20,           # Fewer levels for lines
                          colors='#E8E8E8',    # Light gray lines
                          alpha=0.2,          # Very subtle
                          linewidths=0.5)     # Thin lines

# Zero contour (highlighted)
zero_contour = ax.contour(x, y, z,
                         levels=[0],          # Only zero level
                         colors='#E8E8E8',     # Light gray
                         linewidths=2.5,      # Thicker line
                         linestyles='--')     # Dashed
```

### 3D Surface Plots

```python
from mpl_toolkits.mplot3d import Axes3D

surf = ax.plot_surface(x, y, z,
                       cmap=cmap_custom,      # Custom colormap
                       alpha=0.9,             # Transparency
                       linewidth=0,          # No edge lines
                       antialiased=True,      # Smooth rendering
                       edgecolor='none',      # No edges
                       shade=True)            # Shading enabled
```

### Quadrant Highlighting

```python
# Profit quadrant (bottom-left: Spot < 0, Vol > 0)
ax.contourf(x, y, 
           np.where(profit_mask, 1, np.nan),
           levels=[0.5, 1.5],
           colors=['#66CDAA'],               # Green tint
           alpha=0.15,                       # Very subtle
           hatches=['///'])                  # Diagonal hatch pattern

# Pain quadrant (bottom-left: Spot < 0, Vol < 0)
ax.contourf(x, y,
           np.where(pain_mask, 1, np.nan),
           levels=[0.5, 1.5],
           colors=['#CD5C5C'],               # Red tint
           alpha=0.15,                       # Very subtle
           hatches=['\\\\\\'])               # Backslash hatch pattern
```

---

## 🎨 Color Dictionary Patterns

### Standard Color Mappings

```python
# Market data series
colors = {
    'SPY': '#4B9CD3',      # Carolina blue
    '^VIX': '#7BAFD4'      # Light Carolina blue
}

# Options positions
option_colors = {
    'put': '#CD5C5C',      # Indian red
    'call': '#66CDAA'      # Medium aquamarine
}

# Portfolio components
portfolio_colors = ['#CD5C5C', '#66CDAA', '#4B9CD3', '#E8E8E8']
# Red (put), Green (call), Blue (hedge), Gray (total)
```

---

## 📏 Font Sizes

| Element | Font Size | Usage |
|---------|-----------|-------|
| Title | `16` | Main plot title |
| Subtitle | `14` | Subplot titles, section headers |
| Axis Labels | `12` | X and Y axis labels |
| Legend | `10-11` | Legend text |
| Tick Labels | Default | Automatic (usually 10) |
| Annotation Text | `9-10` | Text boxes, annotations |
| Small Annotations | `8` | Contour labels, small notes |

---

## 🔍 Alpha (Transparency) Values

| Element | Alpha | Usage |
|---------|-------|-------|
| Primary data lines | `0.7-0.8` | Main series |
| Secondary data lines | `0.6` | Additional series |
| Scatter points | `0.5-0.7` | Data points |
| Histogram bars | `0.6-0.7` | Distribution plots |
| Bar charts | `0.7` | Categorical data |
| Grid lines | `0.3` | Background grid |
| Contour fill | `0.9` | Heatmaps |
| Contour lines | `0.2-0.5` | Contour overlays |
| Quadrant highlights | `0.15` | Subtle region highlighting |
| Text boxes | `0.9` | Slight transparency |
| Reference lines | `0.5-0.7` | Zero lines, markers |

---

## 🎯 Marker Styles

| Marker | Symbol | Usage |
|--------|--------|-------|
| Circle | `'o'` | Initial/current values |
| Square | `'s'` | Sticky strike markers |
| Triangle Up | `'^'` | Sticky delta markers |
| Star | `'*'` | Special emphasis points |
| Default | `'.'` | General scatter points |

---

## 📋 Complete Example

Here's a complete example showing all conventions:

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Setup dark mode
plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': '#1B3A6B',
    'axes.facecolor': '#0F1F3A',
    'axes.edgecolor': '#4B9CD3',
    'axes.labelcolor': '#E8E8E8',
    'xtick.color': '#E8E8E8',
    'ytick.color': '#E8E8E8',
    'text.color': '#E8E8E8',
    'grid.color': '#2A4A6B',
    'grid.alpha': 0.3,
    'figure.figsize': (12, 6),
    'legend.facecolor': '#1B3A6B',
    'legend.edgecolor': '#4B9CD3',
    'legend.framealpha': 0.9,
})

# Create figure
fig, ax = plt.subplots(figsize=(14, 8))

# Plot data with semantic colors
ax.plot(x_data, y_data, 
       linewidth=2, 
       color='#4B9CD3', 
       alpha=0.8, 
       label='Primary Series')

# Add reference line
ax.axhline(0, color='#E8E8E8', linewidth=0.5, linestyle='--')

# Add scatter points
ax.scatter(x_points, y_points,
          s=60,
          alpha=0.7,
          color='#CD5C5C',
          edgecolors='#8B3A3A',
          linewidth=0.5,
          zorder=3,
          label='Data Points')

# Add text annotation
props = dict(boxstyle='round', 
            facecolor='#1B3A6B', 
            alpha=0.9, 
            edgecolor='#4B9CD3', 
            linewidth=1)
ax.text(0.05, 0.95, 'Annotation Text',
       transform=ax.transAxes,
       fontsize=10,
       verticalalignment='top',
       bbox=props,
       color='#E8E8E8')

# Formatting
ax.set_title('Plot Title', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('X Axis Label', fontsize=12)
ax.set_ylabel('Y Axis Label', fontsize=12)
ax.legend(fontsize=10, loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## 🎨 Summary of Key Principles

1. **Dark Mode First**: All plots use dark backgrounds for extended viewing comfort
2. **Consistent Color Semantics**: Red for losses/puts, green for profits/calls, blue for primary data
3. **High Contrast**: Light text (`#E8E8E8`) on dark backgrounds for readability
4. **Subtle Grids**: Low alpha (0.3) grids that don't distract from data
5. **Layered Information**: Use zorder, alpha, and linewidths to create visual hierarchy
6. **Professional Appearance**: Rounded text boxes, consistent spacing, clear labels
7. **Accessibility**: High contrast ratios and clear visual distinctions

---

## 📝 Notes

- This color scheme is specifically designed for **dark mode** viewing
- Colors are optimized for **extended reading** and **data analysis**
- The palette is inspired by **UNC baseball dark jerseys** for a cohesive aesthetic
- All hex codes are provided for easy copy-paste into code
- When in doubt, use `#4B9CD3` (Carolina Blue) as the default accent color

---

*Last Updated: Based on analysis of `skew.ipynb`, `crypto_funding.ipynb`, and `bessent_fox_news_trump_cost_of_living.ipynb`*

