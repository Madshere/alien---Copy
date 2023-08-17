import pygame
from settings import Settings




class Grounding:

    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        
        # load in audio files
        self.visualizatio...