# expand modulo '/storage/emulated/0/major/python/linguagem_major/majôrlang/test/teste.tst'
def helo(){
	mprint('Teste de funções\n')}


def main(){
	dyn i8: number0 = 5
	dyn i16: number1 = 5
	dyn i32: number2 = 5
	dyn i32: number3 = 5
	mprint(number0)
	dyn str: hello_world = '\nHello, World!'
	dyn float:pi  = 3.141592653589793238 # opcao2
	input(hello_world,'ola')
	while (number0 <10){
		if (number0==9){
			mprint('acabou\n')}

		else{
			mprint('ainda não...\n')}
			number0 = number0 + 1
			}
	del number0
	helo()
	mprint(pi)
	mprint(hello_world)
}