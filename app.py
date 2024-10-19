from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].lower()
    results = []

    # Debug print statement to check the query
    print(f"Searching for: {query}")

    with open('books_new.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Debug print statement to see each row being checked
            print(f"Checking row: {row}")

            if (query in row['title'].lower() or
                query in row['author'].lower() or
                query in row['year'] or
                query in row['publisher'].lower()):
                results.append(row)
                # Debug print to confirm a match was found
                print(f"Match found: {row}")

    # Debug print to see the results
    print(f"Results: {results}")

    return render_template('index.html', books=results)

if __name__ == '__main__':
    app.run(debug=True)
