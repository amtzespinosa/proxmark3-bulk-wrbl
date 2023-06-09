![Banner](/img/banner.png)

![proxmark3](https://img.shields.io/badge/proxmark3-Easy-lightgrey) ![language](https://img.shields.io/badge/language-Python-blue)

Writing blocks with a Proxmark3 Easy can become an exhausting task when you need to write several blocks and the built-in function for restoring fails.

By writing blocks I mean restoring the dump of an already cracked card into the same card after modification. For example vending purse cards, transport cards, etc...

To use this script you just need to modify the parameters inside the list of dictionaries. Just make sure to match the data you want to write, the block key (usually is key A of the sector where the block belongs) and the block number. This might be tedious but you'll have to do it once if you aim to use that same card over and over again and restore it.

To add blocks just copy, paste and modify:

    {'block_data': '11223344556677881122334455667788', 'key': 'FFFFFFFFFFFF', 'block_number': 16}

> **Note:** Don't forget the comma after each element of the list except the last element. Seems obvious but better remind it!

To run the script once it's all ready:

    sudo python3 bulk_wrbl.py
    
And that's it! Hope this help someone!
