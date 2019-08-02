################################################
# Pre-defined Event Structure Frame list       #
# Date: 2019. 08. 01                           #
# Author: Seohyun Im                           # 
################################################

# Note:
#   pred = predicate, prep = preposition
#   The preposition AT represents a proper locative preposition which can be derivable from the given sentence.

frames = [
# state esf
#   se1: state: pred-ing_PREP(theme1, theme2)
{'type':'STATE', 'subevents':[{'id':'se1', 'se_type':'state', 'predicate':[], 'preposition': '', 'arg_str':{'theme1':'', 'theme2':''}}]},

# process esf
#   se1: process: pred-ing_PREP(agent)
{'type':'PROCESS', 'subevents':[{'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':''}}]},

# cause_process esf
#   se1: process: pred-ing_PREP(agent, theme)
#   se2: process: pred-ing_PREP(theme)
{'type':'CAUSE_PROCESS', 'subevents':[{'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':'', 'theme':''}},
                                           {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'theme':''}}]},

# semelfactive esf
#   se1: process: pred-ing_PREP(agent)
{'type':'SEMELFACTIVE', 'subevents':[{'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':''}}]},

# cause_semelfactive esf
#   se1: process: pred-ing_PREP(agent, theme)
#   se2: process: pred-ing_PREP(theme)
{'type':'CAUSE_SEMELFACTIVE', 'subevents':[{'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':'', 'theme':''}},
                                                {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'theme':''}}]},

# motion
#   d-se1: pre-state: be_AT(agent, source_location)
#   se1: process: pred-ing(agent)
#   d-se2: post-state: be_AT(agent, goal_location)
{'type':'MOTION', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                    {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                    {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_motion
#   d-se1: pre-state: be_AT(theme, source_location)
#   se1: process: pred-ing(agent, theme)
#   d-se2: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOTION', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                          {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                          {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# move_back
#   d-se1: pre-state: be_AT(agent, source_location)
#   d-se2: pre-state: be_behind(goal_location, source_location)
#   se1: process: pred-ing_back(agent)
#   d-se3: post-state: be_AT(agent, goal_location)
{'type':'MOVE_BACK', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'behind', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'back', 'arg_str':{'agent':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_move_back
#   d-se1: pre-state: be_AT(theme, source_location)
#   d-se2: pre-state: be_behind(goal_location, source_location)
#   se1: process: pred-ing_back(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOVE_BACK', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'behind', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'back', 'arg_str':{'agent':'', 'theme':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# move_up
#   d-se1: pre-state: be_AT(agent, source_location)
#   d-se2: pre-state: be_higher_than(goal_location, source_location)
#   se1: process: pred-ing_up(agent)
#   d-se3: post-state: be_AT(agent, goal_location)
{'type':'MOVE_UP', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_higher_than'], 'preposition':'', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'agent':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_move_up
#   d-se1: pre-state: be_AT(theme, source_location)
#   d-se2: pre-state: be_higher_than(goal_location, source_location)
#   se1: process: pred-ing_up(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOVE_UP', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_higher_than'], 'preposition':'', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'agent':'', 'theme':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# move_down
#   d-se1: pre-state: be_AT(agent, source_location)
#   d-se2: pre-state: be_lower_than(goal_location, source_location)
#   se1: process: pred-ing_down(agent)
#   d-se3: post-state: be_AT(agent, goal_location)
{'type':'MOVE_DOWN', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_lower_than'], 'preposition':'', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'down', 'arg_str':{'agent':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_move_down
#   d-se1: pre-state: be_AT(theme, source_location)
#   d-se2: pre-state: be_lower_than(goal_location, source_location)
#   se1: process: pred-ing_down(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOVE_DOWN', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                       {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_lower_than'], 'preposition':'', 'arg_str':{'goal_location':'', 'source_location':''}},
                                       {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'down', 'arg_str':{'agent':'', 'theme':''}},
                                       {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# move_toward_speaker
#   d-se1: pre-state: be_AT(agent, source_location)
#   d-se2: pre-state: be_AT(speaker, goal_location)
#   se1: process: pred-ing(agent)
#   d-se3: post-state: be_AT(agent, goal_location)
{'type':'MOVE_TOWARD_SPEAKER', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                                 {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'speaker':'', 'goal_location':''}},
                                                 {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                                 {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_move_toward_speaker
#   d-se1: pre-state: be_AT(theme, source_location)
#   d-se2: pre-state: be_AT(speaker, goal_location)
#   se1: process: pred-ing(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOVE_TOWARD_SPEAKER', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                                 {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'speaker':'', 'goal_location':''}},
                                                 {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                 {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# move_from_speaker
#   d-se1: pre-state: be_AT(agent, source_location)
#   d-se2: pre-state: be_AT(speaker, source_location)
#   se1: process: pred-ing(t)
#   d-se3: post-state: be_AT(agent, goal_location)
{'type':'MOVE_FROM_SPEAKER', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                                 {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'speaker':'', 'source_location':''}},
                                                 {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                                 {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_move_from_speaker
#   d-se1: pre-state: be_AT(theme, source_location)
#   d-se2: pre-state: be_AT(speaker, goal_location)
#   se1: process: pred-ing(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_MOVE_FROM_SPEAKER', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                                 {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'speaker':'', 'source_location':''}},
                                                 {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                 {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# pull
#   d-se1: pre-state: be_AT(theme, source_location)
#   se1: process: pred-ing(agent, theme)
#   d-se2: post-state: be_AT(theme, goal_location)
{'type':'PULL', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                  {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                  {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# push
#   d-se1: pre-state: be_AT(theme, source_location)
#   se1: process: pred-ing(agent, theme)
#   d-se2: post-state: be_AT(theme, goal_location)
{'type':'PUSH', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                  {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                  {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# carry
#   se1: process: pred-ing(agent, theme)
#   se2: state: having(agent, theme)
{'type':'CARRY', 'subevents':[{'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':'', 'theme':''}},
                                   {'id':'se2', 'se_type':'state', 'predicate':[], 'preposition': '', 'arg_str':{'agent':'', 'theme':''}}]},

# leave
#   se1: pre-state: be_AT(agent, source_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: not_be_AT(agent, source_location)
#   d-se1: post-state: be_AT(agent, goal_location)
{'type':'LEAVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                   {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                   {'id':'se3', 'se_type':'post-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                   {'id':'d-se1', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_leave
#   se1: pre-state: be_AT(theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: not_be_AT(theme, source_location)
#   d-se1: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_LEAVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                         {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                         {'id':'se3', 'se_type':'post-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                         {'id':'d-se1', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# arrive
#   se1: pre-state: not_be_AT(agent, goal_location)
#   d-se1: pre-state: be_AT(agent, source_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: be_AT(agent, goal_location)
{'type':'ARRIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}},
                                    {'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                    {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                    {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_arrive
#   se1: pre-state: not_be_AT(theme, goal_location)
#   d-se1: pre-state: be_AT(theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_ARRIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}},
                                          {'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                          {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                          {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},
# transfer
#   se1: pre-state: be_AT(agent, source_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: be_AT(agent, goal_location)
{'type':'TRANSFER', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                                      {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                      {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_transfer
#   se1: pre-state: be_AT(theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_TRANSFER', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                            {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                            {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},


# pass
#   se1: pre-state: be_AT(agent, source_location)
#   se2: process: pred-ing(agent)
#   se3: state: be_AT(agent, path)
#   se4: post-state: be_AT(agent, goal_location)
{'type':'PASS', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_location':''}},
                             {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                             {'id':'se3', 'se_type':'state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'path':''}},
                             {'id':'se4', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_location':''}}]},

# cause_pass
#   se1: pre-state: be_AT(theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: state: be_AT(theme, path)
#   se4: post-state: be_AT(theme, goal_location)
{'type':'CAUSE_PASS', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_location':''}},
                                   {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                   {'id':'se3', 'se_type':'state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'path':''}},
                                   {'id':'se4', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_location':''}}]},

# spread
#   se1: pre-state: not_be_OVER(agent, ground)
#   se2: process: pred-ing(agent)
#   se3: post-state: be_OVER(agent, ground)
{'type':'SPREAD', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'OVER', 'arg_str':{'agent':'', 'ground':''}},
                               {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                               {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'OVER', 'arg_str':{'agent':'', 'ground':''}}]},

# cause_spread
#   se1: pre-state: not_be_OVER(theme, ground)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_OVER(theme, ground)
{'type':'CAUSE_SPREAD', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'OVER', 'arg_str':{'theme':'', 'ground':''}},
                                          {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                          {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'OVER', 'arg_str':{'theme':'', 'ground':''}}]},

# bring
#   se1: pre-state: not_be_AT(agent&theme, goal_location)
#   d-se1: pre-state: be_AT(agent&theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_AT(agent&theme, goal_location)
{'type':'BRING', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'goal_location':''}},
                                   {'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'source_location':''}},
                                   {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                   {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'goal_location':''}}]},

# take
#   se1: pre-state: be_AT(agent&theme, source_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: not_be_AT(agent&theme, source_location)
#   d-se1: pre-state: be_AT(agent&theme, goal_location)
{'type':'TAKE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'source_location':''}},
                                  {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                  {'id':'se3', 'se_type':'post-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'source_location':''}},
                                  {'id':'d-se1', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'theme':'', 'goal_location':''}}]},

# lose
#   se1: pre-state: have(possessor, theme)
#   se2: process: pred-ing(possessor, theme)
#   se3: post-state: not_have(possessor, theme)
{'type':'LOSE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}},
                                  {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}},
                                  {'id':'se3', 'se_type':'post-state', 'predicate':['not_have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}}]},

# cause_lose
#   se1: pre-state: have(possessor, theme)
#   se2: process: pred-ing(causer, possessor, theme)
#   se3: post-state: not_have(possessor, theme)
{'type':'CAUSE_LOSE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}},
                                  {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'possessor':'', 'theme':''}},
                                  {'id':'se3', 'se_type':'post-state', 'predicate':['not_have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}}]},

# get
#   se1: pre-state: not_have(recipient, theme)
#   se2: process: pred-ing(recipient, theme)
#   se3: post-state: have(recipient, theme)
{'type':'GET', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}},
                                 {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}},
                                 {'id':'se3', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}}]},

# cause_get
#   se1: pre-state: not_have(recipient, theme)
#   se2: process: pred-ing(causer, recipient, theme)
#   se3: post-state: have(recipient, theme)
{'type':'CAUSE_GET', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}},
                                 {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'recipient':'', 'theme':''}},
                                 {'id':'se3', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}}]},

# give
#   se1: pre-state: have(possessor, theme)
#   se2: process: pred-ing(possessor, recipient, theme)
#   se3: post-state: have(recipient, theme)
{'type':'GIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme':''}},
                                  {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'possessor':'', 'recipient':'', 'theme':''}},
                                  {'id':'se3', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme':''}}]},

# exchange
#   se1: pre-state: have(possessor, theme1)
#   se2: pre-state: have(recipient, theme2)
#   se3: process: pred-ing(possessor, recipient, theme1, theme2)
#   se4: post-state: have(possessor, theme2)
#   se5: post-state: have(recipient, theme1)
{'type':'EXCHANGE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme1':''}},
                                  {'id':'se2', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme2':''}},
                                  {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'possessor':'', 'recipient':'', 'theme1':'', 'theme2':''}},
                                  {'id':'se4', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'theme2':''}},
                                  {'id':'se5', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'theme1':''}}]},

# info_transfer
#   se1: pre-state: have(possessor, info)
#   se2: process: pred-ing(possessor, recipient, info)
#   se3: post-state: have(possessor, info)
#   se4: poost-state: have(recipient, info)
{'type':'INFO_TRANSFER', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'info':''}},
                                           {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'possessor':'', 'recipient':'', 'info':''}},
                                           {'id':'se3', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'possessor':'', 'info':''}},
                                           {'id':'se4', 'se_type':'post-state', 'predicate':['have'], 'preposition':'', 'arg_str':{'recipient':'', 'info':''}}]},

# come_into_existence
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: there_be_not(theme)
#   se3: process: pred-ing(theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: there_be(theme)
{'type':'COME_INTO_EXISTENCE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se2', 'se_type':'pre-state', 'predicate':['there_not_be'], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se5', 'se_type':'post-state', 'predicate':['there_be'], 'preposition':'', 'arg_str':{'theme':''}}]},

# cause_come_into_existence
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: there_be_not(theme)
#   se3: process: pred-ing(agent, theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: there_be(theme)
{'type':'CAUSE_COME_INTO_EXISTENCE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se2', 'se_type':'pre-state', 'predicate':['there_not_be'], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                 {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se5', 'se_type':'post-state', 'predicate':['there_be'], 'preposition':'', 'arg_str':{'theme':''}}]},

# go_out_of_existence
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: there_be(theme)
#   se3: process: pred-ing(theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: there_not_be(theme)
{'type':'GO_OUT_OF_EXISTENCE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se2', 'se_type':'pre-state', 'predicate':['there_be'], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                 {'id':'se5', 'se_type':'post-state', 'predicate':['there_not_be'], 'preposition':'', 'arg_str':{'theme':''}}]},

# cause_go_out_of_existence
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: there_be(theme)
#   se3: process: pred-ing(agent, theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: there_not_be(theme)
{'type':'CAUSE_GO_OUT_OF_EXISTENCE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                       {'id':'se2', 'se_type':'pre-state', 'predicate':['there_be'], 'preposition':'', 'arg_str':{'theme':''}},
                                                       {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                       {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                       {'id':'se5', 'se_type':'post-state', 'predicate':['there_not_be'], 'preposition':'', 'arg_str':{'theme':''}}]},

# become
#   se1: pre-state: not_be_pred-ed(theme, state)
#   se2: pre-state: not_be(theme, state)
#   se3: process: pred-ing(theme, state)
#   se4: post-state: be_pred-ed(theme, state)
#   se5: post-state: be(theme, state)
{'type':'BECOME', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                    {'id':'se2', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                    {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                    {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                    {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'', 'arg_str':{'theme':'', 'state':''}}]},

# cause_become
#   se1: pre-state: not_be_pred-ed(theme, state)
#   se2: pre-state: not_be(theme, state)
#   se3: process: pred-ing(agent, theme, state)
#   se4: post-state: be_pred-ed(theme, state)
#   se5: post-state: be(theme, state)
{'type':'CAUSE_BECOME', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                          {'id':'se2', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                          {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':'', 'state':''}},
                                          {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':'', 'state':''}},
                                          {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'', 'arg_str':{'theme':'', 'state':''}}]},

# begin
#   se1: pre-state: not_in_progress(event)
#   se2: process: pred-ing(event)
#   se3: post-state: in_progress(event)
{'type':'BEGIN', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                   {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'event':''}},
                                   {'id':'se3', 'se_type':'post-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

# cause_begin
#   se1: pre-state: not_in_progress(event)
#   se2: process: pred-ing(agent, event)
#   se3: post-state: in_progress(event)
{'type':'CAUSE_BEGIN', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                         {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'event':''}},
                                         {'id':'se3', 'se_type':'post-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

# continue
#   se1: pre-state: in_progress(event)
#   se2: process: pred-ing(event)
#   se3: post-state: in_progress(event)
{'type':'CONTINUE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                      {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'event':''}},
                                      {'id':'se3', 'se_type':'post-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

# cause_continue
#   se1: pre-state: not_in_progress(event)
#   se2: process: pred-ing(agent, event)
#   se3: post-state: in_progress(event)
{'type':'CAUSE_CONTINUE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                            {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'event':''}},
                                            {'id':'se3', 'se_type':'post-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

# end
#   se1: pre-state: in_progress(event)
#   se2: process: pred-ing(event)
#   se3: post-state: not_in_progress(event)
{'type':'END', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                 {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'event':''}},
                                 {'id':'se3', 'se_type':'post-state', 'predicate':['not_in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

# cause_end
#   se1: pre-state: in_progress(event)
#   se2: process: pred-ing(agent, event)
#   se3: post-state: not_in_progress(event)
{'type':'CAUSE_END', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['in_progress'], 'preposition':'', 'arg_str':{'event':''}},
                                       {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'event':''}},
                                       {'id':'se3', 'se_type':'post-state', 'predicate':['not_in_progress'], 'preposition':'', 'arg_str':{'event':''}}]},

#positive_causation
#   se1: pre-state: not_happen(event)
#   se2: process: pred-ing(causer, event)
#   se3: post-state: happen(event)
{'type':'POSITIVE_CAUSATION', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_happen'], 'preposition':'', 'arg_str':{'event':''}},
                                                {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'event':''}},
                                                {'id':'se3', 'se_type':'post-state', 'predicate':['happen'], 'preposition':'', 'arg_str':{'event':''}}]},

#negative_causation
#   se1: pre-state: not_happen(event)
#   se2: process: pred-ing(causer, event)
#   se3: post-state: not_happen(event)
{'type':'NEGATIVE_CAUSATION', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_happen'], 'preposition':'', 'arg_str':{'event':''}},
                                                {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'event':''}},
                                                {'id':'se3', 'se_type':'post-state', 'predicate':['not_happen'], 'preposition':'', 'arg_str':{'event':''}}]},

#scale_up
#   d-se1: pre-state: be_AT(theme, source_scale)
#   d-se2: pre-state: be_higher_than(goal_scale, source_scale)
#   se1: process: pred-ing_up(theme)
#   d-se3: post-state: be_AT(theme, goal_scale)
{'type':'SCALE_UP', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                      {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_higher_than'], 'preposition':'', 'arg_str':{'goal_scale':'', 'source_scale':''}},
                                      {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'theme':''}},
                                      {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#cause_scale_up
#   d-se1: pre-state: be_AT(theme, source_scale)
#   d-se2: pre-state: be_higher_than(goal_scale, source_scale)
#   se1: process: pred-ing_up(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_scale)
{'type':'CAUSE_SCALE_UP', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                      {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_higher_than'], 'preposition':'', 'arg_str':{'goal_scale':'', 'source_scale':''}},
                                      {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'agent':'', 'theme':''}},
                                      {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#scale_dowm
#   d-se1: pre-state: be_AT(theme, source_scale)
#   d-se2: pre-state: be_lower_than(goal_scale, source_scale)
#   se1: process: pred-ing_up(theme)
#   d-se3: post-state: be_AT(theme, goal_scale)
{'type':'SCALE_DOWN', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                        {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_lower_than'], 'preposition':'', 'arg_str':{'goal_scale':'', 'source_scale':''}},
                                        {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'theme':''}},
                                        {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#cause_scale_down
#   d-se1: pre-state: be_AT(theme, source_scale)
#   d-se2: pre-state: be_lower_than(goal_scale, source_scale)
#   se1: process: pred-ing_up(agent, theme)
#   d-se3: post-state: be_AT(theme, goal_scale)
{'type':'CAUSE_SCALE_DOWN', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                              {'id':'d-se2', 'se_type':'pre-state', 'predicate':['be_lower_than'], 'preposition':'', 'arg_str':{'goal_scale':'', 'source_scale':''}},
                                              {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'agent':'', 'theme':''}},
                                              {'id':'d-se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#scale_move
#   d-se1: pre-state: be_AT(theme, source_scale)
#   se1: process: pred-ing(theme)
#   d-se2: post-state: be_AT(theme, goal_scale)
{'type':'SCALE_MOVE', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                        {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                        {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#cause_scale_move
#   d-se1: pre-state: be_AT(theme, source_scale)
#   se1: process: pred-ing_up(agent, theme)
#   d-se2: post-state: be_AT(theme, goal_scale)
{'type':'CAUSE_SCALE_MOVE', 'subevents':[{'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_scale':''}},
                                              {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition':'up', 'arg_str':{'agent':'', 'theme':''}},
                                              {'id':'d-se2', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_scale':''}}]},

#change_direction
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_direction)
#   se3: process: pred-ing(theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_direction)
{'type':'CHANGE_DIRECTION', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                              {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_direction':''}},
                                              {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                              {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                              {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_direction':''}}]},

#cause_change_direction
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_direction)
#   se3: process: pred-ing(causer, theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_direction)
{'type':'CAUSE_CHANGE_DIRECTION', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                    {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_direction':''}},
                                                    {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'causer':'', 'theme':''}},
                                                    {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                    {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_direction':''}}]},

#change_posture
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_posture)
#   se3: process: pred-ing(theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_posture)
{'type':'CHANGE_POSTURE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                            {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_posture':''}},
                                            {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                            {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                            {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_posture':''}}]},

#cause_change_posture
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_posture)
#   se3: process: pred-ing(causer, theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_posture)
{'type':'CAUSE_CHANGE_PSOTURE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                  {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_posture':''}},
                                                  {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                  {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                  {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_posture':''}}]},

#change_state
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_state)
#   se3: process: pred-ing(theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_state)
{'type':'CHANGE_STATE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                          {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_state':''}},
                                          {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                          {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                          {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_state':''}}]},

#cause_change_state
#   se1: pre-state: have_not_pred-ed(theme)
#   se2: pre-state: be_IN(theme, source_state)
#   se3: process: pred-ing(causer, theme)
#   se4: post-state: have_pred-ed(theme)
#   se5: post-state: be_IN(theme, goal_state)
{'type':'CAUSE_CHANGE_STATE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                {'id':'se2', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'source_state':''}},
                                                {'id':'se3', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                                {'id':'se4', 'se_type':'post-state', 'predicate':[], 'preposition':'', 'arg_str':{'theme':''}},
                                                {'id':'se5', 'se_type':'post-state', 'predicate':['be'], 'preposition':'IN', 'arg_str':{'theme':'', 'goal_state':''}}]},

# cos_leave
#   se1: pre-state: be_AT(agent, source_cos_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: not_be_AT(agent, source_cos_location)
#   d-se1: post-state: be_AT(agent, goal_cos_location)
{'type':'COS_LEAVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_cos_location':''}},
                                       {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                       {'id':'se3', 'se_type':'post-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_cos_location':''}},
                                       {'id':'d-se1', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_cos_location':''}}]},

# cause_cos_leave
#   se1: pre-state: be_AT(theme, source_cos_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: not_be_AT(theme, source_cos_location)
#   d-se1: post-state: be_AT(theme, goal_cos_location)
{'type':'CAUSE_COS_LEAVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_cos_location':''}},
                                         {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                         {'id':'se3', 'se_type':'post-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_cos_location':''}},
                                         {'id':'d-se1', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_cos_location':''}}]},

# cos_arrive
#   se1: pre-state: not_be_AT(agent, goal_cos_location)
#   d-se1: pre-state: be_AT(agent, source_cos_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: be_AT(agent, goal_cos_location)
{'type':'COS_ARRIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_cos_location':''}},
                                        {'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_cos_location':''}},
                                        {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                        {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_cos_location':''}}]},

# cause_cos_arrive
#   se1: pre-state: not_be_AT(theme, goal_cos_location)
#   d-se1: pre-state: be_AT(theme, source_cos_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_AT(theme, goal_cos_location)
{'type':'CAUSE_COS_ARRIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['not_be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_cos_location':''}},
                                          {'id':'d-se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_cos_location':''}},
                                          {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                          {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_cos_location':''}}]},
# cos_transfer
#   se1: pre-state: be_AT(agent, source_cos_location)
#   se2: process: pred-ing(agent)
#   se3: post-state: be_AT(agent, goal_cos_location)
{'type':'COS_TRANSFER', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'source_cos_location':''}},
                                      {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':''}},
                                      {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'agent':'', 'goal_cos_location':''}}]},

# cause_cos_transfer
#   se1: pre-state: be_AT(theme, source_cos_location)
#   se2: process: pred-ing(agent, theme)
#   se3: post-state: be_AT(theme, goal_lcos_ocation)
{'type':'CAUSE_COS_TRANSFER', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'source_cos_location':''}},
                                            {'id':'se2', 'se_type':'process', 'predicate':[], 'preposition':'', 'arg_str':{'agent':'', 'theme':''}},
                                            {'id':'se3', 'se_type':'post-state', 'predicate':['be'], 'preposition':'AT', 'arg_str':{'theme':'', 'goal_cos_location':''}}]},

# performative
#   se1: pre-state: not_be_pred-ed_to_by(theme, addressee, speaker)
#   se2: process: pred-ing(speaker, addressee, theme)
#   se3: post-state: be_pred-ed_to_by(theme, addressee, speaker)
{'type':'PERFORMATIVE', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':[],'preposition':'', 'arg_str':{'theme':'', 'addressee':'', 'speaker':''}},
                                          {'id':'se2', 'se_type':'process', 'predicate':[],'preposition':'', 'arg_str':{'speaker':'', 'addressee':'', 'theme':''}},
                                          {'id':'se3', 'se_type':'post-state', 'predicate':[],'preposition':'', 'arg_str':{'theme':'', 'addressee':'', 'speaker':''}}]},

# happen
#   se1: state: pred-ing(event)
{'type':'HAPPEN', 'subevents':[{'id':'se1', 'se_type':'state', 'predicate':[], 'preposition': '', 'arg_str':{'event':''}}]},

# maintain
#   se1: pre-state: be(state)
#   se2: process: pred-ing(agent, state)
#   se3: state: be(state)
{'type':'MAINTAIN', 'subevents':[{'id':'se1', 'se_type':'pre-state', 'predicate':['be'], 'preposition': '', 'arg_str':{'state':''}},
                                      {'id':'se1', 'se_type':'process', 'predicate':[], 'preposition': '', 'arg_str':{'agent':'', 'state':''}},
                                      {'id':'se1', 'se_type':'post-state', 'predicate':['be'], 'preposition': '', 'arg_str':{'state':''}}]},

# precede
#   se1: state: pred-ing(theme1, theme2)
#   se2: state: be_before(theme1, theme2)
{'type':'PRECEDE', 'subevents':[{'id':'se1', 'se_type':'state', 'predicate':[], 'preposition': '', 'arg_str':{'theme1':'', 'theme2':''}},
                                     {'id':'se1', 'se_type':'state', 'predicate':['be'], 'preposition': 'before', 'arg_str':{'theme1':'', 'theme2':''}}]},


# follow
#   se1: state: pred-ing(theme1, theme2)
#   se2: state: be_after(theme1, theme2)
{'type':'FOLLOW', 'subevents':[{'id':'se1', 'se_type':'state', 'predicate':[], 'preposition': '', 'arg_str':{'theme1':'', 'theme2':''}},
                                    {'id':'se1', 'se_type':'state', 'predicate':['be'], 'preposition': 'after', 'arg_str':{'theme1':'', 'theme2':''}}]}
]
