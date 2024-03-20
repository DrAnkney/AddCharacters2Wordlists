## Purpose
This bit of code will take your core wordlist and add numbers or special characters to the front or end of the words for a bigger wordlist. It works just as masking and incrementing would in hashcat or john the ripper but much faster. (No, I didn't measure times, the time difference was "this is killing me" with hashcat vs "oh it's already done" with this script.) There are two time savers: the code creates the list very quickly, and then hashcat/john run faster on a straight wordlist with no masking.

## Usage
You don't have to worry about entering the arguments just so. Just run the script
```
pyhton3 addchars.py
```
and it will ask you for the wordlist file, what you want to add (numbers, special characters, both), how many you want to add, and whether you want to append them to the end or prepend them at the front. Then it will tell you where to find your resulting new wordlist.

## Hints
If you need characters both appended and prepended, just run the script on your core wordlist and then run the script again on your new wordlist. It's fast.

If you plan to use toggles or leetspeak on your core wordlist, do that **before** you run this script.

## Cost
You can go crazy with this code, and your wordlists can get enormous and eat up all of your memory. I am using this for CTFs, and what I have found is that I need to create a new list, try it, and throw it out (and keep track of what I've tried if I wasn't successful so I don't forget and try it again). This really does save enough time that it's worth trying and dumping new lists. Just keep your core list somewhere safe if it's a good one!
