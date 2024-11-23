# News Summary CLI

A simple command-line application that fetches and displays the latest South African news headlines. Each headline includes a clickable link to the full article for quick access.

## Features

- Fetches the latest news focused on South Africa.  
- Displays headlines along with links to the full articles.  
- Lightweight and easy-to-use command-line interface.  

## Prerequisites

- Python 3.8 or higher installed on your system.  
- An API key from a news provider.  

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/ThaboChauke/news-summary-cli.git
   cd news-summary-cli
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:  
   ```bash
   python main.py
   ```
2. The CLI will display a list of the latest South African news headlines. Each headline is followed by a clickable link to the full article.  

## Example Output

```
Latest South African News:
1. "South Africa's Economy Shows Signs of Recovery"  
   Link: https://example.com/article/1  

2. "Local Elections Spark Debate Over Key Issues"  
   Link: https://example.com/article/2  

3. "New Discoveries in South Africa's Rich Natural Reserves"  
   Link: https://example.com/article/3  
```

## Technologies Used

- **Python**: Core language for the application.  
- **Requests**: For making API calls.  
- **dotenv**: For managing environment variables.  

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

---
