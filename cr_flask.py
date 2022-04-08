from flask import Flask, render_template, jsonify
import get_data
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html")

@app.route("/artists")
def get_artists():
    artist = get_data.get_all_artist()
    artist_arr=[{'id':i[0],'name':i[1]} for i in artist]
    return jsonify(artist_arr)

@app.route("/songs/<int:id>")
def list_all_songs(id):
    songs= get_data.get_all_songs(id)
    artist= get_data.singer(id)
    artists = get_data.get_all_artist()
    songs_arr = [{'id':i[1], "name":i[0]} for i in songs]
    return jsonify(songs_arr)


@app.route("/songs/<int:id>/lyrics/<int:sid>")
def lyrics(sid,id):
    lyrics= get_data.get_lyrics(sid)
    songs= get_data.get_all_songs(id)
    artist= get_data.singer(id)
    artists = get_data.get_all_artist()
    print(lyrics)
    return jsonify(lyrics)

if __name__== "__main__":
    app.run(debug=True) 


