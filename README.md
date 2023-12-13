
# Racetrack API

API desenvolvida em python utilizando a biblioteca Flask com informações de autódramos 


## Deploy

Para rodar o projeto é preciso ter instalado o Python 

```bash
  https://www.python.org/downloads/
```
A biblioteca do Flask pode ser instalada pelo PIP

Se não houver o PIP, siga :
#### Windows
```
  py -m pip install --upgrade pip
```
#### Mac/Linux
```
  python3 -m pip install --upgrade pip
```
Execute no terminal o app.py

```
  python app.py
```
## Documentação da API

#### Retorna todos os itens

```http
  GET /localhost/racetrack
```

#### Retorna um item

```http
  GET /localhost/racetrack{id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

#### Criar um novo

```http
  POST /localhost/racetrack  
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |
| `name`      | `string` | **Obrigatório**. Nome do autódramo |
| `lenght`      | `string` | **Obrigatório**. Comprimento do autódramo |
| `record`      | `string` | **Obrigatório**. Volta mais rápida em corrida oficial |

#### Editar um item
```http
  PUT /localhost/racetrack/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |
| `index`      | `string` | **Obrigatório**. nome do index que deseja alterar |


#### Deletar um item

```http
  DELETE /localhost/racetrack/{id}
```
| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `id`      | `int` | **Obrigatório**. O ID do item que você quer |

## Autores

- [@FernandoFragassi](https://www.github.com/fernandofragassi)

