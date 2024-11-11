from pyzotero import zotero


zot = zotero.Zotero('5894485', 'user', 'UTmEMA7P6HECg5UIgD90e3cH')


# Fetch all tags
tags = zot.tags()

# Print each tag
for tag in tags:
    modified_tag = tag.replace(' ', '_').replace('-', '_').lower()
    print(modified_tag)