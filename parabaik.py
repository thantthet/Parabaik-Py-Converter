#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# https://gist.github.com/gromgull/3922244
def re_sub(pattern, replacement, string):
   def _r(m):
      # Now this is ugly.
      # Python has a "feature" where unmatched groups return None
      # then re_sub chokes on this.
      # see http://bugs.python.org/issue1519638
      
      # this works around and hooks into the internal of the re module...
 
      # the match object is replaced with a wrapper that
      # returns "" instead of None for unmatched groups
 
      class _m():
         def __init__(self, m):
            self.m=m
            self.string=m.string
         def group(self, n):
            return m.group(n) or ""
 
      return re._expand(pattern, _m(m), replacement)
   
   return re.sub(pattern, _r, string)

def z1_uni(text):
   text = re_sub(u"\u106A", u"\u1009", text)
   text = re_sub(u"\u1025(?=[\u1039\u102C])", u"\u1009", text)
   # new
   text = re_sub(u"\u1025\u102E", u"\u1026", text)
   # new
   text = re_sub(u"\u106B", u"\u100A", text)
   text = re_sub(u"\u1090", u"\u101B", text)
   text = re_sub(u"\u1040", u"\u1040", text)

   text = re_sub(u"\u108F", u"\u1014", text)
   text = re_sub(u"\u1012", u"\u1012", text)
   text = re_sub(u"\u1013", u"\u1013", text)
   ######

   text = re_sub(u"[\u103D\u1087]", u"\u103E", text)
   # ha
   text = re_sub(u"\u103C", u"\u103D", text)
   # wa
   text = re_sub(u"[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]", u"\u103C", text)
   # ya yint(ra)
   text = re_sub(u"[\u103A\u107D]", u"\u103B", text)
   # ya

   text = re_sub(u"\u103E\u103B", u"\u103B" + u"\u103E", text)
   # reorder

   text = re_sub(u"\u108A", u"\u103D" + u"\u103E", text)
   # wa ha

   ########### Reordering

   text = re_sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u1064", ur"\u1064\1\2\3", text)
   # reordering kinzi
   text = re_sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108B", ur"\u1064\1\2\3\u102D", text)
   # reordering kinzi lgt
   text = re_sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108C", ur"\u1064\1\2\3\u102E", text)
   # reordering kinzi lgtsk
   text = re_sub(u"(\u1031)?(\u103C)?([\u1000-\u1021])\u108D", ur"\u1064\1\2\3\u1036", text)
   # reordering kinzi ttt

   ####################

   text = re_sub(u"\u105A", u"\u102B" + u"\u103A", text)
   text = re_sub(u"\u108E", u"\u102D" + u"\u1036", text)
   # lgt ttt
   text = re_sub(u"\u1033", u"\u102F", text)
   text = re_sub(u"\u1034", u"\u1030", text)
   text = re_sub(u"\u1088", u"\u103E" + u"\u102F", text)
   # ha  u
   text = re_sub(u"\u1089", u"\u103E" + u"\u1030", text)
   # ha  uu

   ###################/

   text = re_sub(u"\u1039", u"\u103A", text)
   text = re_sub(u"[\u1094\u1095]", u"\u1037", text)
   # aukmyint

   ###################/ Pasint order human error
   text = re_sub(u"([\u1000-\u1021])([\u102C\u102D\u102E\u1032\u1036]){1,2}([\u1060\u1061\u1062\u1063\u1065\u1066\u1067\u1068\u1069\u1070\u1071\u1072\u1073\u1074\u1075\u1076\u1077\u1078\u1079\u107A\u107B\u107C\u1085])", r"\1\3\2", text)
   # new


   ######/

   text = re_sub(u"\u1064", u"\u1004\u103A\u1039", text)

   text = re_sub(u"\u104E", u"\u104E\u1004\u103A\u1038", text)

   text = re_sub(u"\u1086", u"\u103F", text)

   text = re_sub(u"\u1060", u"\u1039\u1000", text)
   text = re_sub(u"\u1061", u"\u1039\u1001", text)
   text = re_sub(u"\u1062", u"\u1039\u1002", text)
   text = re_sub(u"\u1063", u"\u1039\u1003", text)
   text = re_sub(u"\u1065", u"\u1039\u1005", text)
   text = re_sub(u"[\u1066\u1067]", u"\u1039\u1006", text)
   text = re_sub(u"\u1068", u"\u1039\u1007", text)
   text = re_sub(u"\u1069", u"\u1039\u1008", text)
   text = re_sub(u"\u106C", u"\u1039\u100B", text)
   text = re_sub(u"\u1070", u"\u1039\u100F", text)
   text = re_sub(u"[\u1071\u1072]", u"\u1039\u1010", text)
   text = re_sub(u"[\u1073\u1074]", u"\u1039\u1011", text)
   text = re_sub(u"\u1075", u"\u1039\u1012", text)
   text = re_sub(u"\u1076", u"\u1039\u1013", text)
   text = re_sub(u"\u1077", u"\u1039\u1014", text)
   text = re_sub(u"\u1078", u"\u1039\u1015", text)
   text = re_sub(u"\u1079", u"\u1039\u1016", text)
   text = re_sub(u"\u107A", u"\u1039\u1017", text)
   text = re_sub(u"\u107B", u"\u1039\u1018", text)
   text = re_sub(u"\u107C", u"\u1039\u1019", text)
   text = re_sub(u"\u1085", u"\u1039\u101C", text)
   text = re_sub(u"\u106D", u"\u1039\u100C", text)

   text = re_sub(u"\u1091", u"\u100F\u1039\u100D", text)
   text = re_sub(u"\u1092", u"\u100B\u1039\u100C", text)
   text = re_sub(u"\u1097", u"\u100B\u1039\u100B", text)
   text = re_sub(u"\u106F", u"\u100E\u1039\u100D", text)
   text = re_sub(u"\u106E", u"\u100D\u1039\u100D", text)

   ############################

   text = re_sub(u"(\u103C)([\u1000-\u1021])(\u1039[\u1000-\u1021])?", r"\2\3\1", text)
   # reordering ra

   text = re_sub(u"(\u103E)(\u103D)([\u103B\u103C])", r"\3\2\1", text)
   text = re_sub(u"(\u103E)([\u103B\u103C])", r"\2\1", text)

   text = re_sub(u"(\u103D)([\u103B\u103C])", r"\2\1", text)

   text = re_sub(u"(([\u1000-\u101C\u101D\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F]))(\u1040)", ur"\1\u101D", text);
   # zero and wa

   text = re_sub(u"(\u1040)(?=([\u1040\u1047])*([\u1000-\u101C\u101D\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F]))", u"\u101D", text)   # zero and wa


   text = re_sub(u"(([\u1000-\u101C\u101D\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F]))(\u1047)", ur"\1\u101B", text);
   # seven and ra

   text = re_sub(u"(\u1047)(?=([\u1047])*([\u1000-\u101C\u101D\u101E-\u102A\u102C\u102E-\u103F\u104C-\u109F]))", u"\u101B", text)   # seven and ra


   text = re_sub(u"(\u1031)?([\u1000-\u1021])(\u1039[\u1000-\u1021])?([\u102D\u102E\u1032])?([\u1036\u1037\u1038]{0,2})([\u103B-\u103E]{0,3})([\u102F\u1030])?([\u1036\u1037\u1038]{0,2})([\u102D\u102E\u1032])?", r"\2\3\6\1\4\9\7\5\8", text)
   # reordering storage order

   text = re_sub(u"(\u103A)(\u1037)", r"\2\1", text)
   # For Latest Myanmar3

   text = re_sub(u"(\u1036)(\u102F)", r"\2\1", text)
   # For Latest Myanmar3
   return text