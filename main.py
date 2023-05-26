from youtube_statistics import YTstats

API_KEY = 'AIzaSyCKK0Bd4uM1ycDdeD2Ka_t-Zd1fyY6SjYA'
channel_id = 'UC1emV4A8liRs9p80CY8ElUQ'

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()  # dumps to .json
