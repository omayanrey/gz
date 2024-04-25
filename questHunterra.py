            # Quest Diarias #


# Weapon & Itens List Ids #
Main_Weapon = 5593

HunterraList = [5592,6612]

DoratiaList = []

    # Island Hunterra #
Hunterra = True
Hunterra_Sequence = ["G", "R", "C", "BB", "H", "B", "F", "CM", "I"]
    # Quests Hunterra #
Redeath = True
Gigantula = True
Crustea = True
Blodbreak = True
Horrornet = True
Bastinx = True
Foresdrake = True
Crysmantis = True
Ifrit = True
NunaFilet = True
LeechacleHeart = True
Mushroom = True
Bloodroot = True
Crystais = True
Ethereal = True

Skills_Hunterra = ["All-In", "Battlemaster"]

    # Island Doratia #

Doratia = False

    # Quest Doratia #

Forgotten = True
Observer = True

Skills_Doratia = ["All-In", "Battlemaster"]
# waypoints

base = 0

# Pegando as Quest Hunterra
for_base_Hunterra = 1
Going_To_PawbloodR = 2
ToBaseRedeath = 3
Going_To_PawbloodG = 4
ToBaseGigantula = 5
Going_To_PawbloodC = 6
ToBaseCrustea = 7
Going_To_QuickillBB = 8
ToBaseBlodbreak = 9
Going_To_QuickillH = 10
ToBaseHorrornet = 11
Going_To_QuickillB = 12
ToBaseBastinx = 13
Going_To_DCorrecF = 14
ToBaseForesdrake = 15
Going_To_DCorrecC = 16
ToBaseCrysmantis = 17
Going_To_DCorrecI = 18
ToBaseIfrit = 19
Going_To_ForageurN = 20
ToBaseNuna = 21
Going_To_ForageurH = 22
ToBaseHeart = 23
Going_To_ForageurM = 24
ToBaseNude = 25
Going_To_LeframS = 26
ToBaseSeed = 27
Going_To_LeframC = 28
ToBaseCrystais = 29
Going_To_LeframE = 30
ToBaseEssence = 31
FromHunterraToAurea = 32

# Indo Fazer as quest de Hunterra
FromAureaToHunterra = 33

GoToHuntRedeath = 34
HuntRedeath = 35
ToBaseRedeathDone = 35
ToPawbloodRedeathDone = 36

GoToHuntGigantula = 37
ToBaseGigantulaDone = 38
ToPawbloodGigantulaDone = 39

GoToHuntCrustea = 40
ToBaseCrusteaDone = 41
ToPawbloodCrusteaDone = 42

GoToHuntBloodbreak = 43
ToBaseBloodbreakDone = 44
ToQuickillBloodbreakDone = 45

GoToHuntHorrornet = 46
ToBaseHorrornetDone = 47
ToQuickillHorrornetDone = 48

GoToHuntBastinx = 49
ToBaseBastinxDone = 50
ToQuickillBastinxDone = 51





# spot base
spot_base_aurea = (31974, 32009, 7)
spot_base_Hunterra = (32849, 32022, 7)
spot_Base_Doratia = ()

# spot Retrieve and Store itens and Skill exchange.
spot_retrieve = (31974, 32006, 7)
spot_Store = (31974, 32011, 7)
spot_SkillExchange = (31974, 32008, 7)
# spot npc
spot_Pawblood = (32841, 32024, 7)
spot_Quikill = (32849, 32025, 7)
spot_Don_Correc = (32854, 32020, 7)
spot_Forageur = (32861, 32020, 7)
spot_Lefram = (32856, 32031, 7)

def ResertVar():
    script.SetVar('take_questH', 0)
    # 0 é quando nao possui quest, 1 quando pegou a quest e 2 quando terminou
    script.SetVar('Redeath', 0)
    script.SetVar('Gigantula', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Bloodbreak', 0)
    script.SetVar('Horrornet', 0)
    script.SetVar('Bastinx', 0)
    script.SetVar('Foresdrake', 0)
    script.SetVar('Crysmantis', 0)
    script.SetVar('Ifrit', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Crustea', 0)
    script.SetVar('Count', 0)
    script.SetVar('QuestSequence', 0)
def onScriptActivation():
    script.PauseMovement(False)
    script.ForceCloseMenus()
    script.DisableStorageInfo(True)
    ResertVar()

def onGetList():
    way = script.GetWay()
    if way == for_base_Hunterra or way == FromHunterraToAurea or way == FromAureaToHunterra:
        return HunterraList
    
def onRetrieveItens():
    ItensList = onGetList()
    GetInventory = list(script.GetInventoryItems())
    GetBackpack = list(script.GetBackpackItems())
    count = script.GetVar('Count')
    
    if count < len(ItensList) and ItensList[count] in GetInventory:
        itemId = ItensList[count]

        if not script.RetrieveItem(itemId):
            if script.IsUsingMenu():
                script.ForceCloseMenus()
            script.RunEvent('onRetrieveItens', 1000)
        else:
            script.RunEvent('onRetrieveItens', 1000)
    else:
        if count >= len(ItensList):
            script.SetVar('Count', 0)
            script.PauseMovement(False)
            return
        elif ItensList[count] in GetBackpack:
            script.SetVar('Count', count + 1)
            script.RunEvent('onRetrieveItens', 1000)
        else:
            script.RunEvent('onRetrieveItens', 1000)

# def onRetrieveItens():
#     ItensList = onGetList()
#     GetInventory = list(script.GetInventoryItems())
#     GetBackpack = list(script.GetBackpackItems())
    
#     for itemId in ItensList:
#         if itemId in GetBackpack:
#             continue
#         if not script.IsStorageRunning():
#             if not script.RetrieveItem(itemId):
#                 if script.IsUsingMenu():
#                     script.ForceCloseMenus()
#                 script.RunEvent('onRetrieveItens', 1000)
#             else:
#                 script.RunEvent('onRetrieveItens', 1000)
#     else:
#         script.RunEvent('onRetrieveItens', 1000)


def onStoreItens():
    ItensList = onGetList()
    GetBackpack = list(script.GetBackpackItems())
    count = script.GetVar('Count')

    if count >= len(ItensList):
        script.SetVar('Count', 0)
        script.PauseMovement(False)
        return

    if ItensList[count] in GetBackpack:
        itemId = ItensList[count]

        if not script.StoreItem(itemId, True):
            if script.IsUsingMenu():
                script.ForceCloseMenus()
            script.RunEvent('onStoreItens', 1000)
        else:
            script.RunEvent('onStoreItens', 1000)
    else:
        script.SetVar('Count', count + 1)
        script.RunEvent('onStoreItens', 1000)

def onGetSkillList():
    way = script.GetWay()
    if way == for_base_Hunterra or way == FromAureaToHunterra:
        return Skills_Hunterra
def onSkillExchange():
    getSkill = onGetSkillList()
    script.StatusMessage(str(getSkill))
    if script.GetSkillName(True) != getSkill[0]:
        script.ActivateSkill(getSkill[0], 1) # Skill left
        script.RunEvent('onSkillExchange', 5000)
           
    elif script.GetSkillName(False) != getSkill[1]:
        script.ActivateSkill(getSkill[1], 2) # Skill right
        script.RunEvent('onSkillExchange', 5000)

    else:
        script.PauseMovement(False)

def onChangeLocation(x, y, z):
    xyz = (x, y, z)
    way = script.GetWay()
    sequenceQ = script.GetVar('QuestSequence')
    if xyz == spot_base_aurea:
        if way == base:
            if Hunterra == True: 
                script.SetWay(for_base_Hunterra, 2)
            elif Doratia == True and Hunterra == False:
                script.SetWay(for_base_Doratia, 2)
        elif way == FromHunterraToAurea:
            if Doratia == True:
                script.SetWay(for_base_Doratia, 2)
            else:
                script.SetWay(FromAureaToHunterra, 2)
     
    elif xyz == spot_base_Hunterra:
        if way == for_base_Hunterra: 
            if Redeath == True:
                script.SetWay(Going_To_PawbloodR, 2)
            elif Gigantula == True and Redeath == False:
                script.SetWay(Going_To_PawbloodG, 2)
            elif Crustea == True and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_PawbloodC, 2)
            elif Blodbreak == True and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_QuickillBB, 2)
            elif Horrornet == True and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_QuickillH, 2)
            elif Bastinx == True and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False and Redeath == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseRedeath:
            if Gigantula == True:
                script.SetWay(Going_To_PawbloodG, 2)
            elif Crustea == True and Gigantula == False:
                script.SetWay(Going_To_PawbloodC, 2)
            elif Blodbreak == True and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_QuickillBB, 2)
            elif Horrornet == True and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_QuickillH, 2)
            elif Bastinx == True and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False and Gigantula == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseGigantula:
            if Crustea == True:
                script.SetWay(Going_To_PawbloodC, 2)
            elif Blodbreak == True and Crustea == False:
                script.SetWay(Going_To_QuickillBB, 2)
            elif Horrornet == True and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_QuickillH, 2)
            elif Bastinx == True and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                    script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                    script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                    script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False and Crustea == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseCrustea:
            if Blodbreak == True:
                script.SetWay(Going_To_QuickillBB, 2)
            elif Horrornet == True and Blodbreak == False:
                script.SetWay(Going_To_QuickillH, 2)
            elif Bastinx == True and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False and Blodbreak == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseBlodbreak:
            if Horrornet == True:
                script.SetWay(Going_To_QuickillH, 2)
            elif Bastinx == True and Horrornet == False:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False and Horrornet == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseHorrornet:
            if  Bastinx == True:
                script.SetWay(Going_To_QuickillB, 2)
            elif Foresdrake == True and Bastinx == False:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False and Bastinx == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseBastinx:
            if Foresdrake == True:
                script.SetWay(Going_To_DCorrecF, 2)
            elif Crysmantis == True and Foresdrake == False:
                    script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False and Foresdrake == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseForesdrake:
            if Crysmantis == True:
                script.SetWay(Going_To_DCorrecC, 2)
            elif Ifrit == True and Crysmantis == False:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False and Crysmantis == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(Going_To_LeframE, 2)
        elif way == ToBaseCrysmantis:
            if Ifrit == True:
                script.SetWay(Going_To_DCorrecI, 2)
            elif NunaFilet == True and Ifrit == False:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False and Ifrit == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False and Ifrit == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False and Ifrit == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)

        elif way == ToBaseIfrit:
            if NunaFilet == True:
                script.SetWay(Going_To_ForageurN, 2)
            elif LeechacleHeart == True and NunaFilet == False:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False and NunaFilet == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False and NunaFilet == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False and NunaFilet == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseNuna:
            if LeechacleHeart == True:
                script.SetWay(Going_To_ForageurH, 2)
            elif Mushroom == True and LeechacleHeart == False:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseHeart:
            if Mushroom == True:
                script.SetWay(Going_To_ForageurM, 2)
            elif Bloodroot == True and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False and Mushroom == False and LeechacleHeart == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseNude:
            if Bloodroot == True:
                script.SetWay(Going_To_LeframS, 2)
            elif Crystais == True and Bloodroot == False:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseSeed:
            if Crystais == True:
                script.SetWay(Going_To_LeframC, 2)
            elif Ethereal == True and Crystais == False and Bloodroot == False:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)
        elif way == ToBaseCrystais:
            if Ethereal == True:
                script.SetWay(Going_To_LeframE, 2)
            else:
                script.SetWay(FromHunterraToAurea, 2)   
        elif way == ToBaseEssence:
            script.SetWay(FromHunterraToAurea, 2)

        elif way == FromAureaToHunterra:
            if Hunterra_Sequence[sequenceQ] == 'R' and script.GetVar('Quest_Redeath') == 0:
                script.SetWay(GoToHuntRedeath, 2)
            elif Hunterra_Sequence[sequenceQ] == 'G' and script.GetVar('Gigantula') == 0:
                script.SetWay(GoToHuntGigantula, 2)
            elif Hunterra_Sequence[sequenceQ] == 'C' and script.GetVar('Crustea') == 0:
                script.SetWay(GoToHuntCrustea, 2)
            elif Hunterra_Sequence[sequenceQ] == 'BB' and script.GetVar('Bloodbreak') == 0:
                pass
                     
    elif xyz == spot_Pawblood:
        if way == Going_To_PawbloodR or way == Going_To_PawbloodG or way == Going_To_PawbloodC:
            script.GoToNpcEx('Pawblood')
    elif xyz == spot_Quikill:        
        if way == Going_To_QuickillBB or way == Going_To_QuickillH or way == Going_To_QuickillB:
            script.GoToNpcEx('Quickill')
    elif xyz == spot_Don_Correc:
        if way == Going_To_DCorrecF or way == Going_To_DCorrecC or way == Going_To_DCorrecI:
            script.GoToNpcEx('Don Correc')
    elif xyz == spot_Forageur:
        if way == Going_To_ForageurN or way == Going_To_ForageurH or way == Going_To_ForageurM:
            script.GoToNpcEx('Forageur')
    elif xyz == spot_Lefram:
        if way == Going_To_LeframC or way == Going_To_LeframS or way == Going_To_LeframE:
            script.GoToNpcEx('Leflam')

    elif xyz == spot_retrieve:
        script.PauseMovement(True)
        script.RunEvent('onRetrieveItens', 1000)
    elif xyz == spot_Store:
        script.PauseMovement(True)
        script.RunEvent('onStoreItens', 1000)
    elif xyz == spot_SkillExchange:
        script.PauseMovement(True)
        script.RunEvent('onSkillExchange', 1000)
def onReachedNpc(uid, name):
	if not script.TalkToNpc(uid):
		script.StatusMessage('Can\'t talk to ' + name + '!')

def onTalkedWithNpc(uid, result):
	if not result:
		if not script.TalkToNpc(uid):
			script.StatusMessage('Can\'t talk to ' + name + '!')

def onReceiveNpcDialogue(name, text, answers):
    var = script.GetVar('dialog')
    way = script.GetWay()

    if name == 'Pawblood':
        if 'Welcome back' in text:
            if way == Going_To_PawbloodR or way == Going_To_PawbloodG or way == Going_To_PawbloodC:
                script.ChooseNpcOption(2)
        elif 'Well, with your experience' in text:
            if way == Going_To_PawbloodR:
                script.StatusMessage('**Quest Redeath**')
                script.ChooseNpcOption(script.GetAnswerId('Redeath.', answers))
                script.SetWay(ToBaseRedeath, 2)
                script.ForgetNpc()
            elif way == Going_To_PawbloodG:
                script.StatusMessage('**Quest Gigantula**')
                script.ChooseNpcOption(script.GetAnswerId('Gigantula.', answers))
                script.SetWay(ToBaseGigantula, 2)
                script.ForgetNpc()
            elif way == Going_To_PawbloodC:
                script.StatusMessage('**Quest Crustea**')
                script.ChooseNpcOption(script.GetAnswerId('Crustea.', answers))
                script.SetWay(ToBaseCrustea, 2)
                script.ForgetNpc()
        elif 'You can start a hunt on a specific prey' in text:
            if way == Going_To_PawbloodR:
                script.SetWay(Going_To_PawbloodR, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 1 min
            elif way == Going_To_PawbloodG:
                script.SetWay(Going_To_PawbloodG, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 1 min
            elif way == Going_To_PawbloodC:
                script.SetWay(Going_To_PawbloodC, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 1 min
        elif 'You\'re already on the hunt for this prey.' in text:
            script.ForgetNpc()
    elif name == 'Quickill':
        if 'Welcome back' in text:
            if way == Going_To_QuickillBB or way == Going_To_QuickillH or way == Going_To_QuickillB:
                script.ChooseNpcOption(1)
        elif 'Well, with your' in text or 'dangerous running bird' in text:
            if way == Going_To_QuickillBB:
                script.StatusMessage('**Quest Bloodbeak**')
                script.ChooseNpcOption(script.GetAnswerId('Bloodbeak.', answers))
                script.SetWay(ToBaseBlodbreak, 2)
                script.ForgetNpc()
            elif way == Going_To_QuickillH:
                script.StatusMessage('**Quest Horrornet**')
                script.ChooseNpcOption(script.GetAnswerId('Horrornet.', answers))
                script.SetWay(ToBaseHorrornet, 2)
                script.ForgetNpc()
            elif way == Going_To_QuickillB:
                script.StatusMessage('**Quest Bastinx**')
                script.ChooseNpcOption(script.GetAnswerId('Bastinx.', answers))
                script.SetWay(ToBaseBastinx, 2)
                script.ForgetNpc()

        elif 'get your performance rated' in text:
            if way == Going_To_QuickillB:
                script.ChooseNpcOption(cript.GetAnswerId('Get rated.', answers))
        elif '24 hours. Come back later' in text:
            if way == Going_To_QuickillBB:
                script.SetWay(Going_To_QuickillBB, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 seg
            elif way == Going_To_QuickillH:
                script.SetWay(Going_To_QuickillH, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 seg
            elif way == Going_To_QuickillB:
                script.SetWay(Going_To_QuickillB, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 seg
        
        elif 'And your performance against' in text:
            script.ChooseNpcOption(1)
        elif 'So you have problems with a task' in text:
            if way == Going_To_QuickillBB:
                script.ChooseNpcOption(script.GetAnswerId('Bloodbeak.', answers))
                script.SetWay(ToBaseBlodbreak, 2)
                script.ForgetNpc()
            elif way == Going_To_QuickillH:
                script.ChooseNpcOption(script.GetAnswerId('Horrornet.', answers))
                script.SetWay(ToBaseHorrornet, 2)
                script.ForgetNpc()
            elif way == Going_To_QuickillB:
                script.ChooseNpcOption(script.GetAnswerId('Bastinx.', answers))
                script.SetWay(ToBaseBastinx, 2)
                script.ForgetNpc()


    elif name == 'Don Correc':
        if 'Welcome back' in text:
            if way == Going_To_DCorrecF or way == Going_To_DCorrecC or way == Going_To_DCorrecI:
                script.StatusMessage('Start hunt.')
                script.SetVar('don_correc_cipsoft_fix', 1)
                script.ChooseNpcOption(1)
            elif way == to_don_correc_done:
                script.StatusMessage('Get rated.')
                script.ChooseNpcOption(2)
        elif 'Well, with your experience' in text:
            if way == Going_To_DCorrecF:
                script.StatusMessage('**Quest Foresdrake**')
                script.ChooseNpcOption(script.GetAnswerId('Foresdrake.', answers)) # Choose prey
                script.SetWay(ToBaseForesdrake, 2)
                script.ForgetNpc()
            elif way == Going_To_DCorrecC:
                script.StatusMessage('**Quest Crysmantis**')
                script.ChooseNpcOption(script.GetAnswerId('Crysmantis.', answers)) # Choose prey
                script.SetWay(ToBaseCrysmantis, 2)
                script.ForgetNpc()
            elif way == Going_To_DCorrecI:
                script.StatusMessage('**Quest Ifrit**')
                script.ChooseNpcOption(script.GetAnswerId('Ifrit.', answers)) # Choose prey
                script.SetWay(ToBaseIfrit, 2)
                script.ForgetNpc()
        elif 'And your performance' in text:
            if way == Going_To_DCorrecF:
                script.StatusMessage('**Quest Foresdrake2**')
                script.ChooseNpcOption(script.GetAnswerId('Foresdrake.', answers)) # Choose prey
            elif way == Going_To_DCorrecC:
                script.StatusMessage('**Quest Crysmantis2**')
                script.ChooseNpcOption(script.GetAnswerId('Crysmantis.', answers)) # Choose prey
            elif way == Going_To_DCorrecI:
                script.StatusMessage('**Quest Ifrit2**')
                script.ChooseNpcOption(script.GetAnswerId('Ifrit.', answers)) # Choose prey
        elif 'You already hunted' in text:
            script.ChooseNpcOption(1) # Get Rated
            script.StatusMessage('Option: Get rated')
        elif 'You can start a hunt on a specific' in text:
            if way == Going_To_DCorrecF:
                script.SetWay(Going_To_DCorrecF, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 5min.
            elif way == Going_To_DCorrecC:
                script.SetWay(Going_To_DCorrecC, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 5min.
            elif way == Going_To_DCorrecI:
                script.SetWay(Going_To_DCorrecI, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 5min.
        elif 'You are already hunting' in text:
            if way == Going_To_DCorrecF:
                script.SetWay(ToBaseForesdrake, 2)
                script.ForgetNpc()
            elif way == Going_To_DCorrecC:
                script.SetWay(ToBaseCrysmantis, 2)
                script.ForgetNpc()
            elif way == Going_To_DCorrecI:
                script.SetWay(ToBaseIfrit, 2)
                script.ForgetNpc()
        elif 'Exit the camp by the eastern bridge' in text:
            script.StatusMessage('Taken Foresdrake.')
            script.SetVar('dialog', var + 1)
            script.GoToNpcEx('Don Correc')
        elif 'Exit the camp by the south western' in text:
            script.StatusMessage('Taken Crysmantis.')
            script.SetVar('dialog', var + 1)
            script.GoToNpcEx('Don Correc')
        elif 'Exit the camp and search' in text:
            script.StatusMessage('Taken Ifrit.')
            script.SetVar('dialog', 0)
            script.ForgetNpc()
        # elif 'Your last hunt on' in text:
        #     if var < 2:
        #         script.StatusMessage('L Option: ' + str(option))
        #         script.SetVar('dialog', var + 1)
        #         script.ChooseNpcOption(1) # Get Rated
        #     else:
        #         script.StatusMessage('Received all rewards.')
        #         script.SetVar('dialog', 0)
        #         script.EndNpcChat()
        #         script.ForgetNpc()
        #         onQuestFinish()
        # elif 'Your time was up' in text:
        #     if var < 2:
        #         script.SetVar('dialog', var + 1)
        #         script.GoToNpcEx('Don Correc')
        #     else:
        #         script.StatusMessage('Received all rewards.')
        #         script.SetVar('dialog', 0)
        #         script.EndNpcChat()
        #         script.ForgetNpc()
        #         onQuestFinish()
        # elif 'You scored' in text:
        #     if var < 2:
        #         script.SetVar('dialog', var + 1)
        #         script.GoToNpcEx('Don Correc')
        #     else:
        #         script.StatusMessage('Received all rewards.')
        #         script.SetVar('dialog', 0)
        #         script.EndNpcChat()
        #         script.ForgetNpc()
        #         onQuestFinish()
        # elif 'You didn\'t deliver any' in text:
        #     if var < 2:
        #         script.SetVar('dialog', var + 1)
        #         script.GoToNpcEx('Don Correc')
        #         script.Alarm('Time is not up for Don Correc: ' + str(val))
        #     else:
        #         script.SetVar('dialog', 0)
    
    elif name == 'Forageur':
        if 'Welcome,' in text:
            if way == Going_To_ForageurN or way == Going_To_ForageurH or way == Going_To_ForageurM:
                script.StatusMessage('Need help?')
                script.ChooseNpcOption(1)
        elif 'I still have enough' in text:
            if way == Going_To_ForageurN:
                script.SetWay(Going_To_ForageurN, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 Seg
            elif way == Going_To_ForageurH:
                script.SetWay(Going_To_ForageurH, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 Seg
            elif way == Going_To_ForageurM:
                script.SetWay(Going_To_ForageurM, 2)
                script.ForgetNpc()
                script.LogoutFor(15) # logout for 15 Seg
        elif 'Just choose and I will see if' in text:
            if way == Going_To_ForageurN:
                script.ChooseNpcOption(script.GetAnswerId('Nuna filet.', answers)) # Choose prey
                script.StatusMessage('Option: Nuna filet')
                script.SetWay(ToBaseNuna, 2)
                script.ForgetNpc()
            elif way == Going_To_ForageurH:
                script.ChooseNpcOption(script.GetAnswerId('Leechacle heart.', answers)) # Choose prey
                script.StatusMessage('Option: Leechacle Heart')
                script.SetWay(ToBaseHeart, 2)
                script.ForgetNpc()
            elif way == Going_To_ForageurM:
                script.ChooseNpcOption(script.GetAnswerId('Newdelishroom.', answers)) # Choose prey
                script.StatusMessage('Option: Newdelishroom')
                script.SetWay(ToBaseNude, 2)
                script.ForgetNpc()
        elif 'I already sent you' in text:
            if way == Going_To_ForageurN:
                script.ChooseNpcOption(script.GetAnswerId('Nuna filet.', answers)) # Choose prey
                script.StatusMessage('**Nuna filet**')
                script.SetWay(ToBaseNuna, 2)
                script.ForgetNpc()
            elif way == Going_To_ForageurH:
                script.ChooseNpcOption(script.GetAnswerId('Leechacle heart.', answers)) # Choose prey
                script.StatusMessage('**Leechacle Heart**')
                script.SetWay(ToBaseHeart, 2)
                script.ForgetNpc()
            elif way == Going_To_ForageurM:
                script.ChooseNpcOption(script.GetAnswerId('Newdelishroom.', answers)) # Choose prey
                script.StatusMessage('**Newdelishroom**')
                script.SetWay(ToBaseNude, 2)
                script.ForgetNpc()

        elif 'Excellent. Which' in text:
            option = var + 1
            script.StatusMessage('Option: ' + str(option))
            script.ChooseNpcOption(option) # Choose option
        elif 'Nunaquatch.' in text:
            script.StatusMessage('Nuna filet.')
            script.SetVar('dialog', var + 1)
            script.GoToNpcEx('Forageur')
        elif 'leechacle.' in text:
            script.StatusMessage('Leechacle heart.')
            script.SetVar('dialog', var + 1)
            script.GoToNpcEx('Forageur')
        elif 'monster named Kapami.' in text:
            script.StatusMessage('Nudelishroom.')
            setWay(to_leflam, 1, 1)
            script.SetVar('dialog', 0)
            script.ForgetNpc()
        
    elif name == 'Leflam':
        if 'what brings you here?' in text:
            if way == Going_To_LeframS or Going_To_LeframC or Going_To_LeframE:
                script.StatusMessage('Need help?')
                script.ChooseNpcOption(1)
        elif 'Well, let\'s see' in text:
            if way == Going_To_LeframS:
                script.StatusMessage('**Bloodroot seed**')
                script.ChooseNpcOption(script.GetAnswerId('Bloodroot seed.', answers)) # Choose
            elif way == Going_To_LeframC:
                script.StatusMessage('**Extracted crystals**')
                script.ChooseNpcOption(script.GetAnswerId('Extracted crystals.', answers)) # Choose
            elif way == Going_To_LeframE:
                script.StatusMessage('**Ethereal essence**')
                script.ChooseNpcOption(script.GetAnswerId('Ethereal essence.', answers)) # Choose
        elif 'Wonderful. The bloodroot' in text:
            script.SetWay(ToBaseSeed, 2)
            script.ForgetNpc()
        elif 'Bring me one crystal' in text:
            script.SetWay(ToBaseCrystais, 2)
            script.ForgetNpc()
        elif 'Kill enough of them' in text:	
            script.SetWay(ToBaseEssence, 2)
            script.ForgetNpc()
        elif 'I already sent you' in text:
            if way == Going_To_LeframS:
                script.SetWay(ToBaseSeed, 2)
                script.ForgetNpc()
            elif way == Going_To_LeframC:
                script.SetWay(ToBaseCrystais, 2)
                script.ForgetNpc()
            elif way == Going_To_LeframE:
                script.SetWay(ToBaseEssence, 2)
                script.ForgetNpc()
