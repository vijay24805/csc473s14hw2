# Tutnese
# Author: Vijaya Kumar V

import re

Den= {'b':'bub',
'c':'coch', 
'd':'dud',
'f':'fuf',
'g':'gug',
'h':'hash',
'j':'jug',
'k':'kuck',
'l':'lul',
'm':'mum',
'n':'nun',
'p':'pup',
'q':'quack',
'r':'rur',
's':'sus',
't':'tut',
'v':'vuv',
'w':'wack',
'x':'xux',
'y':'yub',
'z':'zug',
'bb':'squab',
'cc':'squac', 
'dd':'squad',
'ff':'squaf',
'gg':'squag',
'hh':'squah',
'jj':'squaj',
'kk':'squak',
'll':'squal',
'mm':'squam',
'nn':'squan',
'pp':'squap',
'qq':'squaq',
'rr':'squar',
'ss':'squas',
'tt':'squat',
'vv':'squav',
'ww':'squaw',
'xx':'squax',
'yy':'squay',
'zz':'squaz',
}

Ddec= {
'bub':'b',
'coch' : 'c', 
'dud':'d',
'fuf':'f',
'gug':'g',
'hash':'h',
'jug':'j',
'kuck':'k',
'lul':'l',
'mum':'m',
'nun':'n',
'pup':'p',
'quack':'q',
'rur':'r',
'sus':'s',
'tut':'t',
'vuv':'v',
'wack':'w',
'xux':'x',
'yub':'y',
'zug':'z',
'squab':'bb',
'squac':'cc', 
'squad':'dd',
'squaf':'ff',
'squag':'gg',
'squah':'hh',
'squaj':'jj',
'squak':'kk',
'squal':'ll',
'squam':'mm',
'squan':'nn',
'squap':'pp',
'squaq':'qq',
'squar':'rr',
'squas':'ss',
'squat':'tt',
'squav':'vv',
'squaw':'ww',
'squax':'xx',
'squay':'yy',
'squaz':'zz',
}

englpattern = re.compile(r'(.)\1?' , re.IGNORECASE | re.DOTALL)
 
def encode(input):
  
  if re.search(r'\|',input):
    raise Exception('Invalid character "|"')
  else:
    temp = [x.group() for x in englpattern.finditer(input)]
    print temp
    data=''.join(map(lambda x:Den.get(x.lower(),x.lower()),temp))
    print 'check'
    if '\n' in input:
      print 'new line is there'
    if '\n' in data:
      print 'new in data too'
    print data
    return data


def decode(input):
  
  if re.search(r'\|',input):
    raise Exception('Invalid character "|"')
  else:
    pattern = '|'.join(map(re.escape, Ddec))
    temp = re.sub(pattern, lambda m: Ddec[m.group()], input)
    print temp
    return temp



 
