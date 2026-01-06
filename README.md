# Inverter Controller for Home Assistant

A reactive, event-driven power balancing integration for Home Assistant. It dynamically adjusts your inverter's output limit based on real-time grid consumption, battery state of charge (SoC), and solar production.

# 🔋 Inverter Controller for Home Assistant

**A custom Home Assistant integration that allows you to control your inverter with configurable parameters.**

[![release](https://img.shields.io/github/v/release/MarcelWepper/Inverter-Controller?include_prereleases&style=flat-square)](https://github.com/MarcelWepper/Inverter-Controller/releases)
[![HACS Integration](https://img.shields.io/badge/HACS-Integration-blue.svg?style=flat-square)](https://github.com/hacs/integration)
[![License](https://img.shields.io/github/licence/MarcelWepper/Inverter-Controller?style=flat-square&color=orange)](https://github.com/MarcelWepper/Inverter-Controller/blob/main/LICENCE)

[![Open your Home Assistant instance and open the repository in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=MarcelWepper&repository=Inverter-Controller&category=integration)

## 🚀 Key Features

* **Reactive Power Balancing**: Unlike timer-based scripts, this integration listens for state changes and adjusts power limits instantly as your house load shifts.
* **Exponential Moving Average (EMA)**: Built-in smoothing for solar production data to prevent "flapping" during cloudy days.
* **Safety Guard**: Automatically forces the inverter to a safe minimum (100W) if solar production drops below a critical threshold.
* **High SoC Hard Boost**: Intelligent hysteresis logic that ramps up inverter output when the battery is nearly full (e.g., >96%) to prevent energy waste.
* **Advanced Statistics**: Provides calculated insights including **Estimated House Load**, **Solar Yield Ratio**, and a **Logic State** indicator.
* **Master Switch**: Includes a dashboard toggle to instantly enable or disable the controller logic.

---

## 🛠 Installation

### via HACS (Recommended)
1. Open **HACS** in your Home Assistant instance.
2. Navigate to **Integrations**.
3. Click the **three dots** in the top-right corner and select **Custom repositories**.
4. Paste your repository URL and select **Integration** as the category.
5. Click **Add**, then click **Download** on the Inverter Controller card.
6. **Restart** Home Assistant.

### Manual Installation
1. Download the `inverter_controller` folder from this repository.
2. Copy the folder into your `custom_components/` directory.
3. **Restart** Home Assistant.

---

## ⚙️ Configuration

Once installed, go to **Settings > Devices & Services > Add Integration** and search for **Inverter Controller**. 

### Step 1: Mandatory Entities
You must provide these four entities to start the logic:
* **Grid Power Sensor**: Measures net house power (Positive = Import, Negative = Export).
* **Battery SoC Sensor**: Measures battery percentage (0-100%).
* **Solar Production Sensor**: Measures raw PV power.
* **Inverter Limit Control**: The `number` or `input_number` entity that sets the inverter's maximum output.

### Step 2: Adjustable Parameters
After selecting entities, you can fine-tune the behavior:
* **Min/Max Power**: The absolute bounds for the inverter (e.g., 100W - 800W).
* **Step Size**: How many Watts to adjust by in each cycle (e.g., 50W).
* **EMA Alpha**: The smoothing factor for solar averaging. `0.1` is very smooth/slow, `0.9` is very reactive/jump
