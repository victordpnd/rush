from sample_data import tracks
from catalog import print_catalog
from statistics import print_statistics


def main():
    print_catalog(tracks)
    print_statistics(tracks)


if __name__ == "__main__":
    main()
