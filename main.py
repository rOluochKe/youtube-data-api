from youtube_statistics import YTstats

API_KEY = ''
channel_id = ''

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
yt.dump()  # dumps to .json
