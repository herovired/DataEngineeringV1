## Strings

### Class Excercise [source](https://www.geeksforgeeks.org/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/) (Try to solve on your own)

- Input: welcome2ourcountry34
- Output: True

- Input: stringwithoutnum
- Output: False

- Hints: Look at the output of dir() for any string object and find out the methods which can help in finding which element is a string and which is a number

### Class Demonstration [Common Programming Interview problems](https://www.geeksforgeeks.org/python-uppercase-half-string/)
- input : test_str = dino
- Output : diNO
- Explanation : Latter half of string is uppercased.

- Input : test_str = apples
- Output : appLES
- Explanation : Latter half of string is uppercased.

## Lists

```python
amazon_review = '''
What can I say!
SIMPLY SPECTACULAR.
PUBG - smooth +90 FPS
Smashing all the bench marks by some margin (140%~~)
4 SPEAKERS are like home theatre.
Battery backup is excellent
Could have been better than 20 wts charger

I will keep u guys posted...stay tuned

'''
```
Q1. Count the number of sentences in the review

Understand what new line, line feed and carraige return is: **[reading](https://www.loginradius.com/blog/async/eol-end-of-line-or-newline-characters/)**

Q2 Find out how many words (approximately, consider "say!" as one word) are there in each sentence?

```python
dinkar = '''
वर्षों तक वन में घूम-घूम,
बाधा-विघ्नों को चूम-चूम,
सह धूप-घाम, पानी-पत्थर,
पांडव आये कुछ और निखर।
सौभाग्य न सब दिन सोता है,
देखें, आगे क्या होता है।

मैत्री की राह बताने को,
सबको सुमार्ग पर लाने को,
दुर्योधन को समझाने को,
भीषण विध्वंस बचाने को,
भगवान् हस्तिनापुर आये,
पांडव का संदेशा लाये।

‘दो न्याय अगर तो आधा दो,
पर, इसमें भी यदि बाधा हो,
तो दे दो केवल पाँच ग्राम,
रक्खो अपनी धरती तमाम।
हम वहीं खुशी से खायेंगे,
परिजन पर असि न उठायेंगे!

दुर्योधन वह भी दे ना सका,
आशीष समाज की ले न सका,
उलटे, हरि को बाँधने चला,
जो था असाध्य, साधने चला।
जब नाश मनुज पर छाता है,
पहले विवेक मर जाता है।

हरि ने भीषण हुंकार किया,
अपना स्वरूप-विस्तार किया,
डगमग-डगमग दिग्गज डोले,
भगवान् कुपित होकर बोले-
‘जंजीर बढ़ा कर साध मुझे,
हाँ, हाँ दुर्योधन! बाँध मुझे।

यह देख, गगन मुझमें लय है,
यह देख, पवन मुझमें लय है,
मुझमें विलीन झंकार सकल,
मुझमें लय है संसार सकल।
अमरत्व फूलता है मुझमें,
संहार झूलता है मुझमें।
'''
```

Q1. Programmatically find out how many paras/अनुच्छेद are there in the poem?
Q2. Count the number of words in a paragraph and each sentence

## Tuples

### Class Excercise (Traversing tuples and using set operations)
```python
import pickle ## ignore this for the while
with open("../data/ner_dataset_list","rb") as f:
    ner_data = pickle.load(f)
```

Q1. Use your knowledge about lists and tuples to extract all the entries that have been labelled as GPE

Q2. Find the number of unique GPES in the data. Use the idea of sets. Also find out the the number of duplicated entries.

## Dictionaries

```python
ghalib = [
'''
It’s only my heart, not unfeeling stone,
so why be dismayed when it throbs with pain?
It was made to suffer ten thousand darts;
why let one more torment impede us?
''',

'''
The miracle of your absence
is that I found myself endlessly searching for you.
''',

'''
On the subject of mystic philosophy, Ghalib,
your words might have struck us as deeply profound
and we might have pronounced you a saint ...
Yes, if only we hadn't found
you drunk
as a skunk!
''',
    
'''
Not the blossomings of songs nor the adornments of music:
I am the voice of my own heart breaking.
You toy with your long, dark curls
while I remain captive to my dark, pensive thoughts.
We congratulate ourselves that we two are different:
that this weakness has not burdened us both with inchoate grief.
Now you are here, and I find myself bowing—
as if sadness is a blessing, and longing a sacrament.
I am a fragment of sound rebounding;
you are the walls impounding my echoes.
''',
    
'''
All your life, O Ghalib,
You kept repeating the same mistake:
Your face was dirty
But you were obsessed with cleaning the mirror!
'''
]
```
Q1. Count the number of times each word appears in the above couplet

Q1 Use the ner_data and and organize the data in the following manner in a dictionary:

```json
{
    "PERSON":['Pierre'...],
    "ORGANIZATION":['Boeing'.....],
    "GPE":['DUTCH'.....],
    "LOCATION":['Missisipi'.....]
}

```
You can ignore to handle the cases where a Named Entity is contigously many words long, e.g. for New York, you can treat New and York as separate words.
