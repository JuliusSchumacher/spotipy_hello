import spotipy
import pprint

sp = spotipy.Spotify()

print('Welcome to the Spotify searcher! Type "end" to exit!')

while 1==1 :
    print('Search for artist or track?')
    sType = input()
    if sType == 'end' or sType != 'artist' and sType != 'track' :
        break
    print('Enter', sType, 'to search for!')
    query = input()

    if query == 'end':
        break

    results = sp.search(q=query, limit=20, type=sType)
    if sType == 'track':
        for i, t in enumerate(results['tracks']['items']):
            artist = t['artists'][0]['name']
            name = t['name']
            album = t['album']['name']
            print("{0}. {1} - {2} - {3}".format(i+1, name, artist, album))
    else:
        for i, t in enumerate(results['artists']['items']):
            name = t['name']
            print("{0}. {1}".format(i+1, name))