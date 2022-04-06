from flask import Flask, render_template
import get_data
app = Flask(__name__)

@app.route("/")
def hello():
    artists = get_data.get_all_artist()
    return render_template("index.html", artists=artists)

@app.route("/songs/<int:id>")
def list_all_songs(id):
    songs= get_data.get_all_songs(id)
    artist= get_data.singer(id)
    artists = get_data.get_all_artist()
    return render_template("songslist.html",artist=artist,artists=artists,songs=songs)

@app.route("/songs/<int:id>/lyrics/<int:sid>")
def lyrics(sid,id):
    lyrics= get_data.get_lyrics(sid)
    songs= get_data.get_all_songs(id)
    artist= get_data.singer(id)
    artists = get_data.get_all_artist()
    return render_template("lyrics.html",lyrics=lyrics,artist=artist,artists=artists,songs=songs, current=sid)

if __name__== "__main__":
    app.run(debug=True) 


