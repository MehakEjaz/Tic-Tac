# Tic-Tac
Tic-Tac-Toe Game(AIES Assignment 2)
Youtube link for explaination:
https://youtu.be/wBVQoApGguU?si=TtYgFaJlIeKpy6qW

Logic:
To build a **Tic-Tac-Toe AI** that plays optimally, and then improve its efficiency, you can implement two versions of the **Minimax algorithm**:



1. **Core Logic of the Tic-Tac-Toe Game**

The basic components of the game logic include:

* **Game Board**: A 3x3 grid (usually a 2D list or 1D array of 9 elements).
* **Players**: One is human (e.g., "X"), the other is AI (e.g., "O").
* **Game Rules**:

  * Players alternate turns.
  * A move is valid if the cell is empty.
  * Win conditions: any row, column, or diagonal has the same non-empty symbol.
  * The game ends in a win or a draw (all cells filled without a winner).

---

### 2. **Minimax Algorithm (Standard)**

The **Minimax** algorithm is a recursive decision-making algorithm used in two-player games like Tic-Tac-Toe. It assumes:

* The **AI wants to maximize** its score (best move for itself).
* The **opponent wants to minimize** the AI's score (best counter-move).

**Steps of Minimax:**

1. **Evaluate terminal states** (win/loss/draw) and assign scores:

   * AI win: +1
   * AI loss: -1
   * Draw: 0
2. **Simulate all possible moves** for the current player.
3. **Recursively call Minimax** for the opponent’s turn.
4. **Choose the move** with the highest (for AI) or lowest (for human) score.

**Problem**: This explores **every possible move**, leading to **redundant calculations**, especially in more complex games.

 3. **Alpha-Beta Pruning**

**Alpha-Beta Pruning** is an optimization of Minimax. It **eliminates branches** in the game tree that don’t influence the final decision, thereby reducing computation.

* **Alpha**: Best value that the maximizer (AI) can guarantee.
* **Beta**: Best value that the minimizer (opponent) can guarantee.
* During recursion:

  * If the **current node’s value is worse** than an already explored branch, **stop exploring** further. This is a **prune**.
  * This avoids evaluating unnecessary moves.

**Result**: Alpha-Beta Pruning leads to the **same optimal move** as standard Minimax but is **much faster**.



 4. **Performance Comparison**

Let’s compare the two based on **execution time and number of nodes explored**:

| Metric                      | Minimax (Standard) | Minimax with Alpha-Beta Pruning |
| --------------------------- | ------------------ | ------------------------------- |
| **Nodes Explored**          | \~5500             | \~1000                          |
| **Time Complexity**         | O(b^d)             | O(b^(d/2)) in best case         |
| **Response Time (AI move)** | Slower             | Faster                          |
| **Memory Use**              | Higher             | Lower                           |

Where:

* **b** = branching factor (up to 9 in Tic-Tac-Toe)
* **d** = depth of the tree (up to 9 moves)

**Key Takeaways**:

* Both algorithms lead to **perfect play** by the AI.
* **Alpha-Beta Pruning is significantly more efficient**, especially when good move ordering is applied.
* In small games like Tic-Tac-Toe, performance difference is noticeable but not critical; however, for larger games like chess, Alpha-Beta Pruning is essential.


