from flask import Flask, render_template, request
from Search4Vowels import searchVowels

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/vsearch', methods=['POST'])
def do_vowel_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(searchVowels(phrase, letters))
    title = 'Here are your results:'
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to Search4Vowels on the web!')

if __name__ == '__main__':
    app.run(debug=True)
