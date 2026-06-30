# Controle de Estoque de Medicamentos
## Sobre o projeto

Sistema para controle de estoque de medicamentos desenvolvido em FastAPI.

O projeto surgiu a partir da necessidade de melhorar o controle de medicamentos em um ambiente de trabalho real. A proposta é registrar entradas e saídas de medicamentos, controlar lotes e validade, além de manter o histórico das movimentações realizadas pelos usuários.

## Objetivos

- Controlar medicamentos por lote.
- Registrar entradas e saídas de estoque.
- Identificar o usuário responsável por cada movimentação.
- Controlar validade dos medicamentos.
- Manter histórico para auditoria e rastreabilidade.
- Facilitar o acompanhamento do estoque disponível.

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- PostgreSQL (planejado)

## Estrutura do sistema

### Usuários

Responsável pelo acesso ao sistema e registro das operações realizadas.

### Medicamentos

Cadastro dos medicamentos controlados pelo estoque.

Informações previstas:

- Nome
- Princípio ativo
- Dosagem
- Fabricante

### Lotes

Os medicamentos são controlados através dos lotes.

Cada lote possui:

- Número do lote
- Data de validade
- Quantidade disponível
- Medicamento associado

### Movimentações de Estoque

Registro de todas as operações realizadas no estoque.

Exemplos:

- Entrada de medicamentos
- Saída de medicamentos
- Ajuste de estoque
- Descarte por vencimento
- Perdas

Todas as movimentações devem registrar:

- Usuário responsável
- Data e hora
- Lote utilizado
- Quantidade movimentada

## Modelo de dados

```text
medicamentos
      │
      ▼
    lotes
      │
      ▼
movimentacoes_estoque
      ▲
      │
   usuarios
```

## Regras de negócio

- Um lote não pode existir sem um medicamento.
- Uma movimentação não pode existir sem um lote.
- Toda movimentação deve registrar o usuário responsável.
- O estoque será calculado com base nos lotes cadastrados.
- Não será permitido movimentar quantidade superior à disponível em estoque.
- O histórico de movimentações não deve ser excluído.

## Endpoints previstos

### Autenticação

```http
POST /auth/signin
POST /auth/signup
```

### Medicamentos

```http
GET    /medicamentos
GET    /medicamentos/{id}
POST   /medicamentos
PUT    /medicamentos/{id}
DELETE /medicamentos/{id}
```

### Lotes

```http
GET    /lotes
GET    /lotes/{id}
POST   /lotes
PUT    /lotes/{id}
DELETE /lotes/{id}
```

### Movimentações

```http
GET  /movimentacoes
POST /movimentacoes/entrada
POST /movimentacoes/saida
POST /movimentacoes/ajuste
POST /movimentacoes/descarte
```

## Roadmap

- [ ] Autenticação com JWT
- [ ] Controle de permissões por perfil
- [ ] CRUD de medicamentos
- [ ] CRUD de lotes
- [ ] Controle de movimentações
- [ ] Alertas de vencimento
- [ ] Dashboard de estoque
- [ ] Relatórios de movimentação
- [ ] Migração para PostgreSQL
- [ ] Deploy da aplicação

## Executando o projeto

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar a aplicação:

```bash
uvicorn main:app --reload
```

Documentação da API:

```text
http://127.0.0.1:8000/docs
```

## Status

Projeto em desenvolvimento.
