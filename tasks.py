import json

# task 1
settings = {'volume':80, 'brightness':60, 'diffuculty': 'medium'}

with open('settings.json', 'w') as f:
    json.dump(settings, f)

with open('settings.json', 'r') as f2:
    lines = json.load(f2)
    res = [ lines[ky] for ky in lines if ky=='diffuculty']
    print('diffuculty', res, end='\n\n')
