def convert_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{hours}:{minutes}:{sec}"

print(convert_time(3770))  # 1:2:50
