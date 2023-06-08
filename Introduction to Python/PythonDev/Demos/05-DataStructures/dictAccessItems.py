dialcodes = {"us": "+1", "nl": "+31", "no": "+47"}

print("%s" % "us" in dialcodes)          # True
print("%s" % "us" not in dialcodes)      # False

dialcodes["uk"] = "+44"
print(dialcodes["uk"])                   # +44
print(dialcodes.get("fr"))               # None
print(dialcodes.get("fr", "xxx"))        # xxx

del dialcodes["no"]
print(dialcodes.pop("uk"))               # +44
print(dialcodes.pop("uk", "xxx"))        # xxx
print(dialcodes.setdefault("it", "???")) # ???

dialcodes.update({"ca":"+1", "it":"+39"}) 
print(dialcodes)  # {'ca': '+1', 'us': '+1', 'nl': '+31', 'it': '+39'}
