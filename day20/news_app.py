import tkinter as tk
from tkinter import scrolledtext
import requests

def get_news():
    api_key = 'e205d77d7bc14acc8744d3ea10568f50'  # Replace 'YOUR_API_KEY' with your actual News API key
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()

        if 'articles' in data:
            articles = data['articles']
            news_text.delete(1.0, tk.END)  # Clear previous news

            if not articles:
                news_text.insert(tk.END, "No articles found.")
            else:
                for article in articles:
                    # Format title in bold and different color
                    news_text.insert(tk.END, article['title'] + "\n", 'bold')
                    news_text.insert(tk.END, f"Source: {article['source']['name']}\n")
                    news_text.insert(tk.END, f"Description: {article['description']}\n\n")
                    news_text.insert(tk.END, '-'*50 + "\n\n")  # Separate articles

        else:
            news_text.insert(tk.END, "No articles found.")

    except Exception as e:
        news_text.insert(tk.END, f"Error fetching news: {e}")

# Create the main window
root = tk.Tk()
root.title("News App")

# Set background color to black
root.configure(bg="black")

# Define text style for bold title
bold_text = ('TkDefaultFont', 10, 'bold')

# Create a frame
frame = tk.Frame(root, bg="black")
frame.pack(padx=10, pady=10)

# Create a button to fetch news
fetch_button = tk.Button(frame, text="Fetch News", command=get_news,font=bold_text,bg="white", fg="black")
fetch_button.pack()

# Create a scrolled text widget to display news
news_text = scrolledtext.ScrolledText(frame, width=100, height=40, font=bold_text, bg="gray", fg="black")
news_text.pack()

# Tag configuration for bold text
news_text.tag_configure('bold', font=bold_text, foreground='black')

# Run the main event loop
root.mainloop()
