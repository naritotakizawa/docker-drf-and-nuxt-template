# docker-drf-and-nuxt-template

Django REST framework と Nuxt.js を使ったアプリケーションの、Docker での開発用テンプレート

```
git clone https://github.com/naritotakizawa/docker-drf-and-nuxt-template
cd docker-drf-and-nuxt-template
```

## 開発環境

```
docker-compose -f docker-compose.yml -f dev.yml build
docker-compose -f docker-compose.yml -f dev.yml up
```

標準では、admin admin123 でスーパーユーザーが作成されます。書き換えたい場合は、dev.yml や prod.yml の`SUPERUSER_NAME`、`SUPERUSER_PASSWORD`を書き換えてください。

## 本番環境

```
docker-compose -f docker-compose.yml -f prod.yml build
docker-compose -f docker-compose.yml -f prod.yml up
```

prod.yml の `ALLOWED_HOSTS` に IP アドレスかドメイン名を入れてください。
