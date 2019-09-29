from pprint import pprint as pp
import json as j

punctDict = {'space': 
{
	'replaceWith': 'U+0020',
	'variants': ['U+0009', 'U+00A0', 'U+2000', 'U+2001', 'U+2002', 'U+2003', 'U+2004', 'U+2005', 'U+2006', 'U+2007', 'U+2008', 'U+2009', 'U+200A', 'U+202F', 'U+205F', 'U+3000', 'U+200B', 'U+200C', 'U+200D', 'U+2060', 'U+FEFF']
},

'comma': 
{
	'__comment': '-- 002C is only replaced if  adjacent to foreign text',
	'replaceWith': 'U+FF0C',
	'variants': ['U+002C', 'U+FE10', 'U+FE50']
},

'listComma': 
{
	'__comment': '-- In Japanese, U+3001 is used as a comma instead.',
	'replaceWith': 'U+3001',
	'variants': ['U+FE11', 'U+FE51', 'U+FF64']
},

'interpunct':
{
	'__comment': '''-- U+2022 is the bullet point, it is only replaced if not followed by all whitespaces within a line.
	-- If any of these are followed by all whitespaces within a line, replace with U+2022 instead.
	-- Use NER to determine whether U+002E (half-width western full stop)/U+FF0E (full-width western full stop) should be replaced by a interpunct (U+2027) or a full stop (U+3002).''',
	'replaceWith': 'U+2027',
	'variants': ['U+00B7', 'U+0387', 'U+05BC', 'U+16EB', 'U+2022', 'U+2219', 'U+22C5', 'U+2981', 'U+FF0E', 'U+30FB', 'U+FF65', 'U+10101']
},

'fullStop':
{
	'__comment': '-- cf. \'interpunct\'',
	'replaceWith': 'U+3002',
	'variants': ['U+FE12', 'U+FF61']
}
}

pp(punctDict)
l = j.dumps(punctDict)
with open('punct_info.json', 'w') as x:
    x.write(l)