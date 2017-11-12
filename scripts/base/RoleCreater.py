import random

roleRange=[0,1,2,3,4,5,7,8,9,10]
activeEquipment=[4,5,10,11,20,24,27,52,53,54,55,56,57]
passiveEquipment=[12,13,14,21,22,23,25,26,28,29,30,31,32,33,34,35,36,37,38,39,51,58,59,60]
UniquePass=[12,13,14,25,26,32,33,34,58,59,60]
Role=[[0,50],[2,3],[6,7],[8,9],[15,16],[17,18],[19],[42,43],[40,41],[44,45],[46,47]]

def	createRoleRandom():
	roleNo=random.choice(roleRange)
	roleSkill=(Role[roleNo])[:]
	print("before rolelist is{0}".format(roleSkill))
	active=activeEquipment[:]
	for i in range(3):
		ans=random.choice(active)
		roleSkill.append(ans)
		active.remove(ans)
	print(roleSkill)
	passive=passiveEquipment[:]
	print("psaaive is{0}".format(passive))
	for i in range(5):
		ans=random.choice(passive)
		roleSkill.append(ans)
		print('passive ans is{0}'.format(ans))
		if ans in UniquePass:
			print("enter ans in")
			passive.remove(ans)
	print('final ans is{0}'.format(roleSkill))
	return {"kind":roleNo,"equipmentNos":roleSkill}
def getDefaultRole():#獲得預設的新手角色
	roleNo=9;
	roleSkill=[44,45,54,55,56,29,21,22,23,51]
	return {"kind":roleNo,"equipmentNos":roleSkill}
#createRoleRandom()