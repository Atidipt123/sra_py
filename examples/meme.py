"""
Example

A random meme.

"""

import sra_py

meme = sra_py.meme() # meme() returns a Meme object. Read the docs for more info

print(f'Caption: {meme.caption}\nImage URL: {meme.image_url}\nCategory: {meme.category}')
