def format_duration(seconds):
    seconds=max(0,int(seconds)); m,s=divmod(seconds,60); h,m=divmod(m,60)
    return f'{h:02d}:{m:02d}:{s:02d}' if h else f'{m:02d}:{s:02d}'
