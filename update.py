import json

def perform_replacements(value):
    replacements = {
        "sub": "AS-BP2-SubRosa-LE[F3]",
        "merc": "AS-Mercury[F8]",
        "holo": "AS-HolocorpRedux-LE",
        "proto": "AS-ABP-Protocore-v2",
        "ins": "AS-Insurrection-LE-V3",
        "over": "AS-Overgrown-v3c-night",
        "can": "AS-TheCanyon-LE-v4",
        "ind": "AS-Industrial-v1c",
        "rank": "DM-Rankin-ME-2023-b3",
        "iro": "DM-DE-Ironic-FE",
        "rough": "DM-1on1-Roughinery-FE",
        "lea": "DM-1on1-Lea_ESWC2k5-SE",
        "rev": "DM-1on1-Reverse",
        "aero": "DM-1on1-Aerowalk",
        "back": "DM-1on1-Backspace-FE",
        "sat": "DM-Sateca-SE",
        "camp": "DM-Campgrounds2004-G1E",
        "era": "DM-EraseV2",        
        "trop": "AS-Tropical-v2"
    }

    for key, replacement in replacements.items():
        value = value.replace(key, replacement)

    return value

def update_json(file_path, field, value):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

        if field != 'p':
            value = perform_replacements(value)

        if field == 'p':
            data['blocks'][0]['players'] = value
        elif field == 's':
            data['blocks'][0]['series_score'] = value
        elif field == 'bo':
            data['blocks'][0]['bo'] = value
        elif field == 'm1':
            data['blocks'][0]['map1results'] = value
        elif field == 'm2':
            data['blocks'][0]['map2results'] = value
        elif field == 'm3':
            data['blocks'][0]['map3results'] = value
        elif field == 'm4':
            data['blocks'][0]['map4results'] = value
        elif field == 'm5':
            data['blocks'][0]['map5results'] = value
        elif field == 'm6':
            data['blocks'][0]['map6results'] = value            
        elif field == 'm':
            digit, map_name = value.split(' ', 1)
            match_info_template = "Map %s: %s" % (digit, map_name)
            data['blocks'][0]['match_info'] = match_info_template

    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def reset_json(file_path):

    # Get player names and score
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        bo = data['blocks'][0]['bo']

    reset_data = {
        "blocks": [{
            "match_info": " ",
            "players": " ",
            "bo": bo,
            "series_score": "0:0",
            "map1results": " ",
            "map2results": " ",
            "map3results": " ",                        
            "map4results": " ",
            "map5results": " ",
            "map6results": " "
        }]
    }

    with open(file_path, 'w') as json_file:
        json.dump(reset_data, json_file, indent=2)


if __name__ == "__main__":
    json_file_path = 'data.json'  # Update with your actual JSON file path
    
    while True:
        command = input()

        if command == 'exit':
            break

        parts = command.split(' ', 1)
        if len(parts) > 1:
            command, args = parts
            command = command.lower()
        else:
            args = 'NAN'

        if command in ['p', 's', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm', "bo"]:
            if args != 'NAN':
                value = args
                update_json(json_file_path, command, value)
                print(f"{command} field updated.")
        elif command == 'reset':
            reset_json(json_file_path)
            print("JSON file reset.")
        else:
            print("Invalid command. Please enter a valid command.")

    print("Application closed.")
