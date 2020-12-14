import wikipedia

#show first 2 lines from wiki page
result = wikipedia.summary('Israel',sentences=2)
print(result)

#show 10 instances of the word "israel"
result = wikipedia.search('Israel',results=10)
print(result)

#change the language of the wiki page
wikipedia.set_lang('he')
result = wikipedia.summary('Israel',sentences=4)
print(result)


