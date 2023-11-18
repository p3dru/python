#sale system
from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "Open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    
    ''' (1 -> SRP)
    Sem Single responsability, a classe order fica responsável pela
    gerência do pedido (adicionar item e calcular o preço, que são 
    realmente responsabilidades da classe), mas também fica responsável
    pelo pagamento, o que fere o SRP
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment method: {payment_type}")
    '''

#(1 -> SRP)
#Para adequar ao SRP é necessário criar uma nova classe que cuide do pagamento
'''
class PaymentProcessor:
    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code {security_code}")
        order.status = "paid" #uma vez que é preciso passar a order para ser verificada
        #já que a classe foi "quebrada" para atender o SRP

    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code {security_code}")
        order.status = "paid" #uma vez que é preciso passar a order para ser verificada
        #já que a classe foi "quebrada" para atender o SRP
'''

#(2 -> Open/Closed) 
'''
Basicamente, criarmos uma classe abstrata que é aberta para extensão,
porém fechada para modificação, ou seja, podemos usar essa classe para
criar novas classes "mais específicas" com base na classe abstrata
'''
#classe aberta que define a base dos pagamentos genéricos
'''
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"
'''
#(3 -> Liskov substitytion principle)
'''
Aqui, retiramos o security_code, pois uma das funções de pagamento/
processor de pagamento, não precisava desse atributo específico, mas
sim de um substituto pra ele.
Nesse caso, o Liskov diz que não é necessário herdar tudo. Podemos apenas
inicializar o que precisamos dentro dos processors, exemplo: se credit e debit
processors, precisam do security code, basta inicializarmos dentro deles. E
como o pay pal precisa de um e-mail, inicializamos, dentro do processor de pay pal,
assimm, cada um fica com sua particularidade, sem ser obrigado pela classe na
qual estão herdando.
'''

# (5 -> Dependency Inversion)
'''
Significa dizer que queremos que nossas classes dependam de classes abstratas
não de classes ou subclasses concretas (no exemplo, temos DebitPaymentProcessor
e PayPalPaymentProcessor dependendo da classe concreta SMSAuth), por isso criaremos
uma classe abstrata.
Criando a classe abstrata abaixo, podemos criar outras classes de autorização
'''
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass

#(4 -> Interface segregation utilizando composição)
class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self, code):
        #Aqui está autorizando tudo por padrão
        print(f"Verifying code {code}")
        self.authorized = True
    
    #jeito mais clean de alterar uma variável
    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor(ABC):
    @abstractmethod
    #tirarmos o security_code dos argumentos obrigatórios
    def pay(self, order):
        pass

    '''
    (4 -> Interface Segregation)
    Aqui poderíamos pensar de colocar mais uma abstração dentro
    da interface geral, porém isso feriria a segragação de interfaces
    @abstractmethod
    def auth_sms(self, code):
        pass
    '''

#(4 -> Interface segregation)
'''
aqui criamos uma interface que faz envio de sms de autenticação
de dois fatores, mas nem todas as classes de pagamento suportam
essa funcionalidade, então, basta criarmos um "código adicional"
para a classe abstrata anterior, que forneça a possibilidade de
enviar sms. E assim, os processors que suportarem o envio de sms
simplesmente podem "herdar" diretamente dessa interface
'''
'''
É uma forma de se separar as interfaces
class PaymentProcessor_SMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass
'''

#(4 -> Interface segregation utilizando composição)
class DebitPaymentProcessor(PaymentProcessor):
# (4 -> Interface segregation)
#class DebitPaymentProcessor(PaymentProcessor_SMS): #Já que suporta envio de sms
# (3 -> Liskov) class DebitPaymentProcessor(PaymentProcessor):
    #aqui inicializa o security_code como "particularidade" dessa classe
    #sem que seja uma obrigação da classe mãe
    #(5 -> Dependency inversion, agora, passamos a classe abstrata Authorizer)
    def __init__(self, security_code, authorizer: Authorizer):
    #(4 -> Passávamos a classe concreta SMSAuth)
    #def __init__(self, security_code, authorizer: SMSAuth):
        self.authorizer = authorizer #aqui importa a autorização de SMSAuth
        self.security_code = security_code

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    #aqui inicializa o security_code como "particularidade" dessa classe
    #sem que seja uma obrigação da classe mãe
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor): #Já que suporta envio de sms
    #aqui inicializa o email_address como "particularidade" dessa classe
    #sem que seja uma obrigação da classe mãe
    def __init__(self, email_address, authorizer: SMSAuth):
        self.authorizer = authorizer #aqui importa a autorização de SMSAuth
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not Authorized")
        print("Processing credit payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50);
order.add_item("SSD", 1, 150);
order.add_item("USB cable", 2, 5);

print(order.total_price())
#processor = PaymentProcessor() # (1 -> SRP) aqui criamos um processador de pagamentos
# (0) order.pay("debit", "9099909877"); -> Vira obsoleto, visto que agora, pagamos com o processor
#(4 -> Interface Segregation utilizando composição)
authorizer = SMSAuth() 
processor = DebitPaymentProcessor("9099909877", authorizer) #authorizer que é o autenticador do código sms recebido
authorizer.verify_code(23234132)
#  (3 -> Liskov)
#processor = PayPalPaymentProcessor("csk@email.com") #passa o argumento email address para o PayPalProcessor
processor.pay(order) #aqui apenas paga a order

# (2 -> SRP + OpenClosed)
'''
processor = DebitPaymentProcessor() #aqui alteramos apenas a classe que será responsável pelo pagamento
processor.pay(order, "9099909877") #pay pelo fato de no processor, ser definido o método de pagamento
'''
#(1 -> SRP)
#processor.pay_debit(order, "9099909877") # -> Passamos a order pois agora é necessário


#Muitas vezes utilzar composição ao invés de herança pode ser bem melhor