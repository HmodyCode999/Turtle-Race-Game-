> 🎓 This project was built as a fun way to practice basic Python, logic building, and using the Turtle module.

# 🐢 Turtle Race Game

A fun and interactive turtle racing game built with Python's Turtle graphics library. Watch as colorful turtles compete in an exciting race to the finish line!

## 🎮 Game Overview

Turtle Race is a simple yet engaging game where players can bet on their favorite turtle and watch them race across the screen. Each turtle moves at random speeds, making every race unpredictable and exciting!

### Features
- **4 Colorful Turtles**: Choose from Hmody (White), Red, Blue, or Orange turtle
- **Random Movement**: Each turtle moves at unpredictable speeds for fair competition  
- **Interactive Betting**: Pick your favorite turtle before each race
- **Visual Feedback**: Clear winner announcements with colored text
- **Replay System**: Play multiple rounds without restarting
- **Custom Graphics**: Hand-drawn finish line with checkered pattern

## 🚀 How to Play

1. **Start the Game**: Run the Python script
2. **Choose Your Turtle**: Enter your choice when prompted:
   - `Hmody` or `White` - The signature white turtle
   - `Red` - The speedy red turtle  
   - `Blue` - The steady blue turtle
   - `Orange` - The energetic orange turtle
3. **Watch the Race**: Sit back and watch your turtle compete!
4. **See Results**: Get instant feedback on whether you won or lost
5. **Play Again**: Choose a new turtle for the next race

## 🛠️ Technical Details

### Built With
- **Python 3.x**
- **Turtle Graphics Library** - For game visualization and animation
- **Random Module** - For unpredictable turtle movement

### Game Mechanics
- **Screen Size**: 1200x700 pixels for optimal viewing
- **Movement System**: Random speed selection from 1-10 pixels per frame
- **Win Condition**: First turtle to cross the finish line at x-coordinate 420
- **Race Duration**: Maximum 180 movement cycles per race
- **Input Validation**: Handles invalid player input gracefully and ends the game with feedback

### Code Structure
```
├── Turtle Setup & Configuration
├── Screen Initialization  
├── Game Functions
│   ├── members() - Initialize turtle positions
│   ├── end_line() - Draw finish line
│   ├── player_turtle() - Handle user selection
│   ├── check_winner() - Determine race outcome
│   ├── race() - Main game loop
│   └── clear() - Reset screen for new race
└── Main Game Loop
```

## 🎯 Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- No additional packages required (uses built-in libraries)

### Running the Game
1. Clone this repository:
   ```bash
   git clone https://github.com/HmodyCode999/Turtle-Race-Game-.git
   ```
2. Navigate to the project directory:
   ```bash
   cd turtle-race-game
   ```
3. Run the game:
   ```bash
   python turtle_race.py
   ```
✅ Compatible with Windows, Linux, and macOS

## 🔮 Future Enhancements

- [ ] Add sound effects for race events
- [ ] Implement betting system with points
- [ ] Create tournament mode with multiple races
- [ ] **Input Validation**: Handles invalid player input gracefully and ends the game with feedback

## ✨ Author

Developed by [Hmody](https://github.com/HmodyCode999) 👨‍💻  
Proud student of Computer Science @ Zagazig University 🇪🇬

##

**Happy Racing! 🏁**


*Made with ❤️ and lots of turtle power! 🐢*
