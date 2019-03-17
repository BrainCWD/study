def mod(m, d, n):
	i = 0
	ex = 1
	r = m % n
	dictionary = {i: [r, ex]}
	while ex < d:
		i += 1
		ex *= 2
		r = (r ** 2) % n
		dictionary[i] = [r, ex]

	result = 1
	while d > 0:
		if d - dictionary[i][1] >= 0:
			d = d - dictionary[i][1]
			result = (result * dictionary[i][0]) % n
		i = i - 1
	return result

r1 = mod(989341685881536206614879811226442176696794054183020113469687580534700488037777246497088795021641632603311279612984798417044537830394798241345256954980879751731525312571158114896194426315035791665639180362095298518921819575423824559093693272525402946572747524569730265327077859600082056160131745427634112489135044693876086916612762856183039921824068265551615711386910110799037683036465436615934031928287349232508877540167468968229931495901393252735488402915395226252851600289713026918253466980403281610701173519553982, 4514695337564778040593833324277069895862651094541327365639445379916679593788000751178610441941901883129856729148970820717455231377333585305767816991640354833214851310838495314231996617724068259526384601036307745790169894317104921566350282959035189962373815980864041192625904898553862647963174237400383295547164307129585745079041151470195028798042207862127090182577950175793609774355498943465136858582327884002438265843277285537557421240642790977031049224899454311970816186676051897529300839910941355154387366380305436995943761433601847608009308339945810646335018006547040575998189011941959294452577810331600865989261, 5643369171955972550742291655346337369828313868176659207049306724895849492235000938973263052427377353912320911436213525896819039221666981632209771239550443541518564138548119142789995772155085324407980751295384682237712367896381151957937853698793987452967269976080051490782381123192328309953967796750479119434137174848700743264270013280889405885321856003698555642046141751883371500944319785655255954111369662702308195069903285548306489916669565676596431816073830633329205082569391920188985281933948062598563923073549788906782975140820819902641902555473287002521663288093693089719399015653300047886785682559486168222447)
print(r1)


