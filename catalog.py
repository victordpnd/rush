def stars(rating):
    return "★" * rating + "☆" * (5 - rating)


def print_catalog(tracks):

    print("=" * 45)
    print("          MUSIC CATALOG")
    print("=" * 45)

    for track in tracks:
        print(
            f"{track.title:<20}"
            f"{track.artist:<18}"
            f"{stars(track.rating)}"
        )
