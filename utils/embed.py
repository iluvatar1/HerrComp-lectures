# RUN ME FOR EMBEDING VIDEOS AND URLS
from IPython.display import HTML
from urllib.parse import urlparse, parse_qs

def youtube_embed_url(url):
    """Convert any YouTube URL to embed format."""
    parsed = urlparse(url)
    if parsed.netloc == "youtu.be":
        vid = parsed.path.lstrip("/")
    elif "shorts" in parsed.path:
        vid = parsed.path.split("/shorts/")[-1]
    elif "embed" in parsed.path:
        return url  # already embed format, do nothing
    else:
        vid = parse_qs(parsed.query).get("v", [None])[0]
    return f"https://www.youtube.com/embed/{vid}" if vid else url

def embed(url, caption="", width="90%", aspect=(16, 9)):
    if "youtube.com" in url or "youtu.be" in url:
        url = youtube_embed_url(url)
    w, h = aspect
    padding = float(width.strip("%")) * h / w
    return HTML(f'''
<div style="display:flex; flex-direction:column; align-items:center; width:100%;">
  <div style="position:relative; width:{width}; padding-bottom:{padding:.2f}%; height:0; overflow:hidden;">
    <iframe src="{url}"
      style="position:absolute; top:0; left:0; width:100%; height:100%; border:0;"
      allowfullscreen title="{caption}">
    </iframe>
  </div>
  {"<p style='font-style:italic; margin-top:0.4em;'>" + caption + "</p>" if caption else ""}
</div>''')