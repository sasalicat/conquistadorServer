import random

roleRange=[0,1,2,3,4,5,6]
activeEquipment=[4,5,10,11,20,24,27,28]
passiveEquipment=[12,13,14,25,26]
UniquePass=[12,13,14,25,26]
Role=[[0,50],[2,3],[6,7],[8,9],[15,16],[17,18],[19],[42,43],[40,41],[44,45],[48,49]]

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
#createRoleRandom()