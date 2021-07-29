import json, os
from bot import Bot 

class main:
    def __init__(self) : 
        pass

    def main(self):
        with open(os.path.join(os.path.dirname(__file__),'credentials.json')) as f: 
            creds = json.load(f)
            f.close()

        with open(os.path.join(os.path.dirname(__file__),'settings.json')) as f:
            settings = json.load(f)
            f.close()

        # Creating bot instance
        self.Bot1 = Bot(creds=creds, settings=settings)
        #Bot started in thread 
        self.Bot1.start()

    def update_settings(self):
            try:
                with open(os.path.join(os.getcwd(),'settings.json')) as f:
                    settings = json.load(f)
                    f.close()
                self.Bot1.update_attributes(settings=settings)
                print("\n\tParameters updated!!\t\n")
                self.take_response()
            except:
                print('Invalid settings, check the settings.json')

if __name__ == '__main__':
    a = main()
    a.main()