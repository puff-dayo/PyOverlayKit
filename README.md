<h1 align="center">PyOverlayKit</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Platform">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/github/last-commit/archiebhl/hwinsight.svg" alt="Last Commit">
</p>

Forked from [archiebhl/PyOverlayKit](https://github.com/archiebhl/PyOverlayKit), **PyOverlayKit** is a lightweight Python library for creating customizable, always-on-top overlay windows using **PySide6** or **PyQt6**. It supports transparent backgrounds, rounded theme, drag-to-move functionality, and includes a customizable close button with configurable behavior.

---

## Installation

Install directly from the GitHub repository:

```bash
pip install git+https://github.com/puff-dayo/PyOverlayKit.git
````

---

## Example Usage

See `example.py`.

## Overlay Options

```python
Overlay(
    show_close_button=True,
    close_behavior="exit",                 # Options: 'close', 'hide', 'exit'
    close_button_color="#FF4C4C",
    close_button_hover_color="darkred",
    rounded=True,
    corner_radius=15
)
```

### Available Methods

* `set_background_color(QColor)`
* `set_background_opacity(float)` – Range: 0.0 to 1.0
* `set_overall_opacity(float)` – Range: 0.0 to 1.0
* `set_geometry(x, y, width, height)`
* `set_close_behavior(str)`
* `set_close_button_visibility(bool)`
* `set_close_button_colors(normal_color, hover_color)`
* `set_rounded_corners(enabled, radius)`
* `add_widget(widget)`

---

### Licence

MIT License, see [archiebhl/PyOverlayKit/LICENSE](https://github.com/archiebhl/PyOverlayKit/blob/b4cbb536b205e30820bd53491d106687177c7e81/LICENSE).
