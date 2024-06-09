# Sistema Bancário Simples em Python

Este projeto é uma implementação simples de um sistema bancário em Python. Ele inclui classes para representar clientes, contas e transações.

## Classes

### Cliente

A classe `Cliente` representa um cliente do banco. Cada cliente tem um endereço e uma lista de contas.

### Conta

A classe `Conta` representa uma conta bancária. Cada conta tem um saldo, um número, uma agência, um cliente associado e um histórico de transações.

### ContaCorrente

A classe `ContaCorrente` é uma subclasse de `Conta` que adiciona um limite de saque e um limite de saques diários.

### Transacao

A classe `Transacao` é uma classe abstrata que representa uma transação bancária.

### Deposito e Saque

As classes `Deposito` e `Saque` são subclasses de `Transacao` que representam um depósito e um saque, respectivamente.

### Historico

A classe `Historico` mantém um registro de todas as transações realizadas em uma conta.

## Uso

Para usar este sistema bancário, você pode criar instâncias das classes `Cliente`, `Conta` e `Transacao`, e usar o método `realizar_transacao` do `Cliente` para realizar transações.
