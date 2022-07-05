# DynamoDB local on Docker🐳
## Description
Docker上でDynamoDB localを、python3.9のBoto3で扱えるようにしたリポジトリです．

## Tree🌳
```sh
.
├── Makefile
├── README.md
├── docker
│   └── python
│       ├── Dockerfile
│       └── requirements.txt
├── docker-compose.yml
├── dynamodb-local-data
│   └── .gitkeep
└── src
    └── sample.py

4 directories, 7 files
```
- `Makefile`
    - docker-composeのコマンドを記述しているファイル．
- `docker/python/`
    - pythonコンテナのDockerfileとpythonライブラリのリストが入っているディレクトリ．
- `dynamodb-local-data/`
    - DynamoDB localのdbデータが格納されるディレクトリ．
- `src/`
    - pythonコンテナで扱うソースコードを入れるディレクトリ．

## How to use🔧
### コンテナのビルド
```sh
make build
```

### コンテナの起動
```sh
make up
```

### コンテナの終了
```sh
make down
```

### pythonコンテナに入る
```sh
make exec
```
- 入った後は`python [filename].py`で実行できる．

- DynamoDBを扱うときのURLは`http://dynamodb-local:8000`
