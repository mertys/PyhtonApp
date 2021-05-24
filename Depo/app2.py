import json

with open('data.json' , 'r') as f,  open('data2.json' , 'w') as f2:
    content = json.load(f)
    for friend in content['friends']:
        del friend['age']

    json.dump(content, f2 , indent=4)


    # content = json.load(f)

    # for friend in content['friends']:
    #     print(friend['age'])

    # print(content)
    # print(type(content))
    # print(type(content['friends']))
    # print(type(content['friends'][0]))
        
