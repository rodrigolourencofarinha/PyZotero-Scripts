from pyzotero import zotero

zot = zotero.Zotero('5894485', 'user', 'UTmEMA7P6HECg5UIgD90e3cH')

# Fetch all items with tags
items = zot.everything(zot.top())

print(f"Fetched {len(items)} items.")

# Loop through each item and modify the tags
for item in items:
    if 'tags' in item['data']:
        modified_tags = []
        for tag in item['data']['tags']:
            # Modify the tag: replace spaces with underscores and convert to lowercase
            modified_tag = tag['tag'].replace(' ', '_').replace('-', '_').lower()
            modified_tags.append({'tag': modified_tag})
        
        # Update the item's tags with the modified versions
        item['data']['tags'] = modified_tags
        # Update the item in Zotero
        zot.update_item(item)
        print(f"Updated tags for item: {item['key']}")