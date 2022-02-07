# Messenger graphs & statistics

![Version](https://img.shields.io/badge/python-3.9-blue)
![GitHub issues](https://img.shields.io/github/issues/Byczax/messenger_graphs_statistics)
![GitHub Repo stars](https://img.shields.io/github/stars/Byczax/messenger_graphs_statistics?style=social)

## Description

This code is used with data downloaded from facebook to generate statistics in form of graphs.

## Usage

### 1.Download data

Download conversation data from [**here**](https://www.facebook.com/dyi/?referrer=yfi_settings).

Data format needs to be in **JSON**.
For smaller file (and faster request process) select **low quality** media if you don't want media from groups for personal use (photos, videos).

### 2.Conversion

1. Process this file(s) with `fix_stupid_facebook_unicode_encoding.py` in console.
(write `fix_stupid_facebook_unicode_encoding.py` without argument for help)

1. Insert all generated files into **1 folder** in the same directory as folder `src`. (name folder as you like and write it's name in `main.py`)

### 3.Creating data

1. Process fixed file(s) with `src/main.py` in console.
(write `src/main.py` without argument for help)

2. Good work! now you have stats for your messenger conversations.

### Automating generation

If you have more groups that you want to get statistics, then:

1. Create folder *messages* and inside create **1 folder** for each of your group files
2. Run script `fix_stupid_files.sh`
3. Run script `generate_all.sh`
4. voilà, now you have folder `img` with all your charts with stats.

Example file structure

```bash
.
└── messages
     ├── group1
     ├── group2 
     ├── group3
     └── group4 
```

### 4.Available data

Right now i created modules for:

1. All sended messages
2. All reactions given to others
3. All received reactions
4. Counting specific reaction
5. Counting specific word
6. Counting all emoji used in conversation

### TODO

- Count sended images, gifs
- Count sended files
- Count deleted messages
- Count sended links to websites
- Count Added and **removed** members

### Facebook stupid file documentation [WIP]

**Message file construction:**

- participants
  - name
- messages
  - sender_name
  - timestamp_ms
  - type
  - is_unsent

**Message types:**

- Call
  - call duration
- Generic
  - photos
    - uri
    - creation_timestamp
  - videos
    - uri
    - creation_timestamp
    - thumbnail
      - uri
  - gifs
  - reactions
    - reaction
    - actor
- Share
- Subscribe
  - Users
    - name
- Unsubscribe

"Weird things":

- Pinging is in Generic (@someone)
- when someone join call then it's Generic (someone joined video chat)
