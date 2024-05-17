### IMPORTANT: This overlay was made for personal use and is intended for dual PC (streaming + gaming) setup and is provided as is.


## Match info overlay for BO3-7 series

This is a hacky solution I made for streaming UT2004 cups and consists of three parts: 
- HTML page for OBS Browser source to display data on stream
- json file to store data
- python script that lets you update the data with a couple of quick commands

This solution lets me update the current series score and map results on the fly and without looking up map names or anything. You don't need to reload the source or anything after updating data, overlay will update automatically in a couple of seconds.

Overlay data consists of 4 updatable main components (white text below), each updated with a separate command:
![image](https://github.com/Aryss/MatchInfoOverlay/assets/7546239/9512a390-a940-40e8-b446-a2b6877a53fc)

- **Match:** players/teams. This one requires the most typing and is updated at the start of the series.
- **Score:** first part of the 2nd string
- **Current Map:** rest of the 2nd string
- **Previous results:** lines 3 and below

This was created and used with OBS in mind (I used on versions 30-30.1.1 64-bit ) and only on Windows. I assume if you stream and play on Linux, you'll probably be able to figure out what else needs to be done for this to run.


### Requirements

- Python 3.8 installed
- OBS v30.1+


### Installation

1. Download and extract to the folder of your choice, e.g. I just keep it in the same folder as my other UT scene stuff. All 3 files must be in the same folder. Also, note that HTML file won't work in any regular browser, only in OBS.

2. Add a Browser source to your OBS scene, set it to use a local file, and point to **match_info.html**.

3. Set scene width to 600 and width to 300 (for 1920x1080 scene), and change the custom CSS to
```css 
body { background-color: rgb(0,0,0,0); overflow: hidden; }
```


### Updating overlay

Run update.py script and use following commands to update the overlay:

- **bo** - updates the "(BO**X**)" section to denote how many matches the series may have. Syntax: ```bo X``` e.g. ```bo 5``` 
- **p** - updates the players/teams info. Syntax: ```p [player vs player]``` e.g. ```p Player A vs Player B```
- **s** - updates the score. Syntax: ```s [score as text]``` e.g. ```s 0:2```
- **m** - updates the current match information. Syntax: ```p X [map name]``` where X is the number of the current map in the series and has to be a single digit. e.g. ```m 2 DM-DE-Ironic-FE```
- **m1** to **m6** - adds the results of a specific match. Syntax: ```m1 [map and score]``` e.g. ```m1 DM-DE-Ironic-FE, 14:15 OT```

Commands **m**, and **"m1"** to **m6** support short map names that you can define yourself (see **Customization** section below), e.g. instead of typing out ```m1 DM-DE-Ironic-FE, 14:15 OT``` all I need to type is ```m1 iro, 14:15 OT``` and the script will handle the replacement

Between series you can reset the overlay using the **reset** command - this will reset the score to "0:0" and will empty all other values, except series length.

If you mistyped something and need to update a field with a new value without resetting it just run the command again with corrected input. As with console up arrow is your friend.
If you need to manually empty a field (most commonly needed with m1-m6), just use the command with a space in quotes, e.g. ``` m1 " "```



### Recommendations

- The overlay's layout was made with the intention of placing it on the left side of the screen. If you want to change it to the right side, you'll need to dig into HTML/CSS yourself.
- If you stream UT2004 I recommend the following position to avoid overlap with HUD or killfeed (right-click your browser source and select Edit Transform for quick edit):
```
Position: 0px / 608px
Positional Alignment: Top Left
Bounding Box Type: No bounds
```
- Set up a hotkey to hide the source (File > Settings > Hotkeys), since overlay in this position will partially obscure UTComp accuracy stats. Just find your new source in the list and provide the same combination for both Hide and Show options. Also, make sure you have Hotkey behavior set to **Never disable hotkeys** under Settings > Advanced.


### Customization

**HTML:**

To change the font and the highlight color of "Match:" and "Score:" at the start of the 1st and 2nd line you can update the CSS style at the start of the HTML file or override those in OBS custom CSS.
Overall text style is defined in **body**, highlight color in **.highlight** class. I recommend keeping the text shadow so that the text can be legible regardless of the background.




**Quick map codes:**

You can add or modify the quick map codes by updating the code/full name list in the function at the beginning of the Python script:
```python
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
```






