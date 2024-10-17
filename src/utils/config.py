import json
from typing import Any, Union
from kivy.app import App
from kivy.storage.jsonstore import JsonStore
from kivy.utils import platform
from kivy.logger import Logger

class Config:
    def __init__(self):
        self.store = JsonStore('game_config.json')
        self.default_config = {
            'display' : {
                'orientation' : 'portrait',
                'fullscreen' : True,
            },
            'audio' : {
                'master_volume' : 1.0,
                'music_volume' : 0.7,
                'sfx_volume' : 0.5
            },
            'gameplay' : {
                'difficulty' : 'normal',
                'language' : 'en'
            },
            'controls' : {
                'touch_sensitivity' : 0.5,
                'vibration_enabled' : True
            }
        }

        if platform == 'android':
            self.default_config['android'] = {
                'back_button_behavior' : 'minimize',
                'immersive_mode' : True
            }

        elif platform == 'ios':
            self.default_config['ios'] = {
                'use_metal' : True
            }

        self.load_config()

    def load_config(self):
        if not self.store.exists('config'):
            self.store.put('config', **self.default_config)

    def get_config(self, *keys: str) -> Any:
        config = self.store.get('config')
        for key in keys:
            if key in config:
                config = config[key]
            else:
                return None
        return config
    
    def set_config(self, *keys: str, value: Any) -> None:
        config = self.store.get('config')
        temp = config
        for key in keys[:-1]:
            if key not in temp:
                temp[key] = {}
            temp = temp[key]
        temp[keys[-1]] = value
        self.store.put('config', **config)

    def reset_config(self) -> None:
        self.store.put('config', **self.default_config)