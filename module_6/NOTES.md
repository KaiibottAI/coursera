# Module 6 - Real World Tasks

## Week 2

### Data Serialization

If you have two programs that need to communicate with each other, how do you get that data from one place to another? We're going to talk about two aspects of that problem: what to send, and how to send it.

First, what do you send? When you have a conversation with another person, you don't send thoughts and memories directly between your brains. At least not yet! You first have to convert your thoughts into language, and then transmit that language to another person. They take that language, and convert it back into thoughts. It’s the same with programs running in different places, or at different times.

In a previous course, we took a list of lists in memory and wrote it to disk as a Comma-Separated Value (CSV) file. This is one example of a technique called data serialization. Data serialization is the process of taking an in-memory data structure, like a Python object, and turning it into something that can be stored on disk or transmitted across a network. Later, the file can be read, or the network transmission can be received by another program and turned back into an object again. Turning the serialized object back into an in-memory object is called deserialization.

Data serialization is extremely useful for communicating with web services. A web service's API endpoint takes messages in a specific format, containing specific data. By the end of this module, we'll be sending messages to web services, but for now let's concentrate on how to serialize Python objects into some common formats.

Let's start with the contact information from one of our CSV examples. We'll keep just two entries to keep our examples short, but there's no limit to how long these can be.

```(CSV Example)
name,username,phone,department,role
Sabrina Green,sgreen,802-867-5309,IT Infrastructure,System Administrator
Eli Jones,ejones,684-3481127,IT Infrastructure,IT specialist
```

```(List of Dictionaries)
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": "802-867-5309",
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": "684-348-1127",
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
```

### Data Serialization Formats

```python
import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
```
Using the `json.dump()` function to serialize the `people` object into a JSON file. The contents of the file will looks like this:

```
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  },
]
```

There is also YAML (yet another markup language) that is common to JSON
```python
import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
```
```
- department: IT Infrastructure
  name: Sabrina Green
  phone:
    cell: 802-867-5310
    office: 802-867-5309
  role: Systems Administrator
  username: sgreen
- department: IT Infrastructure
  name: Eli Jones
  phone:
    office: 684-348-1127
  role: IT Specialist
  username: ejones
```


## Week 3

```python
from email.message import EmailMessage

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"
body = """Hey there!
I'm learning to send emails in Python!

"""
message['From'] = sender
message['To'] = recipient
message['Subject'] = "Greetings from {} to {}!".format(sender, recipient)
message.set_content(body)

print(message)
```

### Intro to generating a PDF

Depending on what your automation does, you might want to generate a PDF report at the end, which lets you decide exactly how you want your information to look like.

There's a few tools in Python that let you generate PDFs with the content that you want. Here, we'll learn about one of them: ReportLab. ReportLab has a lot of different features for creating PDF documents. We'll cover just the basics here, and give you pointers for more information at the end.

For our examples, we'll be mostly using the high-level classes and methods in the Page Layout and Typography Using Scripts (PLATYPUS) part of the ReportLab module.

Let's say that I have an awesome collection of fruit, and I want to create a PDF report of all the different kinds of fruit I have! I can easily represent the different kinds of fruit and how much of each I have with a Python dictionary. It might look something like this:

```python
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}
```
Now let's take this information and turn it into a report that we can show off! We're going to use the SimpleDocTemplate class to build our PDF.

```python
from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")
```
The `report` object will create a PDF using the filename `/tmp/report.pdf`
Lets add some content! Title, txt in paragraphs and some charts/images. For that, we use reportlab with `Flowables`. `Flowables` are sort of like chunks of a document that report lab can arrange to make a complete report.

```python
from reportlab.platypus import Paragraph, Space, Table, Image
```

You can make styles on your own, but for simplicity we will use the default provided by the module for these exapmles. The `styles` object now contains a defult 'sample' style. It's like a dictionary of different style settings. If you've ever written HTML, the settings will look familiar.

```python
report_title = Paragraph("A complete inventory of my fruit", styles['h1'])
report.build([report_title])
```

### Making a PDF

```python

```

### Adding Graphics to our PDFs

```python

```