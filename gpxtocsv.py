"""
"""

import argparse
import csv
import gpxpy
import gpxpy.gpx


def main(args):

    with open(args.gpx_path, 'r') as gpx_file:
        with open(args.csv_path, 'w') as csv_file:

            gpx = gpxpy.parse(gpx_file)
            writer = csv.writer(csv_file)

            if args.header:
                writer.writerow(['latitude', 'longitude', 'elevation'])

            for track in gpx.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        writer.writerow([point.latitude, point.longitude, point.elevation])
                        # print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("gpx_path", type=str,
                        help="Path to GPX file with points")
    parser.add_argument("csv_path", type=str,
                        help="Path to output file for CSV")
    parser.add_argument("--header",
                        default=False, action='store_true',
                        help="Write header to CSV")

    args = parser.parse_args()
    main(args)
