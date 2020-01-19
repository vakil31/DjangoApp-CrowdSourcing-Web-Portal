def update_urllookup():
      data = open('static/video_list.txt', 'r',).read()
      rows = re.split('\n', data)  # splits along new line
      for index, row in enumerate(rows):
            cells = row.split(' ')
            obj = VideoUrl(vid_id=cells[0], vid_url='http://' + cells[1])
            obj.save()
      return
#don' delete this #update_urllookup()
# update_urllookup()