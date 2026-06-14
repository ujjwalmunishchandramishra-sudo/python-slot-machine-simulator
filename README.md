🎰 Python Slot Machine SimulatorA highly interactive, terminal-based 3x3 slot machine simulator built from scratch using Python. The application models authentic casino mechanics, utilizing frequency-weighted symbol distributions, multi-line betting architectures, and a persistent state management engine to handle user balance dynamics.🚀 Technical HighlightsDynamic Grid Compilation: Generates a nested list matrix (3 Rows x 3 Columns) utilizing a non-replacing random selection protocol based on structured configuration dictionaries.Weighted Symbol Economy: Implements customized symbol distributions (symbol_count) and multi-tiered payout multipliers (symbol_value) to simulate realistic probability odds.Algorithmic Win-Checking: Line-matching algorithm cross-evaluates horizontal indices against active row wagers to calculate instantaneous returns.Robust Input Validation: Standardized loops using .isdigit() and conditional boundaries to neutralize runtime crashes from invalid input formats, out-of-bound bets, or non-integer inputs.📊 Game Configuration SpecsThe core gameplay loop operates on the following mathematical and rule constraints:SymbolReel Distribution CountMultiplier ValueA25xB44xC63xD82xGrid Size: 3 Rows x 3 ColumnsBetting Bounds: Min: $1 per line | Max: $100 per lineMax Playlines: 3 Horizontal Lines🕹️ Execution & ControlsPrerequisitesEnsure that a Python 3.x runtime environment is installed on your local operating machine.Installation & ExecutionClone the repository or download the source folder.Open your system terminal or Command Prompt (cmd) and navigate to the project root directory.Launch the game script:Bashpython "slot machine.py"
Gameplay Loop InterfaceDeposit: Set up your total starting virtual financial bankroll.Lines: Select how many paths (1–3) you want to cover with your stake.Bet: Allocate your exact wager amount per active playing line.Spin: Strike the Enter key to cycle the reels.Quit: Provide input q at the session loop prompt to finalize and cash out your ending balance.💻 Sample Terminal Gameplay OutputHere is a look at the terminal environment interface during execution, showcasing standard balances, line inputs, payouts, and error-trapping bounds:Plaintextwhat would you like to deposit? $1000
current balance is $ 1000
Press eneter to play (q to quit).
Enter the number of lines to bet on(1-3)?2
what would you like to bet on each line? $20
you are betting $ 20 on 2 lines. Total bet is equal to: $40 
D | D | C
D | D | C
B | C | D
you won $ 0.
You won on lines
current balance is $ 960

Press eneter to play (q to quit).
Enter the number of lines to bet on(1-3)?3
what would you like to bet on each line? $70
you are betting $ 70 on 3 lines. Total bet is equal to: $210 
D | D | D
D | D | D
B | C | C
you won $ 280.
You won on lines 1 2
current balance is $ 1030

Press eneter to play (q to quit).
Enter the number of lines to bet on(1-3)?2
what would you like to bet on each line? $90
you are betting $ 90 on 2 lines. Total bet is equal to: $180 
D | A | D
C | B | D
D | C | D
you won $ 0.
You won on lines
current balance is $ 850

Press eneter to play (q to quit).1
Enter the number of lines to bet on(1-3)?100
Enter a valid number of lines.
Enter the number of lines to bet on(1-3)?1
what would you like to bet on each line? $100
you are betting $ 100 on 1 lines. Total bet is equal to: $100 
C | D | D
C | D | D
D | D | C
you won $ 0.
You won on lines
current balance is $ 750
Press eneter to play (q to quit)._
📜 LicenseThis software is distributed open-source under the terms of the MIT License.
