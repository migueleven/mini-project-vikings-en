# 🛡️ Vikings vs. Saxons ⚔️
![image](https://github.com/user-attachments/assets/0d0d5ef1-eef3-49c4-a49b-dbab5549a7ab)

---

## **📖 Project Overview**

The **Vikings vs. Saxons** project simulates an epic battle between Viking warriors and Saxon soldiers using **object-oriented programming** principles in Python. It models individual warriors, their respective armies, attacks, damage management, and ultimately determines the outcome of the war.

### **What this project includes**:
- ⚙️ **Core Classes**: `Soldier`, `Viking`, and `Saxon`.
- 🧠 A main `War` class that orchestrates interactions between armies.
- ✅ **Unit tests** to ensure the functionality and reliability of the implemented features.
- 🎮 A battle simulation script that showcases the mechanics of the war.

---

## **🌟 Key Features**

### **Classes**

#### **`Soldier`** 🪖
Represents a generic soldier with basic attributes and behaviors.

- **Attributes**:
  - `health`: The soldier's health points.
  - `strength`: The soldier's strength value.
- **Methods**:
  - `attack()`: Returns the soldier's strength.
  - `receiveDamage(damage)`: Reduces the soldier's health by the specified damage amount.

#### **`Viking`** 🪓 *(inherits from `Soldier`)*
Represents a Viking warrior with additional unique behaviors.

- **Attributes**:
  - Inherits `health` and `strength` from `Soldier`.
  - `name`: The Viking's name.
- **Methods**:
  - `battleCry()`: Returns the Viking's war cry: `"Odin Owns You All!"`.
  - `receiveDamage(damage)`: Adjusts health and returns a message indicating damage or death.

#### **`Saxon`** 🛡️ *(inherits from `Soldier`)*
Represents a Saxon soldier.

- **Methods**:
  - `receiveDamage(damage)`: Adjusts health and returns a message indicating damage or death.

#### **`War`** ⚔️
Manages the interaction between Viking and Saxon armies.

- **Attributes**:
  - `vikingArmy`: A list containing all Viking warriors.
  - `saxonArmy`: A list containing all Saxon soldiers.
- **Methods**:
  - `addViking(viking)`: Adds a Viking warrior to the Viking army.
  - `addSaxon(saxon)`: Adds a Saxon soldier to the Saxon army.
  - `vikingAttack()`: Simulates an attack from a random Viking on a random Saxon.
  - `saxonAttack()`: Simulates an attack from a random Saxon on a random Viking.
  - `showStatus()`: Returns the current status of the war based on the remaining armies.

---

## **✅ Unit Testing**

The project includes a comprehensive suite of unit tests to ensure that all components work as expected. These tests cover:

- **Correct instantiation of classes**:
  - Ensures that all required attributes are properly initialized.
- **Method behavior**:
  - Validates methods like `attack()`, `receiveDamage()`, and `battleCry()`.
- **Army management in `War` class**:
  - Tests functionality for adding warriors and simulating attacks.
    
---

## **🚀 Future Improvements**

1. **🔒 Robustness and Validations**:
   - Ensure health and strength values are within valid ranges during instantiation.
   - Handle invalid inputs gracefully.

2. **🤖 Strategic AI**:
   - Implement advanced strategies for Viking and Saxon attacks.
   - Introduce critical hits or defensive maneuvers.

3. **🪖 New Warrior Types**:
   - Add additional classes like Archers or Knights with unique attributes and methods.

4. **🎨 Visualization**:
   - Create a visual representation of the battlefield using ASCII art or a graphical library.

5. **📝 Detailed Logs**:
   - Generate detailed logs for each round to track the progression of the battle.

---

## **📜 License**

This project is open-source and available under the **MIT License**. Feel free to use, modify, and distribute it. 😊
