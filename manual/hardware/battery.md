# Battery

RB-Y1 runs on a lithium-ion battery pack. The battery pack depends on the robot model (see [Battery Pack Specifications](#battery-pack-specifications)).

::: warning CAUTION
- Disconnect the charger before you drive the mobile base (see [Disconnect the Charger Before Driving the Mobile Base](../precautions/power_and_battery.md#disconnect-the-charger-before-driving-the-mobile-base)).
- If the robot is not used for a long time, disconnect the battery connector (see [Disconnect the Battery for Long-Term Storage](../precautions/power_and_battery.md#disconnect-the-battery-for-long-term-storage)).
- If the battery pack is damaged, swollen, hot or smells unusual, stop using the robot and contact the support team (see [Battery](../precautions/power_and_battery.md#battery)).
- Use only the charger described on this page.
:::

## Battery Charger

The RB-Y1 battery charger model is **HEP-600C-48**.

<img :src="$withBase('/images/hardware/battery/battery_charger1.png')" alt="HEP-600C-48 battery charger" class="center rounded-img" style="width:600px">

---
### Charger Specifications

| General Properties  | Value |
| ---------- | ----- |
| `Output Voltage Adj. Range`| 46.1 ~ 60.5V |
| `Output Current Adj. Range`  | 5.2 ~ 10.5A |
| `Input Voltage Range`  | 85 ~ 264VAC / 120 ~ 370VDC |
| `Input Frequency Range`  | 47 ~ 63Hz |
| `Input AC Current (Typ.)`  | 7A / 115VAC, 3.3A / 230VAC, 2.9A / 277VAC |
| `Charger Working Temp.`  | -40 ~ +70°C |

---
### Charging Curve

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/hardware/battery/charging_curve.png')" alt="Charging curve of the battery charger" class="rounded-img" style="width:800px">

</div>

<div>

| Parameter  | Value |
| ---------- | ----- |
| `Constant Current`| 10.5A |
| `V_boost`  | 57.6V |
| `V_float`  | 54.4V |

</div>

</div>

---
### Mechanical Specifications

The charger drawing is shown below.

<img :src="$withBase('/images/hardware/battery/battery_charger3.png')" alt="Battery charger dimensions" class="center rounded-img" style="width:600px">

<br><br>
<img :src="$withBase('/images/hardware/battery/battery_charger_drawing.png')" alt="Battery charger drawing" class="center rounded-img" style="width:600px">

## Charge the Battery

1. Stop the mobile base. Do not drive it while the charger is connected.
2. Connect the charger plug to the charging port on the mobile base (see [Connect the Charger](../getting-started/unboxing.md#connect-the-charger)), and connect the charger to AC power. The robot can stay powered on while it charges.
3. Check the battery level on the Web UI **Dashboard**, or read `battery_state.level_percent` (and `voltage`, `current`) from the robot state in the SDK.
4. Disconnect the charger before you drive the mobile base again.

The charger first charges with a constant current and then holds the voltage (see [Charging Curve](#charging-curve)).

::: info Not listed in this manual
This manual does not list the battery operating and storage temperatures, the charging time, or how the charger shows a full charge. Contact the support team (<a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>) for these values.
:::

## Battery Pack Specifications

The battery pack depends on the robot model. The capacity in Wh is based on the marked voltage (50 V).

---
### Model A Battery

<img :src="$withBase('/images/hardware/battery/battery_A.png')" alt="Model A battery pack" class="center rounded-img" style="width:600px">

| Property | Value |
| ---------- | ----- |
| `Specification` | Lithium-ion battery pack, 427 x 140 x 99 mm, 7.2 kg |
| `Serial Number` | Check the product label |
| `Model Name` | LV-50V25AH-DH375 |
| `Manufacturer` | TABOS Inc. |
| `Date of Manufacture` | Check the product label |
| `Voltage` | Marked 50V / Nominal 51.7V |
| `Capacity` | 25Ah, 1,250Wh |
| `Cycle Life` | Approx. 5,000 cycles based on the LV series (may vary depending on usage conditions) |

---
### Model M Battery

<img :src="$withBase('/images/hardware/battery/battery_M.png')" alt="Model M battery pack" class="center rounded-img" style="width:600px">

| Property | Value |
| ---------- | ----- |
| `Specification` | Lithium-ion battery pack, 467 x 171 x 138 mm, 14.2 kg |
| `Serial Number` | Check the product label |
| `Model Name` | LV-50V50AH-VX2COM |
| `Manufacturer` | TABOS Inc. |
| `Date of Manufacture` | Check the product label |
| `Voltage` | Marked 50V / Nominal 51.7V |
| `Capacity` | 50Ah, 2,500Wh |
| `Cycle Life` | Approx. 5,000 cycles based on the LV series (may vary depending on usage conditions) |
