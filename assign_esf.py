import sys
import nltk
import json
import csv
import friends_esf_wn as friends
import esf_list
import vInflection
from nltk.wsd import lesk
from nltk.tokenize import sent_tokenize, word_tokenize

#sec_num = sys.argv[1]
#text = sys.argv[2]

# get the Event Structure Frame type for each verb in a given sentence via word sense disambiguation (mapping the verbs to their proper wordnet synsets)
# input: sentence
# output: esf_type = the list of tuples, (verb_lemma, WordNet_synset, ESF type), for all verbs derived by the function get_esf_type(sentence) in the given sentence
# word sense disambiguation algorithm: lesk algorithm
# example
#   input: 'I want your love.'
#   wsd output: ('want.v.03')
#   esf_type: 'STATE' - this is got from the friends_esf_wn.py file


def lemmatize(word):
    lem = 'none'
    for v in vInflection.infl.keys():
        if word in v:
            lem = vInflection.infl[v][2]
    return lem

def get_esf_type(sentence):
    sent = word_tokenize(sentence)#tokenization
    #print(sent)
    tokens_with_pos = nltk.pos_tag(sent) #part-of-speeach tagging
    print(tokens_with_pos)
    verb_sense_esf = []
    for token in tokens_with_pos:
        if token[1] in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'] and token[0] not in ["'s", "'re"]:
            #print(token[0])
            sense = lesk(sent, token[0], 'v')
            #print("sense: "+str(sense))
            if sense is None: pass
            else:
                sense=str(sense).split('(')[1].split(')')[0]
                sense = sense.split("'")[1].split("'")[0]
                #print(sense)
                vlem = lemmatize(token[0])
                #print(vlem)
                for v in friends.verbs:
                    if v['VERB']== vlem and v['SENSE_NUMBER']==sense:
                        verb_sense_esf.append((vlem, sense, v['ESF_TYPE']))
    return verb_sense_esf


# select the proper event structure frames for the event structure frame types from friends_esf_wn data file.
# input: esf_type = the list of tuples derived by the function get_est_type(sentence)
# used resource: (1) friends_esf_wn = the list of dictionaries each of which is composed of verb, sense_number, esf_type, synonyms, and hypernyms
#                (2) esf_list = the list of pre-defined event structure frames
# output: esf = the list of dictionaries derived by get_esf(esf_type)


def get_esf(esf_type):
    esfs = []
    if esf_type == []: pass
    for et in esf_type:
        #print("et: "+str(et))
        esf = {}
        #print(str(esf))
        #print(type(esf_list.frames))
        for e in esf_list.frames:
            #print(str(e['type']))
            if et[2] == e['type']:
                esf['verb']=et[0]
                esf['wn_synset'] = et[1]
                #print(et[1])
                #print(esf['wn_synset'])
                esf['esf_type'] = et[2]
                esf['subevents'] =e['subevents']
        esfs.append(esf)
        #print(str(esfs))
    return esfs

def get_esfs_with_predicates(esfs):
    predicates = []
    if esfs == []: pass
    for esf in esfs:
        preds = []
        for v in friends.verbs:
            #print(esf['wn_synset'])
            if esf['wn_synset']==v['SENSE_NUMBER']:
                preds.append(esf['verb'])
                preds.extend(v['SYNONYMS'])
                preds.extend(v['HYPERNYMS'])
                preds = list(set(preds))
        for form in esf['subevents']:
            if form['predicate']==[]:
                form['predicate'].extend(preds)
        predicates.append(esf)
    return predicates




f = open('friends_05_eng_script.csv', 'r')
   
rdr = csv.reader(f)
next(rdr)
num = 0
with open('friends_05_eng_script_verb_esf.json', 'w') as make_file:
    for line in rdr:
        if 0 < num:
            event_frames ={}
            sec_num = line[0]
            print("sec_num "+str(sec_num))
            sentence = line[4]
            print("sentence: "+sentence)
            event_frames['sec_num'] = sec_num
            event_frames['sentence'] = sentence
            esf_type_list = get_esf_type(sentence)
            print("esf_type: "+str(esf_type_list))
            event_str_frames = get_esf(esf_type_list)
            esfs_with_predicates = get_esfs_with_predicates(event_str_frames)
            #print(str(esfs_with_predicates))
            event_frames['verb_event_structure_frames']=esfs_with_predicates
            #json_data = json.dumps(esfs_with_predicates)
            #print(json_data)
            json.dump(event_frames, make_file, ensure_ascii=False, indent = 4)
        num=num+1
        
f.close()

"""
#esf_type_list = get_esf_type(text)
#print(esf_type_list)

#esf_list = get_esf(esf_type_list)

#esfs_with_predicates = get_esfs_with_predicates(esf_list) #esfs_with_predicates: dictionary-formed event structure frames of verbs in a given sentence
#print(esfs_with_predicates)



#
#    

"""
"""
# make event structure frames more understandable
f = open('esf_display.py', 'w')
f.write('input_sentence = '+text+'\n')
for esf in esfs_with_predicates:
    print(esf['verb']+': '+esf['esf_type']+'\n')
    f.write(esf['verb']+': '+esf['esf_type']+'\n')
    for se in esf['subevents']:
        if se['preposition'] == '':
            print(se['id']+': '+se['se_type']+': '+str(se['predicate'])+'('+str(se['arg_str'].keys()).split('[')[1].split(']')[0]+')\n')
            f.write(se['id']+': '+se['se_type']+': '+str(se['predicate'])+'('+str(se['arg_str'].keys()).split('[')[1].split(']')[0]+')\n')
        else:
            print(se['id']+': '+se['se_type']+': '+str(se['predicate'])+'_'+se['preposition']+'('+str(se['arg_str'].keys()).split('[')[1].split(']')[0]+')\n')
            f.write(se['id']+': '+se['se_type']+': '+str(se['predicate'])+'_'+se['preposition']+'('+str(se['arg_str'].keys()).split('[')[1].split(']')[0]+')\n')
    f.write('\n')
f.close()
"""



        


                    

                    

