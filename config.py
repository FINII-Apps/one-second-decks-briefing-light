project = "briefing"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Design

background_fix = 1
background_picture = "Wiretap.jpg"

title_fix = 1
title_picture = "Wiretap.jpg"

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# AI prompts

zielgruppe = "firmen die produkte haben"
branche = "b2b"

userjob = "emotional marketing"
problem1 = "emotionale landingpages entwickeln"
problem2 = "produkte vermarkten"
problem3 = "verkaufsargumente finden"
job_outcome = "verkaufen"
feature1 = "motion picture"
feature2 = "scrollytelling"
feature3 = "einprägsame interaktionen"
brand_edge = "nachhaltigkeit"


ki_request_001 = f"du hast ein produkt entwickelt und willst es einem potentiellen kunden beschreiben. der kunde will {userjob} aber hat drei probleme: {problem1}, {problem2}, {problem3}. als lösung bietet das produkt: {feature1}, {feature2}, {feature3} an um {job_outcome}. Beschreibe mir 1. was das produkt dem kunden abnimmt, 2. wie das produkt dies macht (gib auch ein beispiel) und 3. welche technischen komponenten das produkt haben muss. Schreibe den text einfach wie für einen fünfjährigen in kurzen worten aber mindestens 40 worte pro punkt. teile es in 3 punkte (1., 2., 3.)"
ki_request_002 = f"Du führst eine marke, die hilft bei {problem1}, {problem2}, {problem3} und {job_outcome}. Liste mir 10 einzigartige und kreative Kampagnenansätze"
ki_request_003 = f"Du bist Werbetexter und musst einen namen für ein produkt finden. Das produkt hilft zum {job_outcome}. Generiere einen einprägsamen und einzigartigen Namen."
ki_request_004 = f"welche chance ergibt sich für die marke wenn {feature1}, {feature2} und {feature3} von menschen gebraucht werden? Die Antwort sollte auch {brand_edge} berücksichtigen. Schreibe maximal 40 Worte." 
ki_request_005 = f"Du führst eine marke, die hilft bei {problem1}, {problem2}, {problem3} und {job_outcome}. wie verteidigt sich solch eine marke für gegen ihre wettbewerber? Die Antwort sollte auch {brand_edge} berücksichtigen. Gib auch ein Beispiel. Schreibe maximal 40 Worte."
ki_request_006 = f"Du führst eine marke, die hilft bei {problem1}, {problem2}, {problem3} und {job_outcome}. Wie verdienst du damit Geld? Die Antwort sollte auch {brand_edge} berücksichtigen. Gib auch ein Beispiel. Schreibe maximal 40 Worte." 
ki_request_007 = f"Liste mir 10 Wettbewerber aus dem Märkten rund um {userjob}, {problem1}, {problem2}, {problem3} und {job_outcome}. Beschreibe in zwei Sätzen jeweils ihre Positionierung und Markenbotschaft. Gib auch ein Beispiel."
ki_request_008 = f"Überlege dir 1 einfaches Synonym für {userjob}. Schreibe mir in 4 Sätzen eine kurze Geschichte über eine Person ({zielgruppe}), die das Synonym dringend nutzen sollte."
ki_request_009 = f"erzähl mir kurz warum der nutzer in der branche {branche} mit {userjob} zufrieden ist, nachdem er es genutzt hat. formuliere es in 2 sätzen. Insgemsat maximal 30 Worte"
ki_request_010 = f"Finde einen plakativen Namen für die Zielgruppe, für die der erfolg von {userjob} wichtig ist"


# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# File Paths

title = "1 Second Deck – Powerpoint App"

userfolder_path = "" 

# Pfad zum Eingangsordner (masters) und zur Eingabe-Datei (Master.pptx)
input_folder = f"{userfolder_path}masters"
input_file = f"{project}.pptx"

# Pfad zum Ausgabeordner (output) und zum Ausgabe-Dateinamen
output_folder = f"{userfolder_path}output"
output_file = f"{project}_edited.pptx"

img_folder = f"{userfolder_path}img/"

