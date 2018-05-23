items = [{'name':'Piano'}, {'name':'Chair'}]
name = 'Piano'
item = next(filter(lambda x: x['name'] == name, items), None)

# Filter: filter creates a list of elements for which a function returns true
# Next: retrieves next item from the iterator

print(item)
