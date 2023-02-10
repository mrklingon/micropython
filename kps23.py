from microbit import *
import speech
ps23 = [" DevwI'wI' ghaH joH'a''e': jIneHbe'.",
        "ghaH  chen  jIH  nep  bIng  Daq  SuD  tI' yotlh.",
        "ghaH  Dev  jIH  retlh  vIHHa'  bIQmey.",
        "ghaH  chenqa'  wIj  qa'.",
        "ghaH  Dev  jIH  Daq the  Hemey  vo'  QaQtaHghach  vaD  Daj name's  chIch.",
        "'ach  'a'  jIH  yIt  vegh the  ngech  vo' the  QIb  vo'  Hegh,",
        "jIH  DichDaq  taHvIp  ghobe'  mIghtaHghach,  vaD  SoH  'oH  tlhej  jIH.",
        "lIj  DevwI' naQ  je  lIj  naQ,  chaH  belmoH  jIH.",
        "SoH  ghuH a  SopDaq  qaSpa'  jIH  Daq the  Daq  vo'  wIj  jaghpu'.",
        "SoH anoint  wIj  nach  tlhej  Hergh.",
        "wIj  HIvje'  qettaH  Dung.",
        "DIch  QaQ  je loving kindness  DIchDaq  tlha'  jIH ",
        "Hoch the  jajmey  vo'  wIj  yIn,",
        "je  jIH  DichDaq  yIn  Daq Yahweh's  tuq  reH."]

for phrase in ps23:
    display.scroll(phrase)
    speech.say(phrase)

