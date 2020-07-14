from matplotlib import pyplot as plt
import numpy as np

val={'loss': [2.16989777242537, 2.091913753276249, 2.015111657355329, 1.9441042889794, 1.8794760223772886, 1.8569588918480084, 1.7841548662391498, 1.7553381894132216, 1.732816037514227, 1.73138930471681, 1.714653929360479, 1.7093376470126693, 1.6202340649186278, 1.6500968229856423, 1.631462035419272, 1.6314811809457463, 1.5942191906112562, 1.5904150626642242, 1.599038264734282, 1.591643797407905, 1.5582722013802837, 1.5221368914885487, 1.532140126331247, 1.5793778090168247, 1.5236272245859928, 1.5395346236743515, 1.491430306177345, 1.5284548097377202, 1.5079880815615756, 1.5208387889450403, 1.4839198383495962, 1.4801106813142626, 1.465815786835101, 1.4981892683523164, 1.465543800120731, 1.4525659101472483, 1.4689344930991852, 1.4469297987094027, 1.4465293712753187, 1.49366619604097, 1.4296524670484254, 1.448337776197804, 1.415789719965818, 1.4115106467720415, 1.4166958460704886, 1.4351365180324307, 1.4292121268004823, 1.429461105264348, 1.404923924439245, 1.4336241766703215, 1.43760829434978, 1.432682636401636, 1.385139810095588, 1.4298666938603353, 1.426822556008538, 1.4271166187396152, 1.4109405973832385, 1.3829808942705608, 1.4244393414730647, 1.3964066269586413, 1.3989536856575835, 1.4092933171087032, 1.371610386766118, 1.3955167746372361, 1.4038184186537488, 1.391259719999574, 1.4021160345283343, 1.3678550883162794, 1.3689151925148724, 1.393510163259163, 1.383005448811346, 1.3903251697691223, 1.3843997022230847, 1.388558964935138, 1.3740984681698916, 1.35756342359584, 1.418234121885231, 1.3899206566296036, 1.3912459097320227, 1.355251311827049, 1.3814700370212254, 1.3641276586827615, 1.330550215227141, 1.3751516908192807, 1.3715336880237936, 1.345452920996028, 1.3569873494210003, 1.355862073761096, 1.3470029059073907, 1.3818317703205905, 1.382251631441734, 1.359348093005393, 1.3666711363861028, 1.374409042674003, 1.388815589945951, 1.3644959249084803, 1.3340067083029439, 1.3458920451376934, 1.3532272422914025, 1.3520588231601303], 'acc': [0.2589928057553957, 0.3039568345323741, 0.2985611510791367, 0.33273381294964033, 0.3381294964028777, 0.33453237410071945, 0.3669064748201439, 0.34532374100719426, 0.35611510791366907, 0.36330935251798563, 0.3597122302158274, 0.37769784172661874, 0.3956834532374101, 0.38489208633093525, 0.37949640287769787, 0.39928057553956836, 0.4046762589928058, 0.3920863309352518, 0.41187050359712235, 0.4172661870503597, 0.42086330935251803, 0.4496402877697842, 0.45143884892086333, 0.42086330935251803, 0.41187050359712235, 0.4352517985611511, 0.45683453237410077, 0.46223021582733814, 0.4460431654676259, 0.4388489208633094, 0.4676258992805756, 0.46582733812949645, 0.4694244604316547, 0.4694244604316547, 0.48741007194244607, 0.48201438848920863, 0.4694244604316547, 0.4838129496402878, 0.4676258992805756, 0.47302158273381295, 0.4838129496402878, 0.47302158273381295, 0.48741007194244607, 0.5, 0.4838129496402878, 0.48201438848920863, 0.4784172661870504, 0.4784172661870504, 0.4802158273381295, 0.4712230215827338, 0.5035971223021583, 0.48741007194244607, 0.5143884892086331, 0.4802158273381295, 0.4946043165467626, 0.4802158273381295, 0.4928057553956835, 0.5035971223021583, 0.48201438848920863, 0.5017985611510791, 0.5017985611510791, 0.48561151079136694, 0.4892086330935252, 0.48741007194244607, 0.49640287769784175, 0.5017985611510791, 0.512589928057554, 0.5071942446043166, 0.49640287769784175, 0.4946043165467626, 0.5035971223021583, 0.48741007194244607, 0.5107913669064749, 0.5053956834532375, 0.4928057553956835, 0.5071942446043166, 0.4928057553956835, 0.4892086330935252, 0.525179856115108, 0.5017985611510791, 0.4910071942446043, 0.4982014388489209, 0.525179856115108, 0.4982014388489209, 0.5053956834532375, 0.5269784172661871, 0.5197841726618705, 0.5287769784172662, 0.5143884892086331, 0.49640287769784175, 0.48561151079136694, 0.4928057553956835, 0.5197841726618705, 0.4946043165467626, 0.5215827338129496, 0.5017985611510791, 0.512589928057554, 0.5107913669064749, 0.5161870503597122, 0.5161870503597122]}
train={'loss': [2.262524000737677, 2.1833095453586817, 2.1237662673491164, 2.055225159221665, 1.9873237216126374, 1.9367541505093397, 1.90429244555873, 1.8660556579526528, 1.8406842140735926, 1.8129636364853727, 1.7940228561148108, 1.76339741702891, 1.7564562910325299, 1.7416545013174476, 1.7348408363666772, 1.694416239449592, 1.6842804318147082, 1.6757901029468076, 1.6730821714361674, 1.6595963351459424, 1.644636495974054, 1.6470882479085962, 1.6388975549040987, 1.6304767602706847, 1.6339083795230913, 1.6147678594866235, 1.6131720204570976, 1.6093621950426538, 1.607381059915693, 1.5694991352152527, 1.5832633424102023, 1.5857164905279009, 1.57945081188471, 1.566500216796685, 1.572567125177977, 1.580603948371539, 1.5702899964518566, 1.5579239995647762, 1.5406574860648001, 1.5450050425232693, 1.5483378762526137, 1.5463659476442455, 1.5400937968764563, 1.5373648441678756, 1.5262398757380569, 1.5203648543456778, 1.5086885085244397, 1.5210314170948203, 1.5368489174427333, 1.5257632134860977, 1.5018949599681553, 1.4969002007448822, 1.5028098391299425, 1.5034067521946064, 1.4959171011240155, 1.4855005274175113, 1.4986182277628, 1.457373710094151, 1.48008909739894, 1.4923346802406785, 1.5024621540085408, 1.4694884030156117, 1.4780550984426157, 1.4738203456293004, 1.4690439275686178, 1.4719215522663227, 1.4802523383461093, 1.4674463348764601, 1.4763346579064967, 1.436603995675368, 1.4570582174166604, 1.4578188495517272, 1.4292799176022224, 1.451798730272475, 1.4552622613075858, 1.4489207679305334, 1.4535045481321722, 1.4629585942786758, 1.4300703862890662, 1.42994991041318, 1.4453186351728637, 1.4211431934625776, 1.4265103266941561, 1.415971122836671, 1.421463562146262, 1.419481796149891, 1.4460129425238772, 1.4424084307247178, 1.4019393008774248, 1.4320222704242374, 1.4340004879409347, 1.4025851465359762, 1.3996002375337593, 1.4148993544558766, 1.4186424513575446, 1.4212244892516077, 1.4104135780413616, 1.4023917002301989, 1.3852978914110492, 1.3917693411166243], 'acc': [0.16597510373443983, 0.23858921161825725, 0.2692946058091286, 0.2829875518672199, 0.30622406639004146, 0.31742738589211617, 0.33734439834024893, 0.3385892116182573, 0.34730290456431534, 0.35435684647302906, 0.366804979253112, 0.37095435684647304, 0.37219917012448134, 0.37344398340248963, 0.3780082987551867, 0.3970954356846473, 0.3946058091286307, 0.4058091286307054, 0.395850622406639, 0.4099585062240664, 0.4178423236514523, 0.4215767634854772, 0.41369294605809126, 0.42448132780082987, 0.41244813278008297, 0.4195020746887967, 0.43236514522821573, 0.42738589211618255, 0.43070539419087134, 0.44232365145228214, 0.44066390041493775, 0.44190871369294604, 0.4190871369294606, 0.43941908713692945, 0.42946058091286304, 0.4468879668049792, 0.4352697095435685, 0.44937759336099586, 0.45601659751037343, 0.45145228215767635, 0.44232365145228214, 0.43817427385892116, 0.44937759336099586, 0.45269709543568465, 0.4477178423236514, 0.46639004149377594, 0.4597510373443983, 0.4639004149377593, 0.4605809128630705, 0.45394190871369294, 0.46887966804979253, 0.46680497925311204, 0.46514522821576765, 0.46763485477178424, 0.45435684647302904, 0.475103734439834, 0.4614107883817427, 0.4738589211618257, 0.4721991701244813, 0.4705394190871369, 0.46597510373443984, 0.4767634854771784, 0.4618257261410788, 0.46804979253112033, 0.4784232365145228, 0.470954356846473, 0.4759336099585062, 0.4726141078838174, 0.4701244813278008, 0.4871369294605809, 0.5004149377593361, 0.4784232365145228, 0.4838174273858921, 0.4780082987551867, 0.4858921161825726, 0.4788381742738589, 0.470954356846473, 0.483402489626556, 0.495850622406639, 0.4933609958506224, 0.4912863070539419, 0.5012448132780083, 0.4995850622406639, 0.4933609958506224, 0.4817427385892116, 0.4929460580912863, 0.4867219917012448, 0.49419087136929457, 0.4937759336099585, 0.5016597510373444, 0.4825726141078838, 0.5, 0.5062240663900415, 0.4970954356846473, 0.4904564315352697, 0.48091286307053943, 0.49460580912863067, 0.5020746887966805, 0.5103734439834025, 0.495850622406639]}
epoch_idx=np.arange(len(train["acc"]))
epoch_idx+=1
'''
plt.title("loss graph")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.plot(epoch_idx,train['loss'],color="green")
plt.plot(epoch_idx,val['loss'],color='red')
plt.show()

plt.title("Accuracy graph")
plt.xlabel("epoch")
plt.ylabel("Accuracy")
plt.plot(epoch_idx,train['acc'],color="green")
plt.plot(epoch_idx,val['acc'],color='red')
plt.show()'''

print(min(val["loss"]))