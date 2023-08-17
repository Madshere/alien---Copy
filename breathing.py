class Breathing:

  def __init__(self):
    self.duration = 0
    self.rhythm = ''

  def breathe(self, duration, rhythm):
    self.duration = duration
    self.rhythm = rhythm
    print(f'Starting breathing technique with duration {duration} and rhythm {rhythm}...')
    # Call method to play breathing sounds and display 3D visual

