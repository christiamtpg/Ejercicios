texto= "joc mih dip zep byt duk luf nok mif lut dyk mas nuk bif rup bit jaf zah les gex gaf loc luc des mok bif voq vyx muf vat vyp nuk gac gop vyf mek gic gip mac dic jas gut vat gus bok zit bis vaq luq zef nex bup nyf jex nip lyk bis joq dap zas vyc rox jop meq not ryx lif gax lat gat dec guh ret veh dos zyf jaq goc nox los ric ras lyc dek voh zec luf lyf rih bit gyx byx vox vah deq nyq zuh dax guf jyt nik gep zyh gif zyf jec vif lat lyt vac beh bit ryk bup vix zuc leh zef bop zoc vuc jok zip ref buc nec ges zet zis zof nyp nic roq byx vif vos mof mif gik nyk zoq jax guh gix beh mok vah beq rop doc laf lex gak gut vyt gup roq bak zyt dac mus zax ryc mip lut lyp gis dyp jok gyq naf dix mif daf vyt dup zos zaq lys baf zaf nok not ras lyt zis daf vih voh jap jos ryh niq vup jup zih vak rys jik mis lok baq ryk roq vip jut lyf bih ruf nuh vip ruh rec lys dit dux gep bak bap nax lyc lyc gat bys vak muq jox myp zah gop nit zyc jok zus jes jat mep mos liq bac lyc lut geq rup bos dot byp myt dut mof lep byf vec nut jaf les def vik lak juc maf bat mex ric dac joh zof rac duf raf mak zic lut goh jep zek reh gic nak mex rat dut bok ryh jyk jyk moq rec vox luq vac rix bap guh dup ruk ras jes giq lyk vot nyh gut zax end"

lista=texto.split(" ")
lista3=[]

for n in range(len(lista)):
    n == lista[0]
    elemento=lista.pop(0)
    if elemento in lista:
        lista3.append(elemento)
        
lista4=list(set(lista3))
lista4.sort()

resultado= ",".join(lista4)
resultado2=resultado.replace(",", " ")

print(resultado2)
