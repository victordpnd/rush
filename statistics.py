def print_statistics(tracks):

    total_rating = sum(track.rating for track in tracks)
    average = total_rating / len(tracks)

    longest = max(tracks, key=lambda t: t.duration)

    print("-" * 45)
    print(f"Tracks: {len(tracks)}")
    print(f"Average Rating: {average:.2f}")
    print(f"Longest Track: {longest.title}")

    artists = {}

    for track in tracks:
        artists[track.artist] = artists.get(track.artist, 0) + 1

    print("\nArtists:")

    for artist, count in artists.items():
        print(f"  {artist}: {count}")
