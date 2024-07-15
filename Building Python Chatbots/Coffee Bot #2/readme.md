# Coffee Chatbot Project - Enhanced Version

## Overview
This enhanced version of the Coffee Chatbot introduces loops to the Python-based project, further automating the coffee ordering process. It builds upon the initial chatbot by allowing users to place orders for multiple drinks, improving the user experience and efficiency of the ordering process.

## New Features
- **Multiple Drink Orders**: Users can now order more than one drink in a single session, enhancing the chatbot's functionality.
- **Loop Implementation**: Loops are used to handle multiple orders, allowing the chatbot to repeatedly ask for new orders until the user decides to stop.
- **Improved Input Validation**: The chatbot now includes additional input validation checks within loops to ensure users make recognizable selections.
- **User-Friendly Messages**: Incorporates user-friendly messages for unrecognized inputs, guiding users back to valid options.

## How It Works (New Processes)
1. **Order Multiple Drinks**: After completing an order, users are asked if they would like to order another drink.
2. **Loop Through Drink Orders**: The chatbot uses a `while` loop to continuously take orders until the user indicates they are finished.
3. **Validate User Inputs**: Within the loop, the chatbot checks if the user's input matches expected responses ('y' for yes, 'n' for no) and prompts again if not.
4. **Summarize All Orders**: Once the user finishes ordering, the chatbot summarizes all the drinks ordered before asking for the user's name.
5. **Completion Message**: The chatbot thanks the user by name and informs them that their orders will be ready shortly.

## Enhanced Technologies Used
- Python loops (`while`, `for`) to manage multiple orders and improve input validation.
- Enhanced input/output interactions for a smoother user experience.
- Conditional statements within loops to handle various user inputs and scenarios.
