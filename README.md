# docker-drf-and-nuxt-template

Django REST framework と Nuxt.js を使ったアプリケーションの、Docker での開発用テンプレートです。このリポジトリをクローンやフォークし、設定を書き換えたり、機能やアプリケーションを加えたりして開発を進めていくと捗るかもしれません。

```
git clone https://github.com/naritotakizawa/docker-drf-and-nuxt-template
cd docker-drf-and-nuxt-template
```

データベースはPostgreSQL、WebサーバーとしてNginx、Nginxの背後にDjango REST frameworkとNuxt.js（ユニバーサルモード）が動いています。

backend以下にDjangoプロジェクトが、frontend以下にNuxtのプロジェクトがあります。

## 入っているDjangoアプリケーションについて

必要がなければ消したり、新しく追加してください。

### register

自作のアプリケーション。カスタムユーザーモデルを定義しています。今のところ追加のフィールド等は何もありませんが、ユーザーモデルを拡張したい場合に備え、あらかじめ定義しています。

## 動かしてみる

### 開発環境

```
docker-compose -f docker-compose.yml -f dev.yml build
docker-compose -f docker-compose.yml -f dev.yml up
```

標準では、admin admin123 でスーパーユーザーが作成されます。書き換えたい場合は、dev.yml や prod.yml の`SUPERUSER_NAME`、`SUPERUSER_PASSWORD`を書き換えてください。

### 本番環境

```
docker-compose -f docker-compose.yml -f prod.yml build
docker-compose -f docker-compose.yml -f prod.yml up
```

prod.yml の `ALLOWED_HOSTS` に IP アドレスかドメイン名を入れてください。
