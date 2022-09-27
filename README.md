# MHR-ArmorID-Replacer

A Python script that replaces the armor IDs of modded armor with any other wanted armor ID in Monster Hunter Rise for PC. 

It is highly recommended, that the mod is modified BEFORE it is placed in the installation directory of Monster Hunter Rise.

# How to use:
There are 3 variables in the script, that need to be adjusted:
- before (String)
- after (String)
- rootFolder (String)

### **before**:
A String value, that contains the Armor ID of the Armor the mod currently uses

*Example:* before = '200'

### **after**:
A String value, that contains the Armor ID of the Armor you want to replace the ID from "*before*" with.

*Example:* after = '200'

### **rootFolder**:
A String value containing the full path to the mods directory.
The path uses "/" (forward slash) as seperators. The Path ends without a "/" forward slash).

*Example:* 'C:/path-to-modfolder/Mod-Folder'

# More Information:
There is a list of armor IDs for each armor in Monster Hunter Rise on GitHub if you follow this Link: 
https://github.com/mhvuze/MonsterHunterRiseModding/wiki/Armor-IDs