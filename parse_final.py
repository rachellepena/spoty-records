import csv

final = open('output/final.csv', 'r', encoding='utf-8')
reader = csv.DictReader(final)

track_dicts = []
track_names = []
for track in reader:
    if track['name'] in track_names:
        track_dicts[track_names.index(track['name'])]['msPlayed'] += track['msPlayed']
    else: 
        track_names.append(track['name'])
        track_dict = {
            'trackName': track['trackName'],
            'artistName': track['artistName'],
            'msPlayed': track['msPlayed'],
            'danceability': track['danceability'],
            'energy': track ['energy'],
            'key': track['key'],
            'loudness': track['loudness'],
            'mode': track['mode'],
            'speechiness': track['speechiness'],
            'acousticness': track['acousticness'],
            'instrumentalness': track['instrumentalness'],
            'liveness': track['liveness'],
            'valence': track['valence'],
            'tempo': track['tempo'],
            'id': track['id'],
            'albumName': track['albumName'],
            'albumID': track['albumID']

        }
        track_dicts.append(track_dict)
final.close()

output_file = open('parsed_final.csv', 'w', newline='')
writer = csv.DictWriter(output_file, ['trackName', 'artistName', 'msPlayed', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'id', 'albumName', 'albumID'])
writer.writeheader()
for track_dict in sorted(track_dicts, key=lambda x: x['msPlayed'], reverse=True):
    writer.writerow(track_dict)
output_file.close()