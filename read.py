#!/usr/bin/python
# -*- coding: utf-8 -*-

# şimdi unicode

# Copyright 2012 Grantcox, https://github.com/grantcox
# Copyright 2015 Godfried Borremans

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


    
import codecs
from datetime import datetime
import os
import struct
import sys

#logfile = codecs.open('log.txt', encoding='utf-8', mode='a')
#def log(s):
#    s = unicode(s)
#    print s.encode('ascii', 'ignore')
#    logfile.write('\n' + s)
#log('---- ' + str(datetime.now()) + ' -----------------')

# Python Tuple Lists with language codes (as of ISO 639-1) and country codes (as of ISO 3166)
# https://gist.github.com/alexex/4073388
# alexex / gist:4073388
# Created on 14 Nov 2012
# 
#    Code
#    Revisions 1
#     Stars 4

countries_languages = [
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('af', 'Afrikaans'),
    ('ak', 'Akan'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('an', 'Aragonese'),
    ('hy', 'Armenian'),
    ('as', 'Assamese'),
    ('av', 'Avaric'),
    ('ae', 'Avestan'),
    ('ay', 'Aymara'),
    ('az', 'Azerbaijani'),
    ('ba', 'Bashkir'),
    ('bm', 'Bambara'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bh', 'Bihari languages'),
    ('bi', 'Bislama'),
    ('bo', 'Tibetan'),
    ('bs', 'Bosnian'),
    ('br', 'Breton'),
    ('bg', 'Bulgarian'),
    ('my', 'Burmese'),
    ('ca', 'Catalan; Valencian'),
    ('cs', 'Czech'),
    ('ch', 'Chamorro'),
    ('ce', 'Chechen'),
    ('zh', 'Chinese'),
    ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
    ('cv', 'Chuvash'),
    ('kw', 'Cornish'),
    ('co', 'Corsican'),
    ('cr', 'Cree'),
    ('cy', 'Welsh'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dv', 'Divehi; Dhivehi; Maldivian'),
    ('nl', 'Dutch; Flemish'),
    ('dz', 'Dzongkha'),
    ('el', 'Greek, Modern (1453-)'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('eu', 'Basque'),
    ('ee', 'Ewe'),
    ('fo', 'Faroese'),
    ('fa', 'Persian'),
    ('fj', 'Fijian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fr', 'French'),
    ('fy', 'Western Frisian'),
    ('ff', 'Fulah'),
    ('Ga', 'Georgian'),
    ('de', 'German'),
    ('gd', 'Gaelic; Scottish Gaelic'),
    ('ga', 'Irish'),
    ('gl', 'Galician'),
    ('gv', 'Manx'),
    ('el', 'Greek, Modern (1453-)'),
    ('gn', 'Guarani'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian; Haitian Creole'),
    ('ha', 'Hausa'),
    ('he', 'Hebrew'),
    ('hz', 'Herero'),
    ('hi', 'Hindi'),
    ('ho', 'Hiri Motu'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('hy', 'Armenian'),
    ('ig', 'Igbo'),
    ('is', 'Icelandic'),
    ('io', 'Ido'),
    ('ii', 'Sichuan Yi; Nuosu'),
    ('iu', 'Inuktitut'),
    ('ie', 'Interlingue; Occidental'),
    ('ia', 'Interlingua (International Auxiliary Language Association)'),
    ('id', 'Indonesian'),
    ('ik', 'Inupiaq'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('jv', 'Javanese'),
    ('ja', 'Japanese'),
    ('kl', 'Kalaallisut; Greenlandic'),
    ('kn', 'Kannada'),
    ('ks', 'Kashmiri'),
    ('ka', 'Georgian'),
    ('kr', 'Kanuri'),
    ('kk', 'Kazakh'),
    ('km', 'Central Khmer'),
    ('ki', 'Kikuyu; Gikuyu'),
    ('rw', 'Kinyarwanda'),
    ('ky', 'Kirghiz; Kyrgyz'),
    ('kv', 'Komi'),
    ('kg', 'Kongo'),
    ('ko', 'Korean'),
    ('kj', 'Kuanyama; Kwanyama'),
    ('ku', 'Kurdish'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('li', 'Limburgan; Limburger; Limburgish'),
    ('ln', 'Lingala'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish; Letzeburgesch'),
    ('lu', 'Luba-Katanga'),
    ('lg', 'Ganda'),
    ('mk', 'Macedonian'),
    ('mh', 'Marshallese'),
    ('ml', 'Malayalam'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('Mi', 'Micmac'),
    ('mk', 'Macedonian'),
    ('mg', 'Malagasy'),
    ('mt', 'Maltese'),
    ('mn', 'Mongolian'),
    ('mi', 'Maori'),
    ('ms', 'Malay'),
    ('my', 'Burmese'),
    ('na', 'Nauru'),
    ('nv', 'Navajo; Navaho'),
    ('nr', 'Ndebele, South; South Ndebele'),
    ('nd', 'Ndebele, North; North Ndebele'),
    ('ng', 'Ndonga'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch; Flemish'),
    ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
    ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
    ('no', 'Norwegian'),
    ('oc', 'Occitan (post 1500)'),
    ('oj', 'Ojibwa'),
    ('or', 'Oriya'),
    ('om', 'Oromo'),
    ('os', 'Ossetian; Ossetic'),
    ('pa', 'Panjabi; Punjabi'),
    ('fa', 'Persian'),
    ('pi', 'Pali'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ps', 'Pushto; Pashto'),
    ('qu', 'Quechua'),
    ('rm', 'Romansh'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('rn', 'Rundi'),
    ('ru', 'Russian'),
    ('sg', 'Sango'),
    ('sa', 'Sanskrit'),
    ('si', 'Sinhala; Sinhalese'),
    ('sk', 'Slovak'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('se', 'Northern Sami'),
    ('sm', 'Samoan'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('so', 'Somali'),
    ('st', 'Sotho, Southern'),
    ('es', 'Spanish; Castilian'),
    ('sq', 'Albanian'),
    ('sc', 'Sardinian'),
    ('sr', 'Serbian'),
    ('ss', 'Swati'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('ty', 'Tahitian'),
    ('ta', 'Tamil'),
    ('tt', 'Tatar'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('tl', 'Tagalog'),
    ('th', 'Thai'),
    ('bo', 'Tibetan'),
    ('ti', 'Tigrinya'),
    ('to', 'Tonga (Tonga Islands)'),
    ('tn', 'Tswana'),
    ('ts', 'Tsonga'),
    ('tk', 'Turkmen'),
    ('tr', 'Turkish'),
    ('tw', 'Twi'),
    ('ug', 'Uighur; Uyghur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('ve', 'Venda'),
    ('vi', 'Vietnamese'),
    ('vo', 'Volapük'),
    ('cy', 'Welsh'),
    ('wa', 'Walloon'),
    ('wo', 'Wolof'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('za', 'Zhuang; Chuang'),
    ('zh', 'Chinese'),
    ('zu', 'Zulu')
]

o = dict(countries_languages)

languages_countries = {v.lower(): k.lower() for k, v in o.items()}
 
def get_iso_639_1(iso_3166):
  # TODO add error handling here
  print iso_3166.lower(), languages_countries[iso_3166.lower()]
  return languages_countries[iso_3166.lower()]

class Parser(object):
    struct_short = struct.Struct('<H')

    def __init__(self, filename):
        self.filedata = None
        if filename != '':
            try:
                f = open(filename, 'rb')
                self.filedata = f.read()
                f.close()
            
            except IOError as e:
                pass
        
    def read(self, fmt, offset):
        if self.filedata is None:
            return None
        read = struct.unpack_from('<' + fmt, self.filedata, offset)
        if len(read) == 1:
            return read[0]
        return read
    
    def string(self, offset):
        if self.filedata is None:
            return None
        s = u''
        if offset > 0:
            length = self.read('H', offset)
            for i in range(length):
                raw = self.read('H', offset + i*2 +2)
                char = raw ^ 0x7E
                s = s + unichr(char)
        return s

    def plain_fixed_string(self, offset):
        if self.filedata is None:
            return None
        plain_bytes = struct.unpack_from('<ssssssssssssssssssssssss', self.filedata, offset)
        plain_string = ''.join(plain_bytes).strip('\0x0')
        return plain_string

    def blob(self, offset, filename=''):
        length = self.read('L', offset)
        data = self.filedata[offset+8 : offset+length+8]
        
        return Blob(data, filename)

class Blob(object):
    def __init__(self, data, filename=''):
        self.data = data
        self.filename = filename

    def write(self, filename=None):
        if filename is None:
            filename = self.filename
        if filename is not None and filename != '':
            f = open(filename, 'wb')
            f.write(self.data)
            f.close()
        
class Card(object):
    number = None
    native_title = ''
    native_subtitle = ''
    foreign_title = ''
    foreign_subtitle = ''
    native_alt_answer = ''
    foreign_alt_answer = ''
    foreign_translit = ''
    native_tooltip = ''
    foreign_audio = None
    native_audio = None
    image = None

    def __init__(self, parser, data_pointer=0, card_attributes=0):
        self.data = {}
        attributes = [
            ['native_title', 4],
            ['native_subtitle', 8],
            ['foreign_title', 16],
            ['foreign_subtitle', 32],
            ['native_alt_answer', 64],
            ['foreign_alt_answer', 128],
            ['foreign_translit', 256],
            ['native_tooltip', 512],
            ['foreign_audio', 1024],
            ['native_audio', 2048],
            ['image', 4096]
        ]
        
        self.number = parser.read('L', data_pointer +4)
        data_pointer = data_pointer + 8
        for attr in attributes:
            if card_attributes & attr[1]:
                data_address = parser.read('L', data_pointer)
                data = None
                
                if attr[0] == 'foreign_audio':
                    data = parser.blob(data_address)
                elif attr[0] == 'native_audio':
                    data = parser.blob(data_address)
                elif attr[0] == 'image':
                    data = parser.blob(data_address)
                else:
                    data = parser.string(data_address)
                
                setattr(self, attr[0], data)
                
                data_pointer = data_pointer + 4

        self.valid = True

    def html(self, tofolder):
        def wrap(content, prefix, suffix):
            if content == None or content == '':
                return ''
            return unicode(prefix) + unicode(content) + unicode(suffix)

        src = ''
        cardnum = str(self.number)
        write = {
            'number' : cardnum,
            'native_title' : self.native_title,
            'native_subtitle' : wrap(self.native_subtitle, '<p>', '</p>\n'),
            'foreign_title' : self.foreign_title,
            'foreign_subtitle' : wrap(self.foreign_subtitle, '<p>', '</p>\n'),
            'foreign_translit' : '',
            'native_alt_answer' : wrap(self.native_alt_answer, '<p>Also: ', '</p>\n'),
            'foreign_alt_answer' : wrap(self.foreign_alt_answer, '<p>Also: ', '</p>\n'),
            'native_tooltip' : wrap(self.native_tooltip, '<p class="tooltip">', '</p>\n'),
            'foreign_audio' : '',
            'native_audio' : '',
            'image' : ''
        }
        
        if isinstance(self.foreign_audio, Blob):
            fn = 'card' + cardnum + '_foreign.ogg'
            self.foreign_audio.write(os.path.join(tofolder, fn))
            write['foreign_audio'] = '<a class="audio" href="' + fn + '">(o)</a>'
            
        if isinstance(self.native_audio, Blob):
            fn = 'card' + cardnum + '_native.ogg'
            self.native_audio.write(os.path.join(tofolder, fn))
            write['native_audio'] = '<a class="audio" href="' + fn + '">(o)</a>'
            
        if isinstance(self.image, Blob):
            fn = 'card' + cardnum + '_image.jpg'
            self.image.write(os.path.join(tofolder, fn))
            write['image'] = '<img class="image" src="' + fn + '"/>'
        
        src    = '\
    <div class="card">\n\
        <p class="num">#%(number)s</p>\n\
        %(image)s\
        <h1>%(foreign_title)s%(foreign_audio)s</h1>\n\
        %(foreign_subtitle)s\
        %(foreign_alt_answer)s\
        %(native_tooltip)s\
        \
        <h2>%(native_title)s%(native_audio)s</h2>\n\
        %(native_subtitle)s\n\
        %(native_alt_answer)s\n\
    </div>\n\
                \n' %write
        
        return src
        
    def kvtml(self, tofolder):
        def wrap(content, prefix, suffix):
            if content == None or content == '':
                return ''
            return unicode(prefix) + unicode(content) + unicode(suffix)

        src = ''
        cardnum = str(self.number)
        write = {
            'number' : cardnum,
            'native_title' : self.native_title,
            'native_subtitle' : wrap(self.native_subtitle, '<p>', '</p>\n'),
            'foreign_title' : self.foreign_title,
            'foreign_subtitle' : wrap(self.foreign_subtitle, '<p>', '</p>\n'),
            'foreign_translit' : '',
            'native_alt_answer' : wrap(self.native_alt_answer, '<p>Also: ', '</p>\n'),
            'foreign_alt_answer' : wrap(self.foreign_alt_answer, '<p>Also: ', '</p>\n'),
            'native_tooltip' : wrap(self.native_tooltip, '<p class="tooltip">', '</p>\n'),
            'foreign_audio' : '',
            'native_audio' : '',
            'image' : ''
        }
        
        if isinstance(self.foreign_audio, Blob):
            fn = 'card' + cardnum + '_foreign.ogg'
            self.foreign_audio.write(os.path.join(tofolder, fn))
            write['foreign_audio'] = fn
            
        if isinstance(self.native_audio, Blob):
            fn = 'card' + cardnum + '_native.ogg'
            self.native_audio.write(os.path.join(tofolder, fn))
            write['native_audio'] = fn
            
        if isinstance(self.image, Blob):
            fn = 'card' + cardnum + '_image.jpg'
            self.image.write(os.path.join(tofolder, fn))
            write['image'] = fn
        
        src    = '\
    <div class="card">\n\
        <p class="num">#%(number)s</p>\n\
        %(image)s\
        <h1>%(foreign_title)s%(foreign_audio)s</h1>\n\
        %(foreign_subtitle)s\
        %(foreign_alt_answer)s\
        %(native_tooltip)s\
        \
        <h2>%(native_title)s%(native_audio)s</h2>\n\
        %(native_subtitle)s\n\
        %(native_alt_answer)s\n\
    </div>\n\
                \n' %write
                
        kvtml_src = '\
    <entry id="%(number)s">\n\
      <translation id="0">\n\
        <text>%(foreign_title)s</text>\n\
        <image>%(image)s</image>\n\
        <sound>%(foreign_audio)s</sound>\n\
      </translation>\n\
      <translation id="1">\n\
        <text>%(native_title)s</text>\n\
        <sound>%(native_audio)s</sound>\n\
      </translation>\n\
    </entry>\n\
                \n' %write
        
        return kvtml_src
      
class Deck(object):
    title = ''
    description = ''
    native_language = ''
    foreign_language = ''
    native_locale = ''
    foreign_locale = ''    
    copyright = ''
    copyright_url = ''
    creation_date = ''
    app_creator_name = ''
    
    def __init__(self, filename):
        self.valid = False
        self.cards = []
        self.parser = Parser(filename)
        self.parse()

    def parse(self):
        self.valid = False
        self.data = {}
        self.cards = []
        
        caret = None
        # find the initial caret position - this changes between files for some reason - search for the "Cards" string
        for i in range(3):
            addr = 104 + i*4
            if ''.join(self.parser.read('sssss', addr)) == 'Cards':
                caret = addr + 32
                break
        
        if caret is None:
            return
        
        deck_details_pointer = self.parser.read('L', 92)
        card_count = self.parser.read('L', caret +4)
        next_card = self.parser.read('L', caret +16)
        
        # read in all of the deck properties - name, creator, description, copyright etc
        fields = {
            'Name': 'title',
            'Side1Lang': 'native_language',
            'Side2Lang': 'foreign_language',
            'Description': 'description',
            'Copyright': 'copyright',
            'CopyrightURL': 'copyright_url',
            'CreationDate': 'creation_date',
            'AppCreatorName': 'app_creator_name'
        }
        
        while deck_details_pointer != 0:
            detail_label = self.parser.plain_fixed_string(deck_details_pointer + 4)
            if detail_label in fields:
                detail_string = ''
                detail_data = self.parser.read('L', deck_details_pointer + 40)
             
                if detail_label == 'CreationDate':
                    # not a pointer, this is a timestamp
                    creation_date = datetime.fromtimestamp(detail_data)
                    detail_string = creation_date.strftime('%Y %B %d')
                elif detail_label == 'GUID':
                    detail_string = str(detail_data)
                elif detail_label == 'Ordered':
                    detail_string = str(detail_data)
                else:
                    detail_string = self.parser.string(detail_data)
                
                # set this property on the Deck object
                setattr(self, fields[detail_label], detail_string)
                
            # move to the next attribute
            deck_details_pointer = self.parser.read('L', deck_details_pointer)
        
        self.valid = True
        
        # read in all of the cards
        while (next_card != 0):
            next_card, card_num, boundary, card_data_pointer, card_attributes = self.parser.read('LLLLL', next_card)
            card = Card(self.parser, card_data_pointer, card_attributes)
            if card.valid:
                self.cards.append(card)
        
        return self.valid

    def html(self, tofolder):
        if not os.path.isdir(tofolder):
            os.makedirs(tofolder)
        html = '\
<!DOCTYPE html><html lang="en">\
<head><meta charset="utf-8" />\n\
    <title>Deck</title>\n\
    <style type="text/css">\n\
    .card{border:2px solid #999; margin: 30px; padding: 20px; text-align: center;}\
    </style>\n\
</head><body>\n\
    <h1>'+unicode(self.title)+'</h1>\
    <h2>'+unicode(self.native_language)+':'+unicode(self.foreign_language)+'</h2>\
    <p>Description: '+unicode(self.description)+'</p>\
    <p>Copyright: '+unicode(self.copyright)+' '+unicode(self.copyright_url)+'</p>\
    <p>Created with: '+unicode(self.app_creator_name)+' on '+unicode(self.creation_date)+'</p>\
        \n'

        for card in self.cards:
            html = html + card.html(tofolder)
            
        html = html + '</body></html>'
        
        fn = os.path.join(tofolder, 'cards.html')
        f = codecs.open(fn, encoding='utf-8', mode='w')
        f.write(html)
        f.close()
        
    def kvtml(self, tofolder):
        # todo: transliterate xml characters (ampersand etc)
        if not os.path.isdir(tofolder):
            os.makedirs(tofolder)
            
        self.native_locale = get_iso_639_1(unicode(self.native_language))
        self.foreign_locale = get_iso_639_1(unicode(self.foreign_language))
        
        kvtml = '\
<?xml version="1.0" encoding="UTF-8"?>\n\
<!DOCTYPE kvtml PUBLIC "kvtml2.dtd" "http://edu.kde.org/kvtml/kvtml2.dtd">\n\
<kvtml version="2.0">\n\
  <information>\n\
    <generator>'+unicode(self.app_creator_name)+', converted with https://github.com/grantcox/b4u_reader</generator>\n\
    <title>'+unicode(self.title)+'</title>\n\
    <author>Your Name</author>\n\
    <contact>your.emailaddress@example.com</contact>\n\
    <license>'+unicode(self.copyright)+' '+unicode(self.copyright_url)+'</license>\n\
    <comment>'+unicode(self.description)+'</comment>\n\
    <date>'+unicode(self.creation_date)+'</date>\n\
    <category>Languages</category>\n\
  </information>\n\
  <identifiers>\n\
    <identifier id="0">\n\
      <name>'+unicode(self.native_language)+'</name>\n\
      <locale>'+unicode(self.native_locale)+'</locale>\n\
    </identifier>\n\
    <identifier id="1">\n\
      <name>'+unicode(self.foreign_language)+'</name>\n\
      <locale>'+unicode(self.foreign_locale)+'</locale>\n\
    </identifier>\n\
  </identifiers>\n\
  <entries>\
        \n'

        for card in self.cards:
            kvtml = kvtml + card.kvtml(tofolder)
            
        kvtml_footer = '\
          </entries>\n\
        </kvtml>\
        \n'
        
        kvtml = kvtml + kvtml_footer
        
        fn = os.path.join(tofolder, 'cards.kvtml')
        f = codecs.open(fn, encoding='utf-8', mode='w')
        f.write(kvtml)
        f.close()
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print 'Usage: readb4u.py [filename]'
        sys.exit()

    SCRIPT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
    OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output')
    
    d = Deck(sys.argv[1])
    # d.html(OUTPUT_DIR)
    d.kvtml(OUTPUT_DIR)
    # check the output in kvtml with xmllint
 
