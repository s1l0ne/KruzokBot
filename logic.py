from pymediainfo import MediaInfo
import datetime as dt


def get_metadata_pymediainfo(file_path):
    media_info = MediaInfo.parse(file_path)
    data = {}

    for track in media_info.tracks:
        if track.track_type == 'Video':
            return dt.datetime.strptime(track.encoded_date, '%Y-%m-%d %H:%M:%S UTC')


def is_equal_to_today(date):
    if dt.date(date.year, date.month, date.day) == dt.date.today():
        return True