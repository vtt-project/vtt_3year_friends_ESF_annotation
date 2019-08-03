# vtt_3year_friends_ESF_annotation
**Event Etructure Erame (ESF)** annotation of the verbs in English scripts for the drama FRIENDS season1 episodes 01~05

## Description

#### This project is about (semi-)automatic Event Structure Frame annotation of verbs in a given sentence by using ESF-annotated WordNet. 

##### - Input: the list of text sentences 
##### - Output: event structure frames for all verbs in the input text (json)
##### - Test data: English scripts of the American drama FRIENDS (season1 episodes 01~05)

#### Event Structure Frame Example

      sentence: Just leave my auro alone, okay?
      verb: leave
      Event Structure Frame Type: MAINTAIN
      Event Structure Frame:
             se1: pre-state: be(theme, state)
             se2: process: pred-ing(agent, theme, state)
             se3: post-state: be(theme, state)
             
      After argument mapping, you get the following:
             se1: pre-state: be(my_aura, alone)
             se2: process: leaving(my_auro, alone)
             se3: post-state: be(my_aura, alone)
      (pre-state: a presupposed state before the maintaining event, post-state: an entailed state after the maintaining event)

## Requirements

##### - Python 3.0 or higher

##### - NLTK (Natural Language ToolKit) and NLTK Dataset
    How to download and install NLTK: https://www.guru99.com/download-install-nltk.html
    
## How To Use

#### Preparing input data

###### The input should be a list of sentences (csv).

#### Checking necessary data and program files

###### - main program: assign_esf.py

###### - pre-defined Event Structure Frame list: esf_list.py

###### - ESF-annotated WordNet: friends_esf_wn

###### - verb inflection forms: vInflection

#### How to run a main program

      python assign_esf.py "sentence"

## Friends_verbs Event Structure Frame Annotation Result (json)

"Example:
{
    "sec_num": "34",
    "sentence": "Just leave my aura alone, okay?",
    "verb_event_structure_frames": [
        {
            "verb": "leave",
            "wn_synset": "leave.v.04",
            "esf_type": "MAINTAIN",
            "subevents": [
                {
                    "id": "se1",
                    "se_type": "pre-state",
                    "predicate": [
                        "be"
                    ],
                    "preposition": "",
                    "arg_str": {
                        "theme": "",
                        "state": ""
                    }
                },
                {
                    "id": "se1",
                    "se_type": "process",
                    "predicate": [
                        "refrain",
                        "leave",
                        "leave_alone",
                        "forbear",
                        "leave_behind"
                    ],
                    "preposition": "",
                    "arg_str": {
                        "agent": "",
                        "theme": "",
                        "state": ""
                    }
                },
                {
                    "id": "se1",
                    "se_type": "post-state",
                    "predicate": [
                        "be"
                    ],
                    "preposition": "",
                    "arg_str": {
                        "theme": "",
                        "state": ""
                    }
                }
            ]
        }
    ]
}"
