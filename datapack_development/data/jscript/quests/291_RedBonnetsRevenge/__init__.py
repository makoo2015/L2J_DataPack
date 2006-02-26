# Maked by Mr. Have fun! Version 0.2

import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

BLACK_WOLF_PELT = 1482
GRANDMAS_PEARL,GRANDMAS_MIRROR,GRANDMAS_NECKLACE,GRANDMAS_HAIRPIN = range(1502,1506)

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "7553-03.htm" :
      st.set("cond","1")
      st.setState(STARTED)
      st.playSound("ItemSound.quest_accept")
    return htmltext


 def onTalk (Self,npc,st):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.set("cond","0")
   if int(st.get("cond"))==0 :
      if st.getPlayer().getLevel() < 4 :
          htmltext = "7553-01.htm"
          st.exitQuest(1)
      else:
          htmltext = "7553-02.htm"
   else :
      if st.getQuestItemsCount(BLACK_WOLF_PELT) < 40 :
        htmltext = "7553-04.htm"
      else:
          htmltext = "7553-05.htm"
          st.exitQuest(1)
          st.playSound("ItemSound.quest_finish")
          st.takeItems(BLACK_WOLF_PELT,-1)
          n = st.getRandom(100)
          if n <= 2 :
            st.giveItems(GRANDMAS_PEARL,1)
          elif n <= 20 :
            st.giveItems(GRANDMAS_MIRROR,1)
          elif n <= 45 :
            st.giveItems(GRANDMAS_NECKLACE,1)
          else :
            st.giveItems(GRANDMAS_HAIRPIN,1)
   return htmltext

 def onKill (self,npc,st):
   if st.getQuestItemsCount(BLACK_WOLF_PELT) < 40 :
     if st.getQuestItemsCount(BLACK_WOLF_PELT) < 39 :
       st.playSound("ItemSound.quest_itemget")
     else:
       st.playSound("ItemSound.quest_middle")
       st.set("cond","2")
     st.giveItems(BLACK_WOLF_PELT,1)
   return

QUEST       = Quest(291,"291_RedBonnetsRevenge","Red Bonnets Revenge")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(7553)

CREATED.addTalkId(7553)
STARTING.addTalkId(7553)
STARTED.addTalkId(7553)
COMPLETED.addTalkId(7553)

STARTED.addKillId(317)

STARTED.addQuestDrop(317,BLACK_WOLF_PELT,1)

print "importing quests: 291: Red Bonnets Revenge"
